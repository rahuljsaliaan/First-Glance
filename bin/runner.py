import uvicorn
from first_glance.core import settings


def run():
    # Set the app based on the environment
    if settings.environment == "development":
        reload = True
        app_dir = "src"
        host = "127.0.0.1"
    else:
        reload = False
        app_dir = None
        host = "0.0.0.0"

    # Run the app with uvicorn
    uvicorn.run(
        app="first_glance.app:app",
        host=host,
        port=settings.port,
        reload=reload,
        app_dir=app_dir,
    )


if __name__ == "__main__":
    run()
