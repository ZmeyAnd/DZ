import requests


intelligence = {}
names_of_characters = [ 'Captain America', 'Thanos', 'Hulk', 'A-Bomb', 'Big Man']
url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
for character in resp.json():
    if character['name'] in names_of_characters:
        intelligence[character['powerstats']['intelligence']] = character['name']
sorted_intelligence = dict(sorted(intelligence.items()))
print(f'Герой {list(sorted_intelligence.values())[-1]} с максимальным уровнем интеллекта {list(sorted_intelligence)[-1]}.')




