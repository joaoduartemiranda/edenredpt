class EdenredAPIException(Exception):
    pass

class AuthenticationException(EdenredAPIException):
    "Raised when an authentication error is returned by Edenred API (Edenred uses HTTP 409)"
    pass

