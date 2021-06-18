from uuid import uuid4

from sample.worker import register_task_handler

from sample.store.repos import UserRepo
from sample.domain.models import User


@register_task_handler("create_random_users")
def create_random_users(n_users: int):
    for i in range(n_users):
        user = User(id=uuid4(), name="hey")
        UserRepo().create(user)
