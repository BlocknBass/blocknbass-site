import requests
from flask import (
    Blueprint, redirect, json
)


bp = Blueprint("discord", __name__, url_prefix="/discord")
widget_api = "https://discord.com/api/guilds/699622492750217217/widget.json"


@bp.route("/")
def index():
    data = json.loads(requests.get(widget_api).content)

    return redirect(data["instant_invite"], code=302)
