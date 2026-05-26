# Lexeme Dial-Up System

The lexeme dial-up system routes text lexemes (like `primal`) to BBS modules.

## Registry

Registry file: `config/lexeme_registry.json`

Each lexeme contains:
- `full_name`
- `endpoint`
- `description`
- `dial_number` (future production mapping)
- `status`
- `aliases`

## Behavior

- Lookup is case-insensitive.
- Alias lookup is supported (`primal_bbs`, `primalBBS`, etc.).
- Missing lexeme attempts are logged as failed sessions.
- Session logs are JSON-lines records in `logs/sessions.log`.

## Runtime Flow

1. Terminal accepts a lexeme.
2. Dialer renders a dial-up sequence.
3. Connection manager resolves lexeme to endpoint.
4. BBS module runs.
5. Session summary is logged.
