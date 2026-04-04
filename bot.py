import asyncio
import random
from highrise import BaseBot
from highrise.models import SessionMetadata, User, Position

# --- КОНФИГУРАЦИЯ ---
ROOM_ID = "69ced5ed0c7c2e72825ba9eb"
TOKEN = "d819ee0c359cc3c7f512bb0abff0e155edda0e285a599ac0e548a397c65fab56"
# --------------------

class MyBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        """Действия при запуске бота"""
        print("✅ Бот успешно запущен и подключен к комнате!")
        await self.highrise.chat("✨ Привет! Я бот с эмоциями и телепортацией!")
        await self.highrise.chat("📜 Доступные команды: !emote [число от 1 до 200], !help, !join")

    async def on_user_join(self, user: User, position: Position) -> None:
        """Когда новый игрок заходит в комнату"""
        welcome_text = f"🎉 Добро пожаловать, {user.username}! Напиши !help чтобы увидеть команды."
        await self.highrise.chat(welcome_text)
        print(f"👤 {user.username} присоединился к комнате.")

    async def on_chat(self, user: User, message: str) -> None:
        """Обработка сообщений в чате"""
        msg = message.lower().strip()
        username = user.username

        # Игнорируем свои сообщения
        if user.id == self.highrise.user.id:
            return

        # --- Команда !help ---
        if msg == "!help":
            await self.highrise.chat("📜 Команды: !emote [число 1-200], !join")
            return

        # --- Команда !join (Телепортация игрока к боту) ---
        if msg == "!join":
            await self.highrise.chat(f"🔄 Телепортирую {username} к себе...")
            await self.highrise.teleport(user.id, Position(5, 1, 0, "FrontLeft"))
            return

        # --- Команда !emote <число> ---
        if msg.startswith("!emote"):
            parts = msg.split()
            if len(parts) > 1:
                try:
                    number = int(parts[1])
                    if 1 <= number <= 200:
                        emote_list = [
                            "emote-dance-casual", "emote-wave", "emote-sit",
                            "emote-happy", "emote-sad", "emote-angry",
                            "emote-clap", "emote-boxer", "emote-rest"
                        ]
                        chosen_emote = random.choice(emote_list)
                        await self.highrise.send_emote(chosen_emote, user.id)
                        await self.highrise.chat(f"🎭 {username} исполнил эмоцию: {chosen_emote} (по числу {number})")
                    else:
                        await self.highrise.chat("❌ Число должно быть от 1 до 200!")
                except ValueError:
                    await self.highrise.chat("❌ Укажи число после команды. Пример: !emote 42")
            return

        # Если пользователь написал просто число от 1 до 200
        if msg.isdigit():
            number = int(msg)
            if 1 <= number <= 200:
                emote_list = ["emote-dance-casual", "emote-wave", "emote-sit", "emote-happy"]
                chosen_emote = random.choice(emote_list)
                await self.highrise.send_emote(chosen_emote, user.id)
                await self.highrise.chat(f"🎭 {username} показал эмоцию на число {number}!")
                return

# --- ЗАПУСК БОТА ---
async def main():
    bot = MyBot()
    await bot.start(TOKEN, ROOM_ID)  # ← ИСПРАВЛЕНО: start вместо run

if __name__ == "__main__":
    asyncio.run(main())
