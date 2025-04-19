import uvicorn


def run():
    uvicorn.run(
        app="first_glance.app:app",
        host="127.0.0.1",
        port=8000,
        reload=(True),
        app_dir="src",
    )


if __name__ == "__main__":
    run()
