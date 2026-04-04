import asyncio
from highrise import BaseBot
from highrise.models import SessionMetadata, Position

TOKEN = "d819ee0c359cc3c7f512bb0abff0e155edda0e285a599ac0e548a397c65fab56"
ROOM_ID = "69ced5ed0c7c2e72825ba9eb"

EMOTES = {
    "dance": "emote-dance-casual",
    "wave": "emote-wave",
    "sit": "emote-sit",
    "happy": "emote-happy",
    "sad": "emote-sad",
    "angry": "emote-angry",
    "clap": "emote-clap",
    "boxer": "emote-boxer",
    "rest": "emote-rest"
}

class AnimationBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.chat("🎭 Бот с анимациями запущен!")
        await self.highrise.chat("Команды: !dance, !wave, !sit, !happy, !boxer, !help")
        print("✅ Бот запущен!")

    async def on_chat(self, user, message: str) -> None:
        msg = message.lower().strip()
        username = user.username

        if msg == "!help":
            await self.highrise.chat("📜 Команды: !dance, !wave, !sit, !happy, !sad, !angry, !clap, !boxer, !rest")

        elif msg == "!dance":
            await self.highrise.send_emote(EMOTES["dance"], user.id)
            await self.highrise.chat(f"💃 {username} танцует!")

        elif msg == "!wave":
            await self.highrise.send_emote(EMOTES["wave"], user.id)
            await self.highrise.chat(f"👋 {username} машет!")

        elif msg == "!sit":
            await self.highrise.send_emote(EMOTES["sit"], user.id)
            await self.highrise.chat(f"🪑 {username} сел(а)")

        elif msg == "!happy":
            await self.highrise.send_emote(EMOTES["happy"], user.id)
            await self.highrise.chat(f"😊 {username} счастлив(а)!")

        elif msg == "!sad":
            await self.highrise.send_emote(EMOTES["sad"], user.id)
            await self.highrise.chat(f"😢 {username} грустит")

        elif msg == "!angry":
            await self.highrise.send_emote(EMOTES["angry"], user.id)
            await self.highrise.chat(f"😠 {username} злится!")

        elif msg == "!clap":
            await self.highrise.send_emote(EMOTES["clap"], user.id)
            await self.highrise.chat(f"👏 {username} аплодирует!")

        elif msg == "!boxer":
            await self.highrise.send_emote(EMOTES["boxer"], user.id)
            await self.highrise.chat(f"🥊 {username} в боевой стойке!")

        elif msg == "!rest":
            await self.highrise.send_emote(EMOTES["rest"], user.id)
            await self.highrise.chat(f"😴 {username} отдыхает")

        elif msg == "/hello":
            await self.highrise.send_emote(EMOTES["wave"], user.id)
            await self.highrise.chat(f"Привет, {username}! 👋")

    async def on_user_join(self, user) -> None:
        await self.highrise.chat(f"✨ Добро пожаловать, {user.username}! ✨")

    async def on_user_leave(self, user) -> None:
        await self.highrise.chat(f"👋 Пока, {user.username}!")

async def main():
    bot = AnimationBot()
    await bot.run(TOKEN, ROOM_ID)

if __name__ == "__main__":
    asyncio.run(main())
