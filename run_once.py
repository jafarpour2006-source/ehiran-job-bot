import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from search import collect
from database import init_db, exists, save
from formatter import format_job
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

async def run():
    init_db()
    bot = Bot(TELEGRAM_BOT_TOKEN)
    jobs = await asyncio.to_thread(collect)
    new_count = 0
    for job in jobs:
        if exists(job["url"]):
            continue
        try:
            await bot.send_message(
                chat_id=TELEGRAM_CHANNEL_ID,
                text=format_job(job),
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=False,
            )
            save(job)
            new_count += 1
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"Telegram error: {e}")
    print(f"پایان جستجو؛ {new_count} آگهی جدید ارسال شد.")

if __name__ == "__main__":
    asyncio.run(run())
