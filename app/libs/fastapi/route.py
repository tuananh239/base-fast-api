# ===========================================================================================
# Fast API Route
# Dev: anh.vu
# ===========================================================================================

"""
    Cấu hình riêng cho fastapi app. Các thành phần:
"""

# ===========================================================================================

from fastapi import APIRouter

# Main ======================================================================================
router = APIRouter()

class Controller():
    def __init__(self, router, prefix, tags) -> None:
        self.router = router
        self.prefix = prefix
        self.tags = tags