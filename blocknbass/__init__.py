from os import environ, makedirs

from flask import Flask


def create_app(test_config=None):
    from dotenv import load_dotenv
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=environ["SECRET_KEY"]
    )


    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)


    try:
        makedirs(app.instance_path)
    except OSError:
        pass


    @app.route("/test")
    def test():
        # If this fails or doesn"t return "1 + 1 = 2"
        # The universe is collapsing. Please call Elon Musk and NASA.
        return f"1 + 1 = {1 + 1}"


    from . import (blog, discord, main)

    app.register_blueprint(blog.bp)
    app.register_blueprint(discord.bp)
    app.register_blueprint(main.bp)


    return app
