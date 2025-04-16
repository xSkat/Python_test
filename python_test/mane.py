import requests

host = 'https://api.pokemonbattle.ru/v2'
token = 'MY_TOKEN'
path_sozd = '/pokemons'
path_add_pok = '/trainers/add_pokeball'

HEADers = {
    'trainer_token': token,
    'Content-Type' : 'application/json'
    }

data_sozd = {
    "name": "generate",
    "photo_id": -1
}


# Создали покемона
sozdal = requests.post(url = host + path_sozd, headers = HEADers, json = data_sozd)
print(sozdal.text)


# Изменяем имя и фото
pok_id = sozdal.json()['id']
data_rename = {
    "pokemon_id": pok_id,
    "name": "XRP",
    "photo_id": -1
}

rename = requests.put(url = host + path_sozd, headers = HEADers, json = data_rename)
print(rename.text)

# Ловим нашего стилизованного покемона
data_add_pok = {
    "pokemon_id": pok_id
}

add_pok = requests.post(url = host + path_add_pok, headers = HEADers, json = data_add_pok)
print(add_pok.text)
