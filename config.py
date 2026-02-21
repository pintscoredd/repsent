import os
from dataclasses import dataclass

@dataclass
class Config:
    FRED_API_KEY: str = os.environ.get("FRED_API_KEY", "")
    NEWS_API_KEY: str = os.environ.get("NEWS_API_KEY", "")

config = Config()
