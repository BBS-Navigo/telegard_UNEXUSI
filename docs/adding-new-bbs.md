# Adding a New BBS Module

1. Create a module in `/home/runner/work/quantum_telegard/quantum_telegard/bbs_systems/`.
2. Expose a `run(session, input_func=input, output_func=print) -> dict` function.
3. Return a dictionary with at least:
   - `entry_state`
   - `rooms_visited`
   - `signal`
   - `exit`
4. Register the endpoint in `core/connection_manager.py`.
5. Add a lexeme record (and aliases) in `config/lexeme_registry.json`.
6. Add tests for routing and behavior.

## Suggested Session Return Structure

```python
{
  "entry_state": "shadow",
  "rooms_visited": ["Lobby", "Exit Port"],
  "signal": "brief summary",
  "exit": "disconnect"
}
```
