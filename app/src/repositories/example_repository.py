# ===========================================================================================
# ExampleRepository
# Dev: anh.vu
# ===========================================================================================

"""
    Class này triển khai các phương thức phục vụ cho việc truy vấn dữ liệu trong bảng example
"""

# ===========================================================================================

from app.src.repositories.abstract_repository import AbstractRepository

# ===========================================================================================

# Main class ================================================================================
class ExampleRepository(AbstractRepository):
    def __init__(self) -> None:
        """"""

    
    def get_list(self):
        """
            Lấy ra danh sách các example
        """
        print("get list example")

    
    