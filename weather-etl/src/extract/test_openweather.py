from src.extract.openweather import extract_current_weather, save_raw_weather

payload = extract_current_weather()
path = save_raw_weather(payload)

print("Arquivo salvo em:", path)
print("Cidade retornada:", payload.get("name"))