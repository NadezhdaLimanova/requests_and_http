import requests
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url)
responce = resp.json()
superhero_dict = {}
for heroes in responce:
    for k, v in heroes.items():
        if v == 'Hulk' or v == 'Captain America' or v == 'Thanos':
            for key, values in heroes.items():
                if key == 'powerstats':
                    superhero_dict[v] = values['intelligence']
print(f' Самый умный супергерой - {max(superhero_dict)}')








