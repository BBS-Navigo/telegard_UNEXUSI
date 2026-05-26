---
name: pycache-cleanup
description: Workflow command scaffold for pycache-cleanup in quantum_telegard.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /pycache-cleanup

Use this workflow when working on **pycache-cleanup** in `quantum_telegard`.

## Goal

Removes Python bytecode cache files and updates .gitignore to prevent future tracking.

## Common Files

- `**/__pycache__/*.pyc`
- `.gitignore`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Remove all __pycache__/*.pyc files from tracked files
- Add or update .gitignore to include __pycache__ patterns

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.