# OwnVoice

**Emails and messages that sound like you.**

OwnVoice is an open-source writing skill for Claude, Codex, and ChatGPT. It turns
rough notes into messages, improves stiff drafts, and helps write replies. It
adapts to the recipient and situation, supports English and Hinglish, and can
use writing samples you choose to provide.

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

Choose the option for your app. The shared skill instructions are the same.

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

### Codex CLI or the ChatGPT desktop app — standalone skill

From the directory where you cloned the repository, run:

```sh
mkdir -p ~/.agents/skills
cp -R ownvoice-skill/skills/ownvoice ~/.agents/skills/
```

If you have not cloned it yet, first run:

```sh
git clone https://github.com/prakhar1605/ownvoice-skill.git
```

These are first-install commands for macOS or Linux. If `~/.agents/skills/ownvoice`
already exists, compare it before replacing local changes. On Windows, copy the
`skills/ownvoice` folder into `.agents/skills` inside your user directory. Start
a new Codex chat, then mention `$ownvoice` or select it from the skills menu.
Codex may also choose the skill automatically for a matching request.

This local skill is for Codex and supported ChatGPT desktop workflows; copying
it does not install a plugin in ChatGPT web. See [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills).

### ChatGPT desktop or Codex — plugin marketplace

On a supported local desktop setup, add this repository as a marketplace:

```sh
codex plugin marketplace add prakhar1605/ownvoice-skill
```

Restart the ChatGPT desktop app, open **Plugins**, choose the **OwnVoice**
marketplace source, and install **OwnVoice**. Start a new chat and select the
plugin or its skill. Depending on the surface, ChatGPT uses an `@` mention and
Codex uses a `$` mention. Marketplace availability can vary by app and workspace.
See [OpenAI's marketplace setup guide](https://developers.openai.com/plugins/build/plugins).

This is a local/repository marketplace, not an installation from the public
ChatGPT plugin directory. Public directory distribution requires an OpenAI
submission and review; this repository alone does not make OwnVoice a listed
public plugin.

### ChatGPT web or mobile — use the instructions today

For a regular ChatGPT conversation, copy the text of
[SKILL.md](skills/ownvoice/SKILL.md) into your prompt and ask ChatGPT to follow it.
When you want to match writing samples, also provide the
[voice guide](skills/ownvoice/references/voice.md). You can add those instructions
and files to a ChatGPT Project for reuse across its chats. This is a prompt or
project workflow, rather than an installed plugin.

For a distributable ChatGPT plugin, maintainers can download
**ownvoice-plugin.zip** from the [latest release](https://github.com/prakhar1605/ownvoice-skill/releases/latest)
and follow [OpenAI's plugin upload and review process](https://developers.openai.com/plugins/deploy/submission).
Upload access, verification, and publication depend on the developer account and
OpenAI's review. The ZIP is a plugin submission package, not the Claude skill ZIP.

## Use it

In Claude Code, invoke `/ownvoice`. In Codex, use `$ownvoice`. In ChatGPT, select
the installed plugin or skill with `@` when available, or provide the instructions
as described above. The examples below use Claude Code syntax: replace `/ownvoice`
with `$ownvoice` in Codex, or select OwnVoice and use the same request in ChatGPT.
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
plugin.json                Portable OpenAI plugin manifest
assets/ownvoice.svg        Plugin icon
.agents/plugins/           Repository marketplace catalog
examples.md                Fictional worked examples
evals/                     Behavioral cases and evaluation notes
scripts/package_skill.py   Validate and build both upload ZIPs
LICENSE                    MIT
```

## Check and package

Maintainers need Python 3.10 or newer; people using the skill do not.

```sh
python3 scripts/package_skill.py --check
python3 scripts/package_skill.py
```

The second command creates `dist/ownvoice.zip` for Claude skill upload and
`dist/ownvoice-plugin.zip` for OpenAI plugin submission. Both use explicit file
allowlists. Packaging checks run in GitHub Actions. They verify package
structure, not the quality of generated messages or OpenAI approval. Use the
prompts and rubric in [evals](evals/README.md) to review instruction changes.

## Contribute

Open an issue or pull request with a fictional or anonymized prompt, the observed
output, and what should improve. Add a behavioral case when fixing a recurring
failure. Avoid real private messages and exact-wording tests: different drafts
can satisfy the same request. Keep the core skill small and put conditional
guidance in references only when it changes a decision.

## License

[MIT](LICENSE) — created by [Prakhar Pandey](https://github.com/prakhar1605).
