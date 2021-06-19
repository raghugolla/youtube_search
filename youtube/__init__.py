from os import getenv

import datadog
from ddtrace import config as dd_config
from ddtrace import patch as ddtrace_patch

from youtube.store import configure_db_with_app
from youtube.utils.config import Config
from youtube.utils.consul_patch import requests_use_srv_records

# local imports
from youtube.utils.flask import APIFlask
from youtube.utils.log import LOG


def create_app() -> APIFlask:
    _configure_datadog_filters()
    dd_config.flask["distributed_tracing_enabled"] = True
    dd_config.requests["distributed_tracing"] = True
    ddtrace_patch(requests=True, flask=True)

    LOG.debug("youtube.start")
    app = APIFlask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    datadog.initialize(statsd_host=getenv("NET_BRIDGE_GW_IP"))

    # NOTE: Order matters here
    configure_db_with_app(app)
    _register_all_blueprints(app)

    requests_use_srv_records()

    return app


def _register_all_blueprints(app: APIFlask):
    from youtube.api import search

    app.register_blueprint(search.blueprint)


def _configure_datadog_filters():
    from ddtrace import tracer
    from ddtrace import filters

    trace_filter = [
        filters.FilterRequestsOnUrl([r".*/health"])
    ]  # A list of regex's that match the traces we need to filter
    tracer.configure(settings={"FILTERS": trace_filter})
