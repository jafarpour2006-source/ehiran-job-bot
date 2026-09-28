import sqlite3
from config import DB_PATH

def init_db():
    con = sqlite3.connect(DB_PATH)
    con.execute("""CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT UNIQUE NOT NULL,
        title TEXT,
        source TEXT,
        published_text TEXT,
        category TEXT,
        first_seen TEXT DEFAULT CURRENT_TIMESTAMP
    )""")
    con.commit()
    con.close()

def exists(url):
    con = sqlite3.connect(DB_PATH)
    row = con.execute("SELECT 1 FROM jobs WHERE url=?", (url,)).fetchone()
    con.close()
    return row is not None

def save(job):
    con = sqlite3.connect(DB_PATH)
    con.execute(
        "INSERT OR IGNORE INTO jobs(url,title,source,published_text,category) VALUES(?,?,?,?,?)",
        (job["url"], job["title"], job["source"], job.get("snippet",""), job.get("category",""))
    )
    con.commit()
    con.close()
