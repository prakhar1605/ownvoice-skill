#!/usr/bin/env python3
"""Validate and package OwnVoice using only Python's standard library.

Frontmatter deliberately supports single-line, plain or quoted name/description
values only. It is not a general YAML parser.
"""

import argparse
from pathlib import Path, PurePosixPath
import re
import stat
import sys
from urllib.parse import unquote, urlsplit
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ownvoice"
FILES = {
    "ownvoice/LICENSE": ROOT / "LICENSE",
    "ownvoice/SKILL.md": SKILL / "SKILL.md",
    "ownvoice/references/voice.md": SKILL / "references" / "voice.md",
}


def regular_file(path):
    """Reject symlink files and symlink parent directories inside the repo."""
    for part in (path, *path.parents):
        if part == ROOT:
            break
        if part.is_symlink():
            raise ValueError(f"Symlinks are not allowed: {part.relative_to(ROOT)}")
    if not path.is_file():
        raise ValueError(f"Required file is missing: {path.relative_to(ROOT)}")


def frontmatter_value(frontmatter, key):
    values = re.findall(rf"^{key}:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    if len(values) != 1:
        raise ValueError(f"Frontmatter needs exactly one single-line {key} field")
    value = values[0].strip()
    if value.startswith(("'", '"')):
        if len(value) < 2 or value[-1] != value[0]:
            raise ValueError(f"Unclosed quote in frontmatter {key}")
        value = value[1:-1].strip()
    elif value.startswith(("|", ">", "[", "{", "#")) or value in ("null", "~"):
        raise ValueError(f"Frontmatter {key} must be a single-line string")
    if not value:
        raise ValueError(f"Frontmatter {key} must not be empty")
    return value


def validate_links(path, text):
    # Inline links/images and reference definitions; optional Markdown titles.
    # Exclude fenced code so illustrative examples are not treated as links.
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[ \t]*$", "", text)
    links = re.findall(r"\]\(\s*(<[^>]+>|[^\s)]+)", text)
    links += re.findall(r"(?m)^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", text)
    for link in links:
        target = link.strip("<>")
        if re.match(r"^[A-Za-z]:[/\\]", target):
            raise ValueError(f"Absolute local link in {path.name}: {target}")
        parsed = urlsplit(target)
        if parsed.scheme and parsed.scheme != "file":
            continue
        if parsed.scheme == "file" or parsed.netloc:
            raise ValueError(f"Absolute local link in {path.name}: {target}")
        local = unquote(parsed.path)
        if not local:
            continue  # A fragment within the current document.
        relative = PurePosixPath(local)
        if relative.is_absolute() or ".." in relative.parts or "\\" in local:
            raise ValueError(f"Unsafe local link in {path.name}: {target}")
        linked = path.parent / relative
        if not linked.is_relative_to(SKILL):
            raise ValueError(f"Link leaves the skill directory: {target}")
        regular_file(linked)
        if linked not in FILES.values():
            raise ValueError(f"Linked file is not included in the package: {target}")


def validate():
    for path in FILES.values():
        regular_file(path)
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", skill_text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md must start with YAML frontmatter between --- lines")
    if frontmatter_value(match[1], "name") != "ownvoice":
        raise ValueError("Frontmatter name must be ownvoice")
    frontmatter_value(match[1], "description")
    for path in FILES.values():
        if path.suffix == ".md":
            validate_links(path, path.read_text(encoding="utf-8"))


def build():
    output = ROOT / "dist" / "ownvoice.zip"
    if output.parent.is_symlink() or output.is_symlink():
        raise ValueError("Package destination must not be a symlink")
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, path in sorted(FILES.items()):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = (stat.S_IFREG | 0o644) << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, path.read_bytes(), compresslevel=9)
    print(f"Built {output.relative_to(ROOT)} ({len(FILES)} files)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without building")
    args = parser.parse_args()
    try:
        validate()
        if args.check:
            print("OwnVoice skill is valid")
        else:
            build()
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
