import uvicorn
from first_glance.core import settings
from first_glance.app import app as first_glance_app


def run():
    # Set the app based on the environment
    if settings.environment == "development":
        app = (
            "first_glance.app:app"  # String reference for dev to enable live-reloading
        )
        reload = True
        app_dir = "src"  # For development, file watching is needed in 'src'
        host = "127.0.0.1"  # Dev environment should use localhost
    else:
        app = first_glance_app  # Direct reference to the app instance for production
        reload = False
        app_dir = None  # No need for app_dir in production
        host = "0.0.0.0"  # Production should be accessible on all interfaces

    # Run the app with uvicorn
    uvicorn.run(
        app=app,
        host=host,
        port=settings.port,
        reload=reload,  # Only enabled in development
        app_dir=app_dir,  # Only set in development
    )


if __name__ == "__main__":
    run()
