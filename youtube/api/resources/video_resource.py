from typing import Dict

from shuttlis.serialization import serialize

from youtube.domain.models.video import Video


def video_resource(video: Video) -> Dict:
    return serialize(
        {
            "id": video.id,
            "title": video.title,
            "description": video.description,
            "published_at": video.published_at,
            "created_at": video.created_at,
        }
    )
