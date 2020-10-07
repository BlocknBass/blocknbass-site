from flask import (
    Blueprint, render_template
)


bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("main/home.html", title="Home")

@bp.route("/about")
def about():
    return render_template("main/about.html", title="About")

@bp.route("/installation")
def install():
    return render_template("main/installation.html", title="Installation")

