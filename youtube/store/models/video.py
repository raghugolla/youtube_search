from sqlalchemy.dialects.postgresql import JSONB

from youtube.store import db
from youtube.store.models.base import EntityBase


class VideoModel(EntityBase):
    __tablename__ = "video"

    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    thumbnails = db.Column(JSONB)
    published_at = db.Column(db.DateTime)
    channel_id = db.Column(db.String(255))
    channel_title = db.Column(db.String(255))
