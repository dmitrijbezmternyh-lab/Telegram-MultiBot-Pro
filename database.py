import aiosqlite
import structlog
from datetime import datetime

logger = structlog.get_logger()

class Database:
    def __init__(self, db_url: str):
        self.db_url = db_url.replace("sqlite+aiosqlite:///", "")
        
    async def init(self):
        self.db = await aiosqlite.connect(self.db_url)
        await self.db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_messages INTEGER DEFAULT 0,
                achievements TEXT DEFAULT '[]'
            )
        """)
        await self.db.commit()
        logger.info("Database initialized")
    
    async def get_user(self, user_id: int):
        cursor = await self.db.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        )
        return await cursor.fetchone()
    
    async def update_user_activity(self, user_id: int, username: str, 
                                   first_name: str, last_name: str):
        await self.db.execute("""
            INSERT INTO users (user_id, username, first_name, last_name, total_messages)
            VALUES (?, ?, ?, ?, 1)
            ON CONFLICT(user_id) DO UPDATE SET
                username = excluded.username,
                first_name = excluded.first_name,
                last_name = excluded.last_name,
                last_active = CURRENT_TIMESTAMP,
                total_messages = total_messages + 1
        """, (user_id, username, first_name, last_name))
        await self.db.commit()
