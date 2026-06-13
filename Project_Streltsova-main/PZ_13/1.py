import re

input_file = "radio_stations.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

domain_pattern = re.compile(r"https?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})")
domains = domain_pattern.findall(text)

unique_domains = list(dict.fromkeys(domains))

print(f"Найдено доменов (уникальных): {len(unique_domains)}")
print("Домены:")
for domain in unique_domains:
    print(domain)