# ===========================================================================================
# Fast API App
# Dev: anh.vu
# ===========================================================================================

"""
    Cấu hình riêng cho fastapi app. Các thành phần:
"""

# ===========================================================================================

from fastapi import FastAPI

# Main ======================================================================================
app = FastAPI()

# Function help =============================================================================
def add_router(application, routers):
    """
        Thêm các route vào app
    """
    for router in routers:
        application.include_router(
            router=router.router,
            prefix=router.prefix,
            tags=router.tags
        )