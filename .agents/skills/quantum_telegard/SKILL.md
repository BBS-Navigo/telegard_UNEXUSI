# quantum_telegard Development Patterns 🃏

> Auto-generated skill from repository analysis · 21st iteration marker

## Overview

This skill introduces the core development patterns and workflows used in the `quantum_telegard` Python codebase. Use it to stay aligned with the repository's Python naming, import, test, and workflow conventions.

## Coding Conventions

- **File Naming:**  
  Use `snake_case` for Python files.
  ```
  # Good
  user_manager.py

  # Bad
  UserManager.py
  ```

- **Import Style:**  
  Use explicit package imports for repository modules.
  ```python
  # Good
  from core.connection_manager import ConnectionManager
  from core.lexeme_manager import LexemeManager

  # Bad
  import connection_manager
  import lexeme_manager
  ```

- **Module Interface Style:**  
  Import concrete symbols directly from the module that defines them; there is no established repository-wide `__all__` pattern.
  ```python
  from bbs_systems.sysop_hub_bbs import run
  from utils.validators import normalize_lexeme
  ```

- **Commit Messages:**  
  Follow [Conventional Commits](https://www.conventionalcommits.org/) with prefixes such as `feat`, `chore`, and `fix`.
  ```
  feat: add support for new BBS system
  fix: correct message parsing bug
  chore: update lexeme registry config
  ```

## Workflows

### Feature Development with Tests and Docs
**Trigger:** When adding a new BBS system or core functionality  
**Command:** `/feature-development-with-tests-and-docs`

1. **Implement the Feature:**  
   Create or update implementation files in `bbs_systems/` and/or `core/`.
   ```python
   from core.connection_manager import ConnectionManager
   from core.lexeme_manager import LexemeManager
   ```
2. **Update Configuration:**  
   Modify `config/lexeme_registry.json` as needed.
3. **Document the Change:**  
   Add or update documentation in `docs/` and update `README.md` when behavior changes.
4. **Write or Update Tests:**  
   Add or update corresponding `unittest` coverage in `tests/test_*.py`.
   ```python
   class TestConnectionManager(unittest.TestCase):
       def test_connect_sysop_alias_success(self):
           ...
   ```
5. **Verify Changes:**  
   Run `python -m unittest discover -s tests`.
6. **Commit Changes:**  
   Use a conventional commit message such as `feat: add sysop routing coverage`.

### Pycache Cleanup
**Trigger:** When you need to remove Python bytecode cache files and prevent them from being tracked  
**Command:** `/pycache-cleanup`

1. **Remove Tracked Pycache Files:**  
   Delete tracked `__pycache__` directories and `.pyc` files from the repository.
   ```bash
   find . -name "__pycache__" -type d -prune -exec rm -rf {} +
   find . -name "*.pyc" -delete
   ```
2. **Update .gitignore:**  
   Ensure `.gitignore` includes patterns to ignore `__pycache__` and `.pyc` files.
   ```
   __pycache__/
   *.pyc
   ```
3. **Verify Cleanup:**  
   Run the most relevant tests after cleanup if tracked files changed.
4. **Commit the Cleanup:**  
   Use a conventional commit message such as `chore: purge pycache and update .gitignore`.

## Testing Patterns

- **Test Files:**  
  Test files live under `tests/` and follow the `test_*.py` naming pattern.
  ```
  tests/test_connection_manager.py
  tests/test_dialer.py
  ```
- **Framework:**  
  Use Python's built-in `unittest` framework.
- **Test Example:**
  ```python
  class TestDialer(unittest.TestCase):
      def test_autocomplete(self):
          self.assertIn("primal", self.dialer.autocomplete("pri"))
  ```

## Commands

| Command                                | Purpose                                                    |
|----------------------------------------|------------------------------------------------------------|
| /feature-development-with-tests-and-docs | Start the workflow to add a core feature with tests/docs |
| /pycache-cleanup                       | Clean up Python bytecode files and update `.gitignore`    |

## Next iteration seeds 🃏

- Add a repository-verified example that shows a `config/lexeme_registry.json` change paired with matching tests.
- Include the standard validation command (`python -m unittest discover -s tests`) in generated workflow metadata.
- Re-check generated bundle guidance against live Python files before publishing future iterations.
