---
name: feature-development-with-tests-and-docs
description: Workflow command scaffold for feature-development-with-tests-and-docs in quantum_telegard.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /feature-development-with-tests-and-docs

Use this workflow when working on **feature-development-with-tests-and-docs** in `quantum_telegard`.

## Goal

Implements a new core feature or entity, updates configuration, adds tests, and documents the change.

## Common Files

- `bbs_systems/*.py`
- `core/*.py`
- `config/lexeme_registry.json`
- `docs/*.md`
- `README.md`
- `tests/*.py`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update implementation files in bbs_systems/ and/or core/
- Update configuration files such as config/lexeme_registry.json
- Update or add documentation in docs/
- Update README.md
- Add or update corresponding tests in tests/

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.