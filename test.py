from balepy import Client, filters
from balepy.types import Message

# bot_token = "0123456789:****************************************"
bot_token = "TOKEN"

app = Client("MyBot", bot_token)

@app.on_message(filters.command("start"))
async def updates(message: Message):
    await message.reply("Hello from balepy.")

app.run()
