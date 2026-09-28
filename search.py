import requests
from urllib.parse import urlparse
from config import SERPER_API_KEY, MAX_RESULTS_PER_QUERY

QUERIES = [
    "استخدام بهداشت محیط",
    "استخدام کارشناس بهداشت محیط",
    "استخدام مهندس بهداشت محیط",
    "استخدام مسئول فنی بهداشت",
    "استخدام کارشناس HSE",
    "استخدام بهداشت محیط دانشگاه علوم پزشکی",
    "استخدام بهداشت محیط بیمارستان",
    "استخدام بهداشت محیط آب و فاضلاب",
    "استخدام آزمایشگاه آب",
    "استخدام بهداشت محیط کارخانه",
    "استخدام بهداشت محیط شرکت",
]

KEYWORDS = [
    "بهداشت محیط", "کارشناس بهداشت محیط", "مهندس بهداشت محیط",
    "environmental health", "hse", "مسئول فنی", "آب و فاضلاب",
    "آزمایشگاه آب", "دانشگاه علوم پزشکی", "بیمارستان"
]

def is_relevant(title, snippet):
    text = f"{title} {snippet}".lower()
    return any(k.lower() in text for k in KEYWORDS)

def search_web(query):
    r = requests.post(
        "https://google.serper.dev/search",
        headers={"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"},
        json={"q": query, "gl": "ir", "hl": "fa", "num": MAX_RESULTS_PER_QUERY},
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()
    results = []
    for x in data.get("organic", []):
        title = x.get("title", "").strip()
        url = x.get("link", "").strip()
        snippet = x.get("snippet", "").strip()
        if url and title and is_relevant(title, snippet):
            results.append({
                "title": title,
                "url": url,
                "snippet": snippet,
                "source": urlparse(url).netloc,
            })
    return results

def collect():
    found = {}
    for q in QUERIES:
        try:
            for item in search_web(q):
                found[item["url"]] = item
        except Exception as e:
            print("Search error:", q, e)
    return list(found.values())
