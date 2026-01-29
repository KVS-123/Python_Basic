import requests
import json

def deserialization(url:str) -> dict:
    return json.loads(requests.get(url).text)

def sort_dict(data: dict, need_key_list:list) -> dict:
    return {key: data[key] for key in need_key_list}


url_swapi = 'https://www.swapi.tech/api/starships/?name=X-wing'
starship_data = deserialization(url_swapi)['result'][0]['properties']

pilots = list()
for p_url in starship_data['pilots']:
    pilot_data = deserialization(p_url)['result']['properties']
    homeworld_url = pilot_data['homeworld']
    homeworld = deserialization(homeworld_url)['result']['properties']['name']
    pilot_data['homeworld'], pilot_data['homeworld_url'] = homeworld, homeworld_url
    pilots.append(sort_dict(pilot_data, ['name', 'height', 'mass', 'homeworld', 'homeworld_url']))

starship_data["pilots"] = pilots
starship_data = sort_dict(starship_data, ["name", "max_atmosphering_speed", "starship_class", "pilots"])

with open("starship.json", "w", encoding="utf-8") as f:
    json.dump(starship_data, f, indent=4)