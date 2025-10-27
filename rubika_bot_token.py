import os
import asyncio
from rubpy.bot import BotClient, filters
from openai import AsyncOpenAI


TOKEN = os.getenv("RUBIKA_BOT_TOKEN", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()


async def main() -> None:
    if not TOKEN:
        TOKEN = input("RUBIKA_BOT_TOKEN را وارد کنید: ").strip()
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not openai_api_key:
        openai_api_key = input("OPENAI_API_KEY را وارد کنید: ").strip()
    if not TOKEN or not openai_api_key:
        raise SystemExit("توکن یا کلید OpenAI نامعتبر است.")

    bot = BotClient(TOKEN)
    ai = AsyncOpenAI(api_key=openai_api_key)

    @bot.on_update(filters.commands("start"))
    async def on_start(c: BotClient, update):
        await c.send_message(update.chat_id, "بله")

    @bot.on_update(filters.text)
    async def on_text(c: BotClient, update):
        # استخراج متن پیام
        text = ""
        if getattr(update, "new_message", None) and update.new_message.text:
            text = update.new_message.text
        elif getattr(update, "text", None):
            text = update.text
        text = (text or "").strip()
        if not text:
            return

        # جلوگیری از پاسخ به دستورات
        if text.startswith("/"):
            return

        # پرسش از مدل هوش مصنوعی
        try:
            resp = await ai.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful Persian assistant. پاسخ‌ها را کوتاه، دقیق و فارسی بده."},
                    {"role": "user", "content": text},
                ],
                temperature=0.7,
                max_tokens=500,
            )
            answer = (resp.choices[0].message.content or "").strip()
        except Exception:
            answer = "مشکلی پیش آمد. لطفاً دوباره تلاش کنید."

        await c.send_message(update.chat_id, answer or "پاسخی دریافت نشد.")

    await bot.run()


if __name__ == "__main__":
    asyncio.run(main())

