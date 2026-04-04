import asyncio
import random
from highrise import BaseBot
from highrise.models import SessionMetadata, User, Position, AnchorPosition

# --- КОНФИГУРАЦИЯ ---
# Замените эти значения на свои!
ROOM_ID = "69ced5ed0c7c2e72825ba9eb"
TOKEN = "d819ee0c359cc3c7f512bb0abff0e155edda0e285a599ac0e548a397c65fab56"
# --------------------

class MyBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        """Действия при запуске бота"""
        print("✅ Бот успешно запущен и подключен к комнате!")
        await self.highrise.chat("✨ Привет! Я бот с эмоциями и телепортацией!")
        await self.highrise.chat("📜 Доступные команды: !emote [число от 1 до 200], !help, !join")
        # Телепортируем бота на второй этаж при старте
        await self.highrise.teleport(session_metadata.user_id, Position(5, 1, 0, "FrontLeft"))
        print("📍 Бот перемещен на второй этаж.")

    async def on_user_join(self, user: User, position: Position) -> None:
        """Когда новый игрок заходит в комнату"""
        welcome_text = f"🎉 Добро пожаловать, {user.username}! Напиши !help чтобы увидеть команды."
        await self.highrise.chat(welcome_text)
        print(f"👤 {user.username} присоединился к комнате.")

    async def on_chat(self, user: User, message: str) -> None:
        """Обработка сообщений в чате"""
        msg = message.lower().strip()
        username = user.username

        # Игнорируем свои сообщения, чтобы избежать зацикливания
        if user.id == self.highrise.user.id:
            return

        # --- Команда !help ---
        if msg == "!help":
            await self.highrise.chat("📜 Команды:")
            await self.highrise.chat("!emote [число 1-200] - случайная эмоция")
            await self.highrise.chat("!join - телепортироваться ко мне")
            return

        # --- Команда !join (Телепортация игрока к боту) ---
        if msg == "!join":
            await self.highrise.chat(f"🔄 Телепортирую {username} к себе...")
            # Телепортируем игрока на позицию бота (второй этаж)
            await self.highrise.teleport(user.id, Position(5, 1, 0, "FrontLeft"))
            return

        # --- Команда !emote <число> (Случайная эмоция по числу) ---
        # Используем emote_id из официальной документации SDK
        # Список доступных эмоций: 'emote-dance-casual', 'emote-wave', 'emote-sit', и т.д.
        if msg.startswith("!emote"):
            parts = msg.split()
            if len(parts) > 1:
                try:
                    number = int(parts[1])
                    if 1 <= number <= 200:
                        # Генерируем случайный ID эмоции на основе числа
                        # (В реальности эмоции имеют фиксированные ID, здесь пример для демонстрации)
                        # Случайный выбор из реальных ID эмоций Highrise
                        emote_list = [
                            "emote-dance-casual", "emote-wave", "emote-sit",
                            "emote-happy", "emote-sad", "emote-angry",
                            "emote-clap", "emote-boxer", "emote-rest"
                        ]
                        chosen_emote = random.choice(emote_list)
                        await self.highrise.send_emote(chosen_emote, user.id)
                        await self.highrise.chat(f"🎭 {username} исполнил эмоцию: {chosen_emote} (по числу {number})")
                        print(f"🎭 Бот показал эмоцию {chosen_emote} для {username}")
                    else:
                        await self.highrise.chat("❌ Число должно быть от 1 до 200!")
                except ValueError:
                    await self.highrise.chat("❌ Пожалуйста, укажи число после команды. Пример: !emote 42")
            else:
                # Если число не указано, показываем случайную эмоцию без привязки
                await self.highrise.send_emote("emote-dance-casual", user.id)
                await self.highrise.chat(f"🎭 {username}, ты не указал число, но я показал танец!")
            return

        # Если пользователь написал просто число от 1 до 200 (без !emote)
        if msg.isdigit():
            number = int(msg)
            if 1 <= number <= 200:
                emote_list = [
                    "emote-dance-casual", "emote-wave", "emote-sit",
                    "emote-happy", "emote-sad", "emote-angry"
                ]
                chosen_emote = random.choice(emote_list)
                await self.highrise.send_emote(chosen_emote, user.id)
                await self.highrise.chat(f"🎭 {username} показал эмоцию на число {number}!")
                return

        # Если сообщение не распознано как команда
        # (можно добавить стандартный ответ или игнорировать)
        # await self.highrise.chat(f"Неизвестная команда. Напиши !help")

# --- ЗАПУСК БОТА ---
async def main():
    bot = MyBot()
    await bot.run(TOKEN, ROOM_ID)

if __name__ == "__main__":
    asyncio.run(main())
