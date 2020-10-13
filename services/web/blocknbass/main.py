import requests
from flask import (
    Blueprint, render_template, redirect, json
)


bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return "<h1>Hello, World!</h1>\n<p>This page is a work in progress...</p>"
    return render_template("main/home.html", title="Home")


@bp.route("/discord")
def discord():
    widget_api = "https://discord.com/api/guilds/699622492750217217/widget.json"
    data = json.loads(requests.get(widget_api).content)

    return redirect(data["instant_invite"], code=302)
