from os import getenv
import datadog
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from sample.store import configure_db_with_app
from sample.utils.config import Config
from sample.utils.consul_patch import requests_use_srv_records

# local imports
from sample.utils.flask import APIFlask
from sample.utils.log import LOG
from sample.worker import init_worker
from ddtrace import config as dd_config
from ddtrace import patch as ddtrace_patch


def create_app() -> APIFlask:
    _configure_datadog_filters()
    dd_config.flask["distributed_tracing_enabled"] = True
    dd_config.requests["distributed_tracing"] = True
    ddtrace_patch(requests=True, flask=True)

    LOG.debug("sample.start")
    app = APIFlask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    datadog.initialize(statsd_host=getenv("NET_BRIDGE_GW_IP"))
    sentry_sdk_initialize()

    # NOTE: Order matters here
    configure_db_with_app(app)
    _register_all_blueprints(app)

    requests_use_srv_records()

    init_worker()

    return app


def _register_all_blueprints(app: APIFlask):
    from sample.api.sample import blueprint

    app.register_blueprint(blueprint)


def sentry_sdk_initialize():
    # dsn = '{PROTOCOL}://{PUBLIC_KEY}@{HOST}/{PROJECT_ID}'
    sentry_sdk.init(dsn=Config.SENTRY_DSN, integrations=[FlaskIntegration()])


def _configure_datadog_filters():
    from ddtrace import tracer
    from ddtrace import filters

    trace_filter = [
        filters.FilterRequestsOnUrl([r".*/health"])
    ]  # A list of regex's that match the traces we need to filter
    tracer.configure(settings={"FILTERS": trace_filter})
