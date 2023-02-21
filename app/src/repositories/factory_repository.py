# ===========================================================================================
# FactoryRepository
# Dev: anh.vu
# ===========================================================================================

"""
    * Class này tạo ra một nơi tập trung các repository. Dễ dàng trong việc khởi tạo các
    repository và thay đổi repository(tránh việc sửa đổi code nhiều).
    * Cách sử dụng:
    - Khi cần thay đổi class khác cho một repository thì chỉ cần trả về class đó trong hàm
    get_repository của FactoryRepository chứ không cần thay đổi tại chỗ khác
    (tránh phát sinh lỗi).
"""

# ===========================================================================================

from enum import Enum

from app.libs.exception.NotFoundException import NotFoundException
from app.src.repositories.example_repository import ExampleRepository

# Elements ==================================================================================
"""
    Khai báo các element được sử dụng trong class
"""

class RepositoryName(Enum):
    """
        Định nghĩa tên các bảng trong Database
    """
    EXAMPLE_REPOSITORY = "example"


class RepositoryManager():
    def __init__(self, example) -> None:
        self.example = example

# Main class ================================================================================
class FactoryRepository():
    def __init__(self) -> None:
        """"""

    def get_repository(self, repository_name):
        """
            Hàm này thực hiện lấy ra object repository tương ứng với tên của repository đó.
            Đầu vào:
                - repository_name: Tên của repository
            Đầu ra:
                - Trả về object khởi tạo từ class của repository tương ứng
        """
        # Kiểm tra tên của repository và trả về kết quả tương ứng, nếu không tồn tại
        # repository đó thì trả về lỗi
        if repository_name == RepositoryName.EXAMPLE_REPOSITORY:
            return ExampleRepository()
        else:
            raise NotFoundException(message=f"{repository_name} repoistory is't existed!")

    
    def get_repository_manager(self):
        """
            Hàm này thực hiện lấy ra object chứa tất cả các repository
            Đầu vào: Không có
            Đầu ra:
                - Trả về object chứa tất cả các repository
        """
        _repository_manager = RepositoryManager(
            example=ExampleRepository()
        )

        return _repository_manager