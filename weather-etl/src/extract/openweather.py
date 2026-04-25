import os
from datetime import datetime, UTC
from pathlib import Path

import requests


def extract_current_weather() -> dict:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = os.getenv("OPENWEATHER_CITY", "Sao Paulo")
    country = os.getenv("OPENWEATHER_COUNTRY", "BR")
    units = os.getenv("OPENWEATHER_UNITS", "metric")
    lang = os.getenv("OPENWEATHER_LANG", "pt_br")

    if not api_key:
        raise ValueError("A variável OPENWEATHER_API_KEY não foi definida.")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},{country}",
        "appid": api_key,
        "units": units,
        "lang": lang,
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def save_raw_weather(payload: dict) -> str:
    base_path = Path("/opt/airflow/storage/raw")
    base_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    file_path = base_path / f"openweather_current_{timestamp}.json"

    file_path.write_text(
        __import__("json").dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return str(file_path)