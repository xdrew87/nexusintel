# Contributing to NexusIntel

Thank you for your interest in contributing! Here's how you can help.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/nexusintel.git`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Test thoroughly
6. Commit: `git commit -m "Add your feature"`
7. Push: `git push origin feature/your-feature`
8. Create a Pull Request

## Development Setup

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m uvicorn api.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Code Style

- **Python:** Follow PEP 8
- **JavaScript:** Use Prettier + ESLint
- **Commit messages:** Keep clear and concise

## Before Submitting

- ✅ Run tests
- ✅ Check code style
- ✅ Update documentation
- ✅ Ensure no hardcoded secrets
- ✅ Test locally with Docker

## PR Guidelines

1. Link related issues
2. Describe what and why
3. Include test cases if applicable
4. Keep commits clean and logical
5. Be open to feedback

## Areas We Need Help With

- 🔍 Enrichment modules (new data sources)
- 🎨 UI/UX improvements
- 📚 Documentation
- 🧪 Test coverage
- 🔗 Integration modules
- 🐛 Bug fixes

## Code Review Process

1. Automated checks run (linting, tests)
2. Manual review by maintainers
3. Feedback and iteration
4. Merge when approved

## Questions?

- Check GitHub Discussions
- Open an issue with the `question` label
- Email for security issues

Thank you for contributing! 🙌
