# ===========================================================================================
# Decorator Controller
# Dev: anh.vu
# ===========================================================================================

"""
    Các decorator phục vụ cho việc viết API. Các thành phần:
        - Try catch
"""

# ===========================================================================================

from fastapi import Request

# Main ======================================================================================

def try_catch(handler):
    async def wrapper(request: Request, *args, **kwargs):
        try:
            return await handler(request, *args, **kwargs)
        except Exception:
            return {"name": "error"}

    # Fix signature of wrapper
    import inspect
    wrapper.__signature__ = inspect.Signature(
        parameters = [
            # Use all parameters from handler
            *inspect.signature(handler).parameters.values(),

            # Skip *args and **kwargs from wrapper parameters:
            *filter(
                lambda p: p.kind not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD),
                inspect.signature(wrapper).parameters.values()
            )
        ],
        return_annotation = inspect.signature(handler).return_annotation,
    )
    wrapper.__name__ = handler.__name__

    return wrapper