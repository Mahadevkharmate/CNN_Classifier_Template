# Custom Exception Class
import sys
import traceback

class CustomException(Exception):
    """
    Custom Exception class for the CNN Classifier Template project.
    Captures error message, optional errors, and traceback info.
    """
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
        self.message = message
        _, _, tb = sys.exc_info()
        self.traceback = "".join(traceback.format_tb(tb)) if tb else None

    def __str__(self):
        error_info = f"CustomException: {self.message}"
        if self.errors:
            error_info += f" | Errors: {self.errors}"
        if self.traceback:
            error_info += f"\nTraceback:\n{self.traceback}"
        return error_info
