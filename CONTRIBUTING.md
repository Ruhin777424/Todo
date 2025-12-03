# Contributing to Todo App

Thank you for considering contributing to this project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions with other contributors and maintainers.

## How to Contribute

### Reporting Bugs

Before submitting a bug report, please search the issue tracker to avoid duplicates.

When submitting a bug report, include:
- Clear, descriptive title
- Step-by-step reproduction instructions
- Expected behavior
- Actual behavior
- Python version and OS
- Relevant error messages or logs

### Suggesting Features

For feature suggestions:
- Use a clear, descriptive title
- Provide a detailed description of the feature
- Explain why this feature would be useful
- List examples of similar features in other applications (if applicable)

### Pull Requests

1. **Fork** the repository and create a new branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow PEP 8 style guidelines
   - Write clear commit messages
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests** before submitting:
   ```bash
   python manage.py test
   ```

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "Add/Fix: clear description of changes"
   git push origin feature/your-feature-name
   ```

5. **Submit a Pull Request**:
   - Use a clear, descriptive title
   - Reference related issues
   - Describe what changes were made and why
   - Ensure all tests pass

## Development Setup

1. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install black flake8 pytest pytest-django
   ```

2. Create a `.env.dev` file:
   ```bash
   cp .env.example .env.dev
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints where possible
- Write descriptive function/class docstrings
- Limit line length to 100 characters

### Format code with black:
```bash
black .
```

### Check code with flake8:
```bash
flake8 --max-line-length=100 --exclude=venv,migrations
```

## Testing

- Write tests for all new features
- Ensure existing tests still pass
- Aim for >80% code coverage

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test task

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

## Documentation

- Update `README.md` if adding new features
- Add docstrings to all functions and classes
- Include examples in comments where helpful
- Update `CHANGELOG.md` with significant changes

## Commit Messages

Follow these conventions:
- Use the imperative mood ("Add feature" not "Added feature")
- Limit first line to 50 characters
- Reference issues when applicable: "Fix #123"
- Keep commits atomic and logical

Examples:
```
Add dark mode toggle to settings
Fix: TaskSerializer not including status field
Update dependencies for security patch
Docs: improve README installation section
```

## Areas for Contribution

- **Bug fixes**: Check open issues labeled `bug`
- **Features**: Check issues labeled `enhancement`
- **Documentation**: Improve README, add examples, fix typos
- **Testing**: Increase test coverage
- **Performance**: Optimize queries and frontend
- **Accessibility**: Improve keyboard navigation, screen reader support
- **Translations**: Add new language support

## Review Process

1. Maintainers will review your PR within 2-7 days
2. Feedback will be provided if changes are needed
3. Once approved, your PR will be merged

## Questions?

Feel free to open an issue or reach out to the maintainers.

---

**Thank you for contributing! Your effort helps make this project better for everyone.** 🎉
