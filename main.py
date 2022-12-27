import requests
import json

token = '6d9453b618fd07c084555ad6b54b6bb7'
response = requests.post('test_pokemon.pypokemons', headers={'trainer_token': token}, 
json={
    "name": "Ментор",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": 2770,
    "name": "НеМентор",
    "photo": ""
})

print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token': token}, json={
    "pokemon_id": "2770"
})

print(response_post.text)






