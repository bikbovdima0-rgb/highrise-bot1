from highrise import BaseBot

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        await self.highrise.chat("✅ Бот запущен!")

    async def on_chat(self, user, message: str) -> None:
        if message == "/hello":
            await self.highrise.chat(f"Привет, {user.username}!")
