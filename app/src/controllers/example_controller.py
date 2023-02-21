# ===========================================================================================
# AbstractRepository
# Dev: anh.vu
# ===========================================================================================

"""
    Định nghĩa và triển khai tất cả các API liên quan đến example
"""

# ===========================================================================================

from fastapi import APIRouter

from app.libs.fastapi.decorator import try_catch
from app.libs.fastapi.route import Controller

# ===========================================================================================

class ExampleUrl():
    """
        Định nghĩa các đường dẫn của các API của Example
    """
    GET_LIST = "/"
    POST = GET_LIST
    UPDATE = GET_LIST
    DELETE = GET_LIST

# Main ======================================================================================
EXAMPLE_URL = ExampleUrl()

# Tạo router cho example
example_router = APIRouter()

# Tạo đối tượng controller cho example
example_controller = Controller(
    router=example_router,
    prefix="/example",
    tags=["admin"]
)

# Implement API =============================================================================
@example_router.get(path=EXAMPLE_URL.GET_LIST)
@try_catch
async def get_list():
    """
        Thực hiện lấy và trả về danh sách của các Example 
    """
    raise Exception("false")
    # return {"name": "vta"}

