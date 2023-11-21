from apps.shared_kernel.exception import BaseMsgException

class TodoContentException(BaseMsgException):
    message = "Content is required."