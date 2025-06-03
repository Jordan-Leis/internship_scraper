# scraper.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

ADZUNA_APP_ID  = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")
JOOBLE_API_KEY = os.getenv("JOOBLE_API_KEY")
THE_MUSE_API_KEY = os.getenv("THE_MUSE_API_KEY")
USA_JOBS_API_KEY = os.getenv("USA_JOBS_API_KEY")
USAJOBS_USER_AGENT = os.getenv("USAJOBS_USER_AGENT")

def fetch_adzuna(query="electrical engineer intern", country="ca", page=1, per_page=50):
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": per_page,
        "what": query,
        "what_and": "intern"
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json().get("results", [])

def fetch_jooble(query="electrical engineer intern", location="", page=1, limit=50):
    key = JOOBLE_API_KEY
    url = f"https://jooble.org/api/{key}"
    payload = {
        "keywords": query,
        "location": location,
        "page": page,
        "limit": limit,
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, json=payload, headers=headers, timeout=10)
    r.raise_for_status()
    return r.json().get("jobs", [])

def fetch_themuse(page=1):
    key = THE_MUSE_API_KEY
    url = "https://www.themuse.com/api/public/jobs"
    params = {"api_key": key, "page": page, "level": "Internship"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json().get("results", [])

def fetch_usajobs(query="engineering intern", page=1, per_page=25):
    key   = USA_JOBS_API_KEY
    agent = USAJOBS_USER_AGENT
    url = "https://data.usajobs.gov/api/search"
    params = {
        "Keyword": query,
        "PositionOfferingType": "Internship",
        "ResultsPerPage": per_page,
        "Page": page,
    }
    headers = {
        "Host":             "data.usajobs.gov",
        "User-Agent":       agent,
        "Authorization-Key": key,
        "Accept":           "application/json",
    }
    r = requests.get(url, params=params, headers=headers, timeout=10)
    r.raise_for_status()
    items = r.json().get("SearchResult", {}).get("SearchResultItems", [])
    return [item["MatchedObjectDescriptor"] for item in items]

def fetch_remotive(search="intern", limit=100):
    url = "https://remotive.com/api/remote-jobs"
    params = {"search": search, "limit": limit}
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
    r = requests.get(url, params=params, headers=headers, timeout=10)
    r.raise_for_status()
    return r.json().get("jobs", [])

if __name__ == "__main__":
    sources = {
        "adzuna":  fetch_adzuna,
        "jooble":  fetch_jooble,
        "themuse": fetch_themuse,
        "usajobs": fetch_usajobs,
        "remotive":fetch_remotive
    }
    for name, fn in sources.items():
        try:
            results = fn()
            print(f"{name}: {len(results)} jobs")
        except Exception as e:
            print(f"[!] {name} error:", e)
