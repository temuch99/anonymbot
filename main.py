from telethon import events
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from config import (API_ID, API_HASH, SESSION_STRING)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler_new_message(event):
    try:
        print(event.message)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    client.start()
    print("--------------")
    print("App is started")
    print("--------------")
    client.run_until_disconnected()
    print("--------------")
    print("App is stopped")
    print("--------------")