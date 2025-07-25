"""
Custom exceptions for Site24x7 CLI
"""

class Site24x7CLIError(Exception):
    """Base exception for Site24x7 CLI"""
    pass

class AuthenticationError(Site24x7CLIError):
    """Authentication related errors"""
    pass

class APIError(Site24x7CLIError):
    """API request errors"""
    pass

class ValidationError(Site24x7CLIError):
    """Input validation errors"""
    pass
