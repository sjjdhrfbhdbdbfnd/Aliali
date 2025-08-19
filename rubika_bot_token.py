import os
import asyncio
from rubpy.bot import BotClient, filters


TOKEN = os.getenv("RUBIKA_BOT_TOKEN", "")


async def main() -> None:
    if not TOKEN:
        raise SystemExit("Set RUBIKA_BOT_TOKEN env variable to your bot token")

    bot = BotClient(TOKEN)

    @bot.on_update(filters.commands("start"))
    async def on_start(c: BotClient, update):
        await c.send_message(update.chat_id, "بله")

    await bot.run()


if __name__ == "__main__":
    asyncio.run(main())

