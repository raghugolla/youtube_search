from youtube.exapi.youtube import get_youtube_service, YoutubeService
from youtube.store.repo.video import VideoRepo, get_video_repo


class VideoService:
    def __init__(self, youtube_service: YoutubeService, video_repo: VideoRepo):
        self._youtube_service = youtube_service
        self._video_repo = video_repo

    def sync_videos_by_query(self, query: str):
        videos = self._youtube_service.search_videos_by_query(query=query)
        self._video_repo.upsert_multi(videos=videos)


def get_video_service() -> VideoService:
    return VideoService(
        youtube_service=get_youtube_service(), video_repo=get_video_repo()
    )
