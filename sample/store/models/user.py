from sample.store import db
from sqlalchemy_uuidstr import UUIDType


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(UUIDType(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
