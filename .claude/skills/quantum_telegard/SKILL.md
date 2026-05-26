```markdown
# quantum_telegard Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill introduces the core development patterns and workflows used in the `quantum_telegard` Python codebase. You'll learn about the repository's coding conventions, commit styles, and the step-by-step processes for adding new features, maintaining code quality, and managing tests and documentation. This guide is ideal for contributors seeking to align with established practices and streamline their workflow.

## Coding Conventions

- **File Naming:**  
  Use `snake_case` for all Python files.
  ```
  # Good
  user_manager.py

  # Bad
  UserManager.py
  ```

- **Import Style:**  
  Prefer relative imports within the package.
  ```python
  # Good
  from .utils import parse_message

  # Bad
  import utils
  ```

- **Export Style:**  
  Use named exports (explicitly define what is exported).
  ```python
  # In core/bbs_manager.py
  __all__ = ['BBSManager', 'BBSConfig']
  ```

- **Commit Messages:**  
  Follow [Conventional Commits](https://www.conventionalcommits.org/) with prefixes: `feat`, `chore`, `fix`.
  ```
  feat: add support for new BBS system
  fix: correct message parsing bug
  chore: update lexeme registry config
  ```

## Workflows

### Feature Development with Tests and Docs
**Trigger:** When adding a new BBS system or core functionality  
**Command:** `/new-bbs-system`

1. **Implement the Feature:**  
   Create or update implementation files in `bbs_systems/` and/or `core/`.
   ```python
   # bbs_systems/new_bbs.py
   class NewBBS:
       pass
   ```
2. **Update Configuration:**  
   Modify `config/lexeme_registry.json` as needed.
   ```json
   {
     "new_bbs": {
       "enabled": true
     }
   }
   ```
3. **Document the Change:**  
   Add or update documentation in `docs/` and update `README.md` to reflect new features.
4. **Write or Update Tests:**  
   Add or update corresponding tests in `tests/`.
   ```python
   # tests/test_new_bbs.py
   def test_new_bbs_initialization():
       assert NewBBS() is not None
   ```
5. **Commit Changes:**  
   Use a conventional commit message, e.g.,  
   `feat: add NewBBS system with docs and tests`

### Pycache Cleanup
**Trigger:** When you need to remove Python bytecode cache files and prevent them from being tracked  
**Command:** `/purge-pycache`

1. **Remove Tracked Pycache Files:**  
   Delete all `__pycache__/*.pyc` files from the repository.
   ```bash
   find . -name "*.pyc" -delete
   ```
2. **Update .gitignore:**  
   Ensure `.gitignore` includes patterns to ignore `__pycache__` and `.pyc` files.
   ```
   __pycache__/
   *.pyc
   ```
3. **Commit the Cleanup:**  
   Use a conventional commit message, e.g.,  
   `chore: purge pycache and update .gitignore`

## Testing Patterns

- **Test Files:**  
  Test files are typically placed in the `tests/` directory and named using `snake_case`, matching the module under test.
  ```
  tests/test_bbs_manager.py
  ```
- **Framework:**  
  The specific testing framework is not detected; use standard Python testing tools like `unittest` or `pytest`.
- **Test Example:**
  ```python
  def test_bbs_manager_init():
      manager = BBSManager()
      assert manager is not None
  ```

## Commands

| Command           | Purpose                                                        |
|-------------------|----------------------------------------------------------------|
| /new-bbs-system   | Start the workflow to add a new BBS system or core feature     |
| /purge-pycache    | Clean up Python bytecode files and update .gitignore           |
```
