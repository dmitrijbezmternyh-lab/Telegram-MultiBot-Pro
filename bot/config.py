import os
from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    # Bot
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    
    # APIs
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENWEATHER_API_KEY: str = os.getenv("OPENWEATHER_API_KEY", "")
    
    # Admin
    ADMIN_IDS: List[int] = field(default_factory=lambda: 
        list(map(int, os.getenv("ADMIN_IDS", "").split(","))) if os.getenv("ADMIN_IDS") else []
    )
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///data/bot.db")
    
    # Limits
    RATE_LIMIT: float = float(os.getenv("RATE_LIMIT", "0.5"))  # seconds
    GPT_CONTEXT_LENGTH: int = int(os.getenv("GPT_CONTEXT_LENGTH", "15"))
    GPT_MAX_TOKENS: int = int(os.getenv("GPT_MAX_TOKENS", "500"))
    
    # Cache
    WEATHER_CACHE_TTL: int = 1800  # 30 minutes
    CURRENCY_CACHE_TTL: int = 3600  # 1 hour
    
    def validate(self):
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required!")
        return self

config = Config()
