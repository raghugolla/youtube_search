from sqlalchemy import func

from youtube.store import db


class EntityBase(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
