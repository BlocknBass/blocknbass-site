from flask import (
    Blueprint
)


bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route("/")
def index():
    return """<h1>This feature is not ready yet...</h1> \
              <p>Check back at a later stage.<h1>"""