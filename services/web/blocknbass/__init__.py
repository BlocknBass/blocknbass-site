from base64 import b64encode as b64enc
from os import environ, makedirs, urandom

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY=b64enc(urandom(16)).decode("utf-8"))

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

    from . import (blog, main)

    app.register_blueprint(blog.bp)
    app.register_blueprint(main.bp)

    return app
