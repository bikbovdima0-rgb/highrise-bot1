import asyncio
from highrise import BaseBot
from highrise.models import SessionMetadata

TOKEN = "d819ee0c359cc3c7f512bb0abff0e155edda0e285a599ac0e548a397c65fab56"
ROOM_ID = "69ced5ed0c7c2e72825ba9eb"

class MyBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.chat("✅ Бот запущен!")

    async def on_chat(self, user, message: str) -> None:
        if message == "/hello":
            await self.highrise.chat(f"Привет, {user.username}!")

def main():
    bot = MyBot()
    bot.run(TOKEN, ROOM_ID)

if __name__ == "__main__":
    main()
