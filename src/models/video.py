from pydantic import BaseModel
from typing import Optional, List


class VideoRequest(BaseModel):
    video_url: str
    title: Optional[str] = None
    transcript: Optional[List] = None