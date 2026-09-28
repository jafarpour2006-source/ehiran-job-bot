from html import escape

def format_job(job):
    title = escape(job["title"])
    snippet = escape(job.get("snippet", ""))
    source = escape(job.get("source", ""))
    url = escape(job["url"], quote=True)
    return (
        f"🆕 <b>{title}</b>\n\n"
        f"📌 {snippet}\n\n"
        f"🌐 {source}\n"
        f'🔗 <a href="{url}">مشاهده آگهی</a>\n\n'
        "#استخدام #بهداشت_محیط"
    )
