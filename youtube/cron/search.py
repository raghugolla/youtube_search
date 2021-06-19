import time

from youtube import create_app
from youtube.domain.services.video_service import get_video_service
from youtube.utils.log import LOG

flask_app = create_app()

QUERY = "music"

if __name__ == "__main__":
    LOG.info("cron.iam_wait")

    time.sleep(20)

    LOG.info("cron.get.videos.from.youtube.get.start")

    get_video_service().sync_videos_by_query(query=QUERY)

    LOG.info("cron.get.videos.from.youtube.get.start")
