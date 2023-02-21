# ===========================================================================================
# ExampleRepository
# Dev: anh.vu
# ===========================================================================================

"""
    Class này triển khai các phương thức phục vụ cho việc truy vấn dữ liệu trong bảng example
"""

# ===========================================================================================

from app.libs.fastapi.app import app, add_router
from app.src.controllers.example_controller import example_controller

# ===========================================================================================

# Main class ================================================================================
app_controller = app

controllers = [
    example_controller
]

add_router(app, controllers)

# Implement =================================================================================

