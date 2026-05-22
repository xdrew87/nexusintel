# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in NexusIntel, please **do not** create a public GitHub issue. Instead:

1. Email security concerns to: xdrew87@osintintelligence.xyz (with "[NexusIntel Security]" in subject)
2. Describe the vulnerability in detail
3. Include steps to reproduce if applicable
4. Allow 7 days for initial response

We take security seriously and will work with you to address the issue promptly.

## Security Best Practices

### For Users

- Never commit .env files with API keys
- Use strong, unique API key credentials
- Validate all user input on the backend
- Use HTTPS in production
- Keep dependencies updated: `pip install -U -r requirements.txt`
- Run with DEBUG=false in production
- Implement rate limiting
- Use environment variables for all secrets

### For Contributors

- Never hardcode secrets or credentials
- Sanitize user input before database queries
- Validate file uploads (type, size, content)
- Use prepared statements to prevent SQL injection
- Implement proper authentication/authorization
- Keep dependencies minimal and up-to-date
- Run security linters: `bandit`, `safety`
- Test edge cases and error conditions

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ Yes    |
| < 1.0   | ❌ No     |

## Security Headers

NexusIntel backend includes:
- `Content-Security-Policy`
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection`

## Dependency Management

We regularly audit dependencies for vulnerabilities:

```bash
# Check for known vulnerabilities
pip install safety
safety check

# Update packages
pip install -U -r requirements.txt
npm audit fix
```

## API Security

- All API endpoints validate input via Pydantic
- File uploads are restricted by type and size
- Paths are sanitized to prevent traversal
- Rate limiting is enforced
- Async workers prevent blocking attacks

## Questions?

For security questions, open a discussion or email security concerns responsibly.
