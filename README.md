# OwnVoice

**Emails and messages that sound like you.**

OwnVoice is an open-source Claude skill for writing from rough notes, improving
stiff drafts, and replying to messages. It adapts to the recipient and situation,
supports English and Hinglish, and can use writing samples you choose to provide.

> **Before**
> I hope this message finds you well. I wanted to take a moment to kindly follow
> up on my previous email regarding the opportunity.
>
> **After**
> Hi Ankit, following up on my email about the role. Any update on next steps?

A recruiter email, a client apology, and a WhatsApp message need different kinds
of care. OwnVoice keeps those differences. It preserves facts, uncertainty, and
commitments while making the wording easier to read.

## Install

### Claude Code

Clone the repository and copy the skill into your personal skills directory:

```sh
git clone https://github.com/prakhar1605/ownvoice-skill.git
mkdir -p ~/.claude/skills
cp -R ownvoice-skill/skills/ownvoice ~/.claude/skills/
```

These commands are for a first install on macOS or Linux. If you already have an
`ownvoice` folder there, compare it before replacing your local changes. On
Windows, copy `skills/ownvoice` into the `.claude/skills` folder inside your user
directory. To install only in one project, use that project's `.claude/skills/`
directory instead. Start a new Claude Code session after installation.

See [Claude Code's skill documentation](https://code.claude.com/docs/en/skills)
for supported locations and invocation details.

### Claude web or desktop

Download **ownvoice.zip** from the [latest release](https://github.com/prakhar1605/ownvoice-skill/releases/latest).
Open **Customize → Skills**, choose the upload option, and upload the ZIP.
Enable the skill if needed. Use the release asset; GitHub's source-code ZIP
contains the whole repository.

The archive contains an `ownvoice/` folder with `SKILL.md`, the voice guide, and
the license. See [Anthropic's custom-skill guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
if your interface uses different labels.

## Use it

In Claude Code, invoke `/ownvoice`. In Claude chat, ask Claude to use OwnVoice.
You can name a mode or simply describe what you need.

| Mode | What you provide | What you get |
| --- | --- | --- |
| **Write** | Rough notes and the intended outcome | A draft suited to the recipient |
| **Rewrite** | An existing draft | A natural edit that keeps its meaning |
| **Reply** | An incoming message and your position | A response that addresses the relevant points |

### Write from notes

```text
/ownvoice write
Email Ankit, a recruiter. We discussed the backend role last week.
I want an update on next steps. Keep it friendly and direct.
```

### Rewrite a draft

```text
/ownvoice rewrite
This is a Slack message to my teammate. Keep the uncertainty:
"I wanted to kindly inform you that I may be able to share the patch
by Thursday, provided the flaky test is resolved."
```

### Reply in Hinglish

```text
/ownvoice reply
Friend: "Aaj 7 baje call kar sakte hain?"
Say that 7 doesn't work for me and ask if 8 works. Roman Hinglish.
```

### Match your voice

```text
/ownvoice write
Slack message to my team: the preview is ready; feedback by Friday
would help. Use these samples for style only:
1. "Quick update: the fix is live. Let me know if it still happens."
2. "Thanks for checking. I'll take a look this afternoon."
```

Samples are optional. The skill uses their style without transferring their
facts into the new message. It does not create a saved voice profile unless you
explicitly request one and your host supports it.

By default, you get one draft. Ask for alternatives, a shorter version, or an
explanation of the edits when you want them. If a reply would require deciding
something you haven't specified, such as accepting an offer, the skill asks.

More [worked examples](examples.md) cover formal messages, refusals, technical
details, Hinglish, and drafts that already work.

## What to expect

- English and Hinglish with tone adapted to the relationship and channel.
- Facts, names, numbers, links, and commitments preserved during editing.
- Short messages when the task is simple; enough context and care when it isn't.
- No added anecdotes, deliberate typos, forced slang, or fixed banned-word list.

OwnVoice prepares text. It does not send messages, access your inbox, or add a
background service. The runtime skill consists of Markdown files; your chosen
AI host still processes the text you supply under its own settings and terms.
Writing quality is contextual, and the skill makes no AI-detector guarantees.

## Repository

```text
skills/ownvoice/
  SKILL.md                 Skill entrypoint
  references/voice.md      Optional voice-matching guidance
examples.md                Fictional worked examples
evals/                     Behavioral cases and evaluation notes
scripts/package_skill.py   Validate and build the upload ZIP
LICENSE                    MIT
```

## Check and package

Maintainers need Python 3.10 or newer; people using the skill do not.

```sh
python3 scripts/package_skill.py --check
python3 scripts/package_skill.py
```

The second command creates `dist/ownvoice.zip` using an explicit file allowlist.
Packaging checks run in GitHub Actions. They verify the package structure, not
the quality of generated messages. Use the prompts and rubric in [evals](evals/README.md)
to review behavior after changing the instructions.

## Contribute

Open an issue or pull request with a fictional or anonymized prompt, the observed
output, and what should improve. Add a behavioral case when fixing a recurring
failure. Avoid real private messages and exact-wording tests: different drafts
can satisfy the same request. Keep the core skill small and put conditional
guidance in references only when it changes a decision.

## License

[MIT](LICENSE) — created by [Prakhar Pandey](https://github.com/prakhar1605).
