from highrise import BaseBot

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        await self.highrise.chat("✅ Бот запущен!")

    async def on_chat(self, user, message: str) -> None:
        if message == "/hello":
            await self.highrise.chat(f"Привет, {user.username}!")

    async def on_user_join(self, user) -> None:
        await self.highrise.chat(f"👋 Добро пожаловать, {user.username}!")

    async def on_user_leave(self, user) -> None:
        await self.highrise.chat(f"👋 Пока, {user.username}!")
