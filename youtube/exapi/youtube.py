from datetime import timedelta, timezone
from http import HTTPStatus
from typing import List

import requests
from shuttlis.serialization import serialize
from shuttlis.time import time_now

from youtube import Config
from youtube.domain.models.video import Video

BATCH_SIZE = 50


def published_before_ten_min() -> str:
    past_ten_min = time_now() + timedelta(minutes=-10)
    time_stamp = str(past_ten_min.replace(tzinfo=timezone.utc)).split(" ")
    return f"{time_stamp[0]}T{time_stamp[1][:-6]}Z"


class YoutubeService:
    def __init__(self, url):
        self._url = url

    def search_videos_by_query(
        self, query: str, batch_size: int = BATCH_SIZE
    ) -> List[Video]:
        params = {
            "part": "snippet",
            "maxResults": batch_size,
            "q": query,
            "publishedAfter": published_before_ten_min(),
            "key": Config.API_KEY,
        }
        response = requests.get(
            f"{self._url}/youtube/v3/search", params=serialize(params)
        )

        if HTTPStatus.OK == response.status_code:
            return [
                Video.from_dict(dikt=video)
                for video in response.json()["items"]
                if video["id"].get("videoId")
            ]
        else:
            raise RuntimeError("Youtube Service Error, Unable to fetch zones")


def get_youtube_service():
    return YoutubeService(url=Config.YOUTUBE_URL)
