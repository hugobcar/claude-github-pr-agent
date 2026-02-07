# Claude Code Review Guidelines

This document defines the coding standards and best practices for this project. Claude should use these guidelines when reviewing pull requests.

## Python Code Standards

### Code Style

- Follow PEP 8 style guidelines
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black formatter default)
- Use meaningful variable and function names in `snake_case`
- Use `PascalCase` for class names
- Use `UPPER_SNAKE_CASE` for constants

### Type Hints

- All functions must include type hints for parameters and return values
- Use `typing` module types when needed (Optional, Union, List, Dict, etc.)
- Use modern type hint syntax (e.g., `list[int]` instead of `List[int]` for Python 3.9+)
- Document complex types with type aliases when appropriate

### Documentation

- All public functions and classes must have docstrings
- Use Google-style or NumPy-style docstrings consistently
- Include parameter descriptions for complex functions
- Document exceptions that may be raised

### Error Handling

- Use specific exception types instead of bare `except` clauses
- Raise custom exceptions with descriptive messages
- Validate input at function boundaries
- Handle errors gracefully with appropriate logging

### Security Best Practices

- Never store passwords in plain text; use secure hashing (bcrypt, argon2)
- Validate and sanitize all user inputs
- Avoid SQL injection by using parameterized queries
- Never expose sensitive information in error messages or logs
- Use environment variables for secrets and configuration
- Avoid `eval()`, `exec()`, and similar functions with user input

### Testing

- All new code should have corresponding unit tests
- Maintain test coverage above 80%
- Use descriptive test names that explain the scenario
- Test edge cases and error conditions
- Use fixtures and mocks appropriately

### Code Organization

- One class per file when classes are substantial
- Group related functions in modules
- Use `__init__.py` to define public APIs
- Keep functions focused and under 50 lines when possible
- Avoid deep nesting (max 3-4 levels)

### Dependencies

- Pin dependency versions in requirements files
- Document why each dependency is needed
- Prefer standard library solutions when reasonable
- Keep dependencies up to date for security patches

### Git Commit Guidelines

- Write clear, concise commit messages
- Use imperative mood ("Add feature" not "Added feature")
- Reference issue numbers when applicable
- Keep commits atomic and focused

## Bugsnag Workflow Guidelines

When handling Bugsnag issues via the `claude-bugsnag.yml` workflow, follow these guidelines for creating branches and pull requests:

### Branch Naming

- Branch name format: `bugfix/issue-<issue_number>`
- Always branch from `main`

### PR Creation

- **Target branch**: Always use `--base main` to target the main branch
- **Title format**: `fix(bugsnag-<issue_number>): <short description of the fix>`
  - Example: `fix(bugsnag-42): handle null pointer in user authentication`
- **Reviewers**: Read the `REVIEWERS` environment variable (comma-separated) and add each as a `--reviewer` flag
  - Example: `gh pr create --base main --reviewer user1 --reviewer user2`
- **PR body must include**:
  - A clear description of what caused the bug (root cause analysis)
  - An explanation of the fix and how it resolves the issue
  - A reference to the originating issue using `Fixes #<issue_number>`

### Bug Fix Process

1. Analyze the stack trace and error details from the Bugsnag issue
2. Locate the relevant source files and understand the root cause
3. Implement a fix following the code standards defined in this document
4. Commit with a clear message referencing the issue number
5. Open a PR following the conventions above
6. Comment on the original issue summarizing findings and linking to the PR

### Fix Quality Standards

- Fixes must address the root cause, not just suppress the error
- Include appropriate error handling around the fix
- Ensure the fix does not introduce regressions
- Follow all code style, type hint, and documentation standards from this document

## Review Checklist

When reviewing code, verify:

1. **Functionality**: Code works as intended and handles edge cases
2. **Security**: No vulnerabilities introduced (injection, exposure, etc.)
3. **Performance**: No obvious performance issues or N+1 queries
4. **Readability**: Code is clear and maintainable
5. **Testing**: Adequate test coverage for new functionality
6. **Documentation**: Public APIs are documented
7. **Error Handling**: Failures are handled gracefully
8. **Type Safety**: Type hints are present and correct
