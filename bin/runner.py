import uvicorn
from first_glance.core import settings
import os


def run():
    # Determine the host and port based on the environment
    host = "127.0.0.1" if settings.environment == "development" else "0.0.0.0"
    port = int(
        os.getenv("PORT", 8000)
    )  # Use the dynamic port provided by Railway or fallback to 8000

    # Set reload to True only in development, and set app_dir for dev
    reload = True if settings.environment == "development" else False
    app_dir = "src" if settings.environment == "development" else None

    # Run the application using uvicorn
    uvicorn.run(
        "first_glance.app:app",  # The app to run (import path)
        host=host,
        port=port,
        reload=reload,
        app_dir=app_dir,
    )


if __name__ == "__main__":
    run()
