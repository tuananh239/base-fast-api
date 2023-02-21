# ===========================================================================================
# AbstractRepository
# Dev: anh.vu
# ===========================================================================================

"""
    * Class này được sử dụng để định nghĩa các phương thức(method) cho các repository có cùng
    các phương thức giống nhau. Ví dụ:
        - Phương thức lấy ra danh sách đối tượng trong Database
        - Phương thức thêm đối tượng vào trong Database
    ...
    * Cách sử dụng:
        - Chỉ khai báo các phương thức
        - Không triển khai(implement) code trong phương thức
        - Những class kế thừa AbstractRepository phải implement các phương thức đã được khai
        báo.
"""

# ===========================================================================================

from abc import ABC, abstractclassmethod, abstractmethod

# Main class ================================================================================
class AbstractRepository(ABC):

    @abstractmethod
    def get_list(self, *args, **kwargs):
        """
            Lấy ra danh sách các đối tượng
        """
        raise NotImplementedError


    def get_detail(self, *args, **kwargs):
        """
            Lấy thông tin chi tiết của đối tượng
        """
        raise NotImplementedError

    
    def create(self, *args, **kwargs):
        """
            Thêm mới đối tượng
        """
        raise NotImplementedError

    
    def update(self, *args, **kwargs):
        """
            Cập nhật thông tin đối tượng
        """
        raise NotImplementedError


    def remove(self, *args, **kwargs):
        """
            Xóa đối tượng
        """
        raise NotImplementedError


