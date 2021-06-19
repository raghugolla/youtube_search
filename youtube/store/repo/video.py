from typing import List

from shuttlis.pagination import Cursor

from youtube.domain.models.video import Video
from youtube.store import db
from youtube.store.models.video import VideoModel
from youtube.store.repo.utils import process_search_string, paginated_results


class VideoRepo:
    def __init__(self):
        self._db = db

    def upsert_multi(self, videos: List[Video]):
        video_models = [self._to_store_model(video) for video in videos]
        for vm in video_models:
            self._db.session.merge(vm)
        self._db.session.commit()

    def get_by_title(self, title: str, cursor: Cursor) -> List[Video]:
        search_string = title.strip()
        if not search_string:
            return []

        query = self._db.session.query(VideoModel).filter(
            VideoModel.title.match(
                process_search_string(search_string), postgresql_regconfig="english"
            ),
        )
        if cursor:
            models = paginated_results(
                query=query,
                model=VideoModel,
                cursor=cursor,
                timestamp_attr=VideoModel.published_at,
            )
        else:
            models = query.order_by(VideoModel.published_at).all()

        return [self._to_domain_model(model) for model in models]

    def _to_store_model(self, video: Video) -> VideoModel:
        return VideoModel(
            id=video.id,
            title=video.title,
            description=video.description,
            thumbnails=video.thumbnails,
            published_at=video.published_at,
            channel_id=video.channel_id,
            channel_title=video.channel_id,
        )

    def _to_domain_model(self, video_model: VideoModel) -> Video:
        return Video(
            id=video_model.id,
            title=video_model.title,
            description=video_model.description,
            thumbnails=video_model.thumbnails,
            published_at=video_model.published_at,
            channel_id=video_model.channel_id,
            channel_title=video_model.channel_id,
        )


def get_video_repo():
    return VideoRepo()
