import random
from highrise import BaseBot
from highrise.models import SessionMetadata, User, Position

# --- КОНФИГУРАЦИЯ ---
ROOM_ID = "69ced5ed0c7c2e72825ba9eb"
TOKEN = "d819ee0c359cc3c7f512bb0abff0e155edda0e285a599ac0e548a397c65fab56"
# --------------------

class MyBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("✅ Бот успешно запущен!")
        await self.highrise.chat("✨ Привет! Я бот с эмоциями!")
        await self.highrise.chat("📜 Команды: !emote [число], !help, !join")

    async def on_user_join(self, user: User, position: Position) -> None:
        await self.highrise.chat(f"🎉 Добро пожаловать, {user.username}! Напиши !help")

    async def on_chat(self, user: User, message: str) -> None:
        msg = message.lower().strip()
        username = user.username

        if user.id == self.highrise.user.id:
            return

        if msg == "!help":
            await self.highrise.chat("📜 Команды: !emote [число 1-200], !join")
            return

        if msg == "!join":
            await self.highrise.chat(f"🔄 Телепортирую {username}...")
            await self.highrise.teleport(user.id, Position(5, 1, 0, "FrontLeft"))
            return

        if msg.startswith("!emote"):
            parts = msg.split()
            if len(parts) > 1 and parts[1].isdigit():
                number = int(parts[1])
                if 1 <= number <= 200:
                    emotes = ["emote-dance-casual", "emote-wave", "emote-sit", "emote-happy"]
                    chosen = random.choice(emotes)
                    await self.highrise.send_emote(chosen, user.id)
                    await self.highrise.chat(f"🎭 {username} показал эмоцию (число {number})!")
                else:
                    await self.highrise.chat("❌ Число от 1 до 200!")
            return

        if msg.isdigit():
            number = int(msg)
            if 1 <= number <= 200:
                emotes = ["emote-dance-casual", "emote-wave", "emote-sit", "emote-happy"]
                chosen = random.choice(emotes)
                await self.highrise.send_emote(chosen, user.id)
                await self.highrise.chat(f"🎭 {username} показал эмоцию на число {number}!")
                return

# --- ЗАПУСК БОТА (ПРАВИЛЬНЫЙ СПОСОБ) ---
bot = MyBot()
bot.run(TOKEN, ROOM_ID)                
