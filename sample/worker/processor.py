import time
from contextlib import contextmanager

from simple_worker import TaskExecutor

from sample import create_app
from sample.worker import simple_worker_app, init_worker
from sample.utils.log import LOG

flask_app = create_app()


class FlaskContextTaskExecutor(TaskExecutor):
    @contextmanager
    def context(self):
        with flask_app.app_context():
            yield


if __name__ == "__main__":
    # Working around IAM's eventually consistent nature. See
    # https://github.com/Shuttl-Tech/monorepo/issues/4084 for details
    LOG.info("worker.iam_wait")
    time.sleep(10)

    init_worker()
    LOG.info("worker.start")
    worker = simple_worker_app.worker(task_executor_cls=FlaskContextTaskExecutor)
    worker.start()
