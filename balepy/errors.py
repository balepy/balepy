
class APIError(Exception):
    error_code: int
    description: str

    def __init__(self, description: str, error_code: int):
        self.error_code = error_code
        self.description = description
        super().__init__(f"Error {self.error_code}: {self.description}")
