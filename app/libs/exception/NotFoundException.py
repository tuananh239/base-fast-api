# ===========================================================================================
# NotFoundException
# Dev: anh.vu
# ===========================================================================================

"""
    * Exception mô tả cho việc không tìm thấy kết quả. Các thành phần
"""

# Main class ================================================================================
class NotFoundException(Exception):
    def __init__(self, status_code:str = 404, message:str = "Not found!") -> None:
        super().__init__(message)
        self.status_code = status_code
        self.message = message