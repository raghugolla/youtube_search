from flask import Blueprint

from youtube_search.utils.flask import APIResponse

blueprint = Blueprint("finance_payments", __name__)


@blueprint.route("/")
def hello():
    return APIResponse("Finance Payments Panel Backend")
