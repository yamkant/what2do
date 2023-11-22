from apps.shared_kernel.exception import BaseMsgException

class InvalidTokenException(BaseMsgException):
    message = "Invalid token."