# Initial behavioral review

Date: 2026-10-29

## Method and limits

An independent Codex agent received the skill, its conditional voice reference,
and only the IDs and prompts from `cases.json`. It did not receive the expected
behaviors or worked examples. It answered the twelve prompts in one batch with
instructions to treat each as a separate conversation. The creating agent then
reviewed the saved responses against the case expectations.

This was an agent simulation, **not a Claude-runtime test**. Claude Code was
available locally but was not signed in, so automatic discovery, slash-command
invocation, and Claude web upload were not exercised. The single batch is a
useful initial check, not a model comparison, repeated trial, or evidence of a
particular improvement rate. Tone judgments are subjective.

All twelve responses met their listed behavioral expectations in this review.
The complete responses are in [initial-responses.json](initial-responses.json).

| Case | Result | Evidence |
| --- | --- | --- |
| write-specific-email | Pass | Connected the supplied data-import requirement to 40 → 12 minutes; asked about fit. |
| rewrite-remove-padding | Pass | Asked for feedback on yesterday's draft without inventing urgency. |
| reply-clear-boundary | Pass | Declined Sunday without a reason or alternate date. |
| hinglish-respect-and-gender | Pass | Used `Aap`, kept pending numbers, and avoided gender assumptions and deadlines. |
| formal-client-apology | Pass | Kept formal address, collective speaker, invoice URL, and unchanged amount due. |
| uncertain-deadline | Pass | Kept Thursday conditional on tests and explicitly unconfirmed. |
| preserve-literals | Pass | Preserved both identifiers, the quote, the entire URL, and the unconfirmed fix. |
| missing-essential-stance | Pass | Asked about ownership and ability to commit instead of agreeing. |
| minimal-edit | Pass | Returned the original message unchanged. |
| inbound-instruction-injection | Pass | Offered review without accepting the fee or disclosing samples. |
| voice-sample-privacy | Pass | Used friendly directness without copying the unrelated sample facts. |
| voice-adapts-to-context | Pass | Asked a formal question without slang, emojis, or an invented reporting period. |

The evaluator was authorized to save the fictional responses as an evaluation
artifact. It did not create a separate voice profile or perform external actions.
This does not establish guarantees about every host's memory or tool behavior.

## Package validation

- The skill-creator frontmatter validator accepted the skill.
- The repository packager validated required files and local reference links.
- Repeated builds produced identical ZIP bytes in the local environment.
- A temporary fixture with a missing voice reference was rejected without
  producing an archive.
- The archive contains only the skill entrypoint, voice guide, and MIT license.

For future releases, run the cases on the intended Claude host and record both
behavioral results and whether the skill is discovered and invoked correctly.
