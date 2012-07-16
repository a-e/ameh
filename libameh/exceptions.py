"""Custom ameh exceptions
"""

class AmehError (RuntimeError):
    """Base class for all ameh exceptions.
    """
    pass

class UsageError (AmehError):
    """Incorrect command-line usage.
    """
    pass

class UnknownApplication (AmehError):
    """Application name is unknown or unconfigured.
    """
    pass

class MissingConfig (AmehError):
    """Configuration file is missing.
    """
    pass

class NoPermission (AmehError):
    """Current user is lacking permission for something.
    """
    pass

