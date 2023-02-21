import sys
[sys.path.append(i) for i in ['.', '..']]

import uvicorn

if __name__ == "__main__":
    config = uvicorn.Config("src.applications.app:app_controller", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
