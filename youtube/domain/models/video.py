from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict


@dataclass
class Video:
    id: str
    title: str
    description: str
    channel_id: str
    channel_title: str
    thumbnails: Dict
    published_at: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, dikt: Dict) -> "Video":
        return cls(
            id=dikt["id"]["videoId"],
            title=dikt["snippet"]["title"],
            description=dikt["snippet"]["description"],
            thumbnails=dikt["snippet"]["thumbnails"],
            published_at=dikt["snippet"]["publishedAt"],
            channel_id=dikt["snippet"]["channelId"],
            channel_title=dikt["snippet"]["channelTitle"],
        )
