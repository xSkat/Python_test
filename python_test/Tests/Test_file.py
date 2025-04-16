import requests
import pytest

host = 'https://api.pokemonbattle.ru/v2'
path_trainers = '/trainers'
my_id = {
    'trainer_id' : '28082'
}

def test_status_code():
    response = requests.get(url = host + path_trainers, params = my_id)
    assert response.status_code == 200


def test_NAME():
    name = requests.get(url = host + path_trainers,  params = my_id)
    assert name.json() ["data"][0]["trainer_name"] == 'Ripple'