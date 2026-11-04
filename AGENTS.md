# Instructions for AI Coding Agents

These instructions apply to AI assistants working anywhere in the CourtListener
repository, regardless of the assistant or model used. They supplement, rather
than replace, the project's existing development rules. An AI agent's output
is not a substitute for an accountable human contributor.

## Read the project's rules first

Before proposing or changing files, read and follow:

1. [`CLAUDE.md`](CLAUDE.md) — the repository's coding, testing, and
   pull-request requirements. Treat its technical rules as applying to all AI
   coding agents, not only Claude.
2. [Guidelines for Contributions](https://wiki.free.law/c/courtlistener/dev-guide/getting-started#guidelines-for-contributions)
   — the project's Git, review, quality, and contributor workflow.
3. [AI Policy for Volunteers](https://wiki.free.law/c/ai-policies-resources/policies/artificial-intelligence-policies-for-volunteers-working-with-free-law-project)
   — human accountability, acceptable AI use, data handling, and incident
   reporting.

Read [`FRONTEND.md`](FRONTEND.md) before touching frontend code, the
[testing guide](https://wiki.free.law/c/courtlistener/dev-guide/automated-tests)
before writing tests, and the
[database migration guide](https://wiki.free.law/c/courtlistener/dev-guide/database-migrations)
before making migrations. Consult the current wiki pages rather than
assuming that a summary in this file replaces them.

## Keep a human accountable

- A human must be able to understand, explain, defend, and take ownership of
  every proposed change before it is submitted as reviewed work.
- Do not undertake changes to systems the human contributor cannot
  understand and verify, except simple, self-contained changes such as typos.
  For project-specific uncertainties, seek guidance from the FLP staff contact.
- Identify the **specific AI model** used for each AI-assisted contribution.
  The human contributor must review the work and certify that review. Never
  assert that a human reviewed the output or check the PR template's
  AI-review certification box without that person's actual confirmation.
- Keep an unreviewed AI-assisted pull request in draft state. Do not describe
  AI-generated changes as already approved or verified by a human.

## Protect data when using AI tools

- Use an authenticated account and opt out of the AI provider's training and
  data-collection uses as required by FLP policy before processing FLP work.
- Publicly available legal materials (such as public opinions and dockets)
  are generally permitted as AI inputs.
- Never submit nonpublic personally identifiable information or information
  from sealed, expunged, or restricted court records to an AI assistant.
  Replace such information with generic placeholders before use.
- Do not include secrets, credentials, or sensitive configuration in prompts.
  If a category of data is not covered by FLP's policy, consult its internal
  AI team rather than assuming it is permitted.

## Make reviewable contributions

- Work on a narrowly scoped change; associate it with an issue when
  appropriate, and follow the branch and commit conventions in the
  contribution guidelines and `CLAUDE.md`.
- Follow the existing coding patterns, add appropriate tests, and run the
  relevant checks, including `pre-commit`, before requesting review. Report
  any checks that could not be run instead of claiming they passed.
- Respect the repository's existing frontend stacks and testing conventions;
  do not invent new patterns that conflict with its development guides.
- Use `.github/PULL_REQUEST_TEMPLATE.md`, and open new pull requests as
  drafts as required by `CLAUDE.md`. Explain the change, tests performed,
  and the specific AI model used. Leave human-review attestation to the
  actual contributor.
- Do not force-push after code review begins; preserve review context and
  make subsequent changes in new commits.

## Escalate mistakes

If AI-assisted work introduces an error into published code,
communications, or contractual commitments, notify the responsible human
immediately so the incident can be reported to the FLP contact or
[report@free.law](mailto:report@free.law). Include the AI tool and its
purpose, the error, the affected work or data, and any corrective actions
already taken.

If these instructions appear inconsistent with current FLP policy or
maintainer direction, stop and seek clarification rather than silently
choosing a weaker rule.
