# quantum_telegard

A terminal-based lexeme dial-up BBS prototype.

## What it does

- Dials into BBS systems using lexemes (e.g. `primal`) instead of numbers.
- Resolves aliases and routes to endpoint modules.
- Logs every connection attempt/session in structured JSON-lines format.
- Ships with:
  - `primal` BBS
  - `house` (THE House of Confusion) BBS
  - `sysop` (SYSOP Hub) BBS
  - a template BBS module for extension

## Run

From the project root directory:

```bash
python main.py
```

## Commands

- `list` — show known lexemes
- `history` — show recent dialed lexemes
- `help` — show help
- `quit` — disconnect terminal
- `<lexeme>` — dial into a BBS

## Registry & Config

- Lexeme registry: `config/lexeme_registry.json`
- Dial-up config: `config/dialup_config.yaml`
- Session logs: `logs/sessions.log`

## Tests

```bash
python -m unittest discover -s tests
```
