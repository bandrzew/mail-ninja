---
description: Enforce running quality checks immediately after code edits to
  maintain reliability.
alwaysApply: true
---

Run linter and unit tests after every source code or test code modification to ensure code quality and correctness. `autopep8 --in-place --recursive src tests && pytest`