from youtube import create_app

app = create_app()

if __name__ == "__main__":
    from os import getenv

    is_debug = getenv("DEBUG") in ["true", "True", "1", "yes"]
    app.run(host=getenv("BIND_HOST"), port=getenv("BIND_PORT"), debug=is_debug)
