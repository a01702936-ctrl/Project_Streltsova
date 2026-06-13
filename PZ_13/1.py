#15. В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным).

import re

with open('PZ_13/radio_stations.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'https?://([a-zA-Z0-9.-]+)'

domains = re.findall(pattern, text)

print("Найденные домены:")
for d in domains:
    print(d)

print(f"\nВсего найдено доменов: {len(domains)}")