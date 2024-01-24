import secrets

SECURITY_KEY = secrets.token_urlsafe(32)
print(SECURITY_KEY)
