import sys
from typing import Callable

from simple_worker import App
from sample.utils.config import Config


simple_worker_app = App(
    queue_prefix=Config.SQS_QUEUE_PREFIX,
    sqs_endpoint_url=Config.SQS_ENDPOINT_URL,
    sqs_region=Config.SQS_REGION,
    # use in memory queue in test environment
    # Pytest runner will always load the pytest module,
    # making it available in sys.modules
    testing_mode="pytest" in sys.modules,
)


def register_task_handler(*args, **kwargs) -> Callable:
    """
    Proxy to simple_worker.App.register_task_handler

    Usage:

    ```
    @register_task_handler('task_1'):
    def task_1():
        pass
    ```

    View simple_worker's docs for details.
    """
    return simple_worker_app.register_task_handler(*args, **kwargs)


# Proxies to the simple_worker_app
def add_task(*args, **kwargs):
    """
    Proxy to simple_worker.App.add_task

    Usage:

    ```
    add_task('task_1', param1='a')
    ```

    View simple_worker's docs for details.
    """
    simple_worker_app.add_task(*args, **kwargs)


def init_worker():
    import sample.worker.jobs  # noqa
