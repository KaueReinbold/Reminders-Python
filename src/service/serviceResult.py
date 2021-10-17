class ServiceResult:
    def __init__(
        self,
        is_valid,
        message,
        result=None
    ) -> None:
        self.is_valid = is_valid
        self.message = message
        self.result = result
