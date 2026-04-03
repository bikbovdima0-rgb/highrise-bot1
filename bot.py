
import asyncio
import websockets
import json

TOKEN = "d819ee0c359cc3c7f512bb0abff0e155edda0e285a599ac0e548a397c65fab56"
ROOM_ID = "69ced5ed0c7c2e72825ba9eb"

async def main():
    uri = f"wss://rooms.highrise.game/socket/websocket?vsn=2.0.0&room_id={ROOM_ID}&token={TOKEN}"
    print("✅ Подключение к Highrise...")
    async with websockets.connect(uri) as websocket:
        print("✅ Бот запущен и работает!")
        async for message in websocket:
            try:
                data = json.loads(message)
                if data.get("type") == "chat":
                    username = data.get("user", {}).get("username", "")
                    content = data.get("content", "")
                    if content == "/hello":
                        await websocket.send(json.dumps({
                            "type": "chat",
                            "content": f"Привет, {username}!"
                        }))
            except:
                pass

asyncio.run(main())
