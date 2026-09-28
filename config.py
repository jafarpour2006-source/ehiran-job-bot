import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "@behdashtmohitiran")
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")
DB_PATH = os.getenv("DB_PATH", "jobs.db")
MAX_RESULTS_PER_QUERY = int(os.getenv("MAX_RESULTS_PER_QUERY", "10"))

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN تنظیم نشده است.")
if not SERPER_API_KEY:
    raise RuntimeError("SERPER_API_KEY تنظیم نشده است.")
