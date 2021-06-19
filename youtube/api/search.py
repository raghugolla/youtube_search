from flask import Blueprint
from shuttlis.serialization import serialize
from shuttlis.pagination import After, Cursor, Paginator
from shuttlis.serialization import serialize
from shuttlis.validators import pagination
from voluptuous import Schema, Required

from youtube.api.resources.video_resource import video_resource
from youtube.domain.services.video_service import get_video_service
from youtube.store.repo.video import get_video_repo
from youtube.utils.flask import APIResponse
from youtube.utils.schema import queryschema

blueprint = Blueprint("youtube", __name__, url_prefix="/api/v1/youtube")


class _After(After):
    @classmethod
    def from_data(cls, data):
        return cls(data.id, data.published_at)


@blueprint.route("/health")
def health() -> APIResponse:
    get_video_service().sync_videos_by_query(query="music")
    return APIResponse({"healthy": True})


@blueprint.route("/by_title", methods=["GET"])
@queryschema(Schema({Required("title"): str}).extend(pagination.schema))
def get_by_names(title: str, after=None, limit=None) -> APIResponse:
    cursor = Cursor.from_strings(after=after, limit=limit)
    videos = get_video_repo().get_by_title(title=title, cursor=cursor)
    cursor = Paginator.from_data(videos, page_size=len(videos), custom_cls=_After)
    return APIResponse(
        [serialize(video_resource(video)) for video in videos],
        meta={"cursor": cursor.as_dict()},
    )
