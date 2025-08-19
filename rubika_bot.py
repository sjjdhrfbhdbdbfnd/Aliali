import os
from rubpy import Client
from rubpy.types import Update


client = Client("rubika_bot_session", display_welcome=True)


@client.on_message_updates()
async def handle_message(update: Update) -> None:

    if not update.is_text:
        return

    incoming_text = (update.text or "").strip()
    if incoming_text == "/start":
        await update.reply("بله")


if __name__ == "__main__":
    phone_number = os.getenv("RUBIKA_PHONE")
    client.run(phone_number=phone_number)

