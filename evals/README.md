# Behavioral evaluation

`cases.json` contains fictional prompts and observable expectations. Use it to
check whether an instruction change improves the skill without changing what
the sender means. The possible outputs in `../examples.md` are illustrations,
not golden answers.

## Run a review

1. Load `skills/ownvoice/SKILL.md` into the target host, with its voice reference
   available. Record the host and model or agent used.
2. Start a fresh conversation for each case. Provide only its `prompt`, not the
   `expected_behavior` list. Collect the actual response.
3. Review each response against its expectations. Record pass, partial, or fail,
   and quote the part that supports the judgment.
4. Recheck failures after a change. If the instructions changed more broadly,
   also recheck the other affected cases.

A good result preserves facts, intent, commitments, relevant technical strings,
and relationship context. Naturalness remains a judgment call. Do not grade by
exact wording or a made-up human-likeness score. Check punctuation when a case
explicitly tests the prose default or a preservation rule.

For privacy and instruction-boundary cases, inspect any tool actions as well as
the text: a clean-looking response alone does not prove that nothing was saved.
Keep real private messages out of published cases and reports.

## What these checks cover

- Writing a specific email, rewriting padding, and replying with a clear boundary.
- Roman Hinglish with respectful address and no gender assumption.
- Formal client language and an explicitly unconfirmed deadline.
- Exact identifiers, quoted words, and URLs.
- A missing decision that calls for a question instead of a commitment.
- Minimal edits to an already natural draft.
- Instructions embedded in an incoming message.
- Voice samples used for style without copying their private facts.
- Explicit formality overriding casual samples.

The package check in GitHub Actions validates structure and archive contents.
It does not invoke a language model or validate automatic skill discovery.
See [the initial review](initial-review.md) for the evidence and limitations of
the first release.

## Version 2 checks

The seven cases from `thread-quoted-offer` through `sender-edit-evidence` cover
quoted history, grammar-only edits, translation of instructions mixed with
message content, two length limits, an impossible limit and sample attribution.
For character budgets, count only the actual message, including its link and
punctuation. In the revision case, keep the previous turn’s limit in force.

## Version 2.1 checks

The four cases from `plain-recruiter-email` through `grammar-only-style-exception`
cover natural email and post drafts, exact quotes, and grammar-only requests.
Check for stock wording and compare the final draft with the original facts.
