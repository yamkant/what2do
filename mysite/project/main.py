import os
import uvicorn

from apps.shared_kernel.config import config

def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)
    uvicorn.run(
        app="apps.shared_kernel.server:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "production" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()