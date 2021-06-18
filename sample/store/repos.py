from typing import List, Optional
from sample.store import db

from sample.domain.models import User
from sample.store.models.user import UserModel


class UserRepo:
    def create(self, user: User) -> User:
        user_model = UserModel(id=user.id, name=user.name)
        db.session.add(user_model)
        db.session.commit()

        return self.get(user.id)

    def get(self, user_id: str) -> Optional[User]:
        user_model = db.session.query(UserModel).get(user_id)
        if not user_model:
            return None

        return User(id=user_model.id, name=user_model.name)

    def get_all(self) -> List[User]:
        user_models = db.session.query(UserModel).all()
        return [
            User(id=user_model.id, name=user_model.name) for user_model in user_models
        ]
