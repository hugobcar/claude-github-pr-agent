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
