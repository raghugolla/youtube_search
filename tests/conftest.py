import logging

import pytest
import ddtrace

from sample import create_app


@pytest.fixture
def app():
    app = create_app()
    app.testing = True

    from sample.store import db

    with app.app_context():
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
            db.session.commit()

        # By using a yield statement instead of return, all the code after the
        # yield statement serves as the teardown code:
        # https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code
        yield app


@pytest.fixture(autouse=True, scope="session")
def disable_dogstats_logger():
    # Datadog's logger tries to send messages in a separate thread,
    # and this messes with pytest's capturing mechanism
    ddtrace.tracer.enabled = False
    logging.getLogger("datadog.threadstats").propagate = False
    logging.getLogger("ddtrace._worker").propagate = False
    logging.getLogger("srv_hijacker").propagate = False
