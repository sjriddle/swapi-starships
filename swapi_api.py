import requests
import json
import sys

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


def starship_pilots(film_input=sys.argv[1]):
    result = []
    pilot_list = []
    film_id = 0
    pilot_check = {}

    if film_input.lower() == 'a new hope':
        film_id = 1
    elif film_input.lower() == 'the empire strikes back':
        film_id = 2
    elif film_input.lower() == 'return of the jedi':
        film_id = 3
    elif film_input.lower() == 'the phantom menace':
        film_id = 4
    elif film_input.lower() == 'attack of the clones':
        film_id = 5
    elif film_input.lower() == 'revenge of the sith':
        film_id = 6
    elif film_input.lower() == 'the force awakens':
        film_id = 7
    else:
        print(f'"{film_input}" is not a valid input. Plase input one of the following:\n'
              f'[+] A New Hope\n'
              f'[+] The Empire Strikes Back\n'
              f'[+] Return of the Jedi\n'
              f'[+] The Phantom Menace\n'
              f'[+] Attack of the Clones\n'
              f'[+] Revenge of the Sith\n'
              f'[+] The Force Awakens')
        sys.exit(1)

    response = requests.get(f'https://swapi.co/api/films/{film_id}')
    if response.status_code == 200:
        output = json.loads(response.content.decode('utf-8'))
        for ship in output['starships']:
            ship_response = requests.get(ship)
            ship_output = json.loads(ship_response.content.decode('utf-8'))
            for pilot in ship_output['pilots']:
                if pilot in pilot_check.values():
                    key_to_add = None
                    for name, url in pilot_check.items():
                        if pilot == url:
                            key_to_add = name
                    pilot_list.append(key_to_add)
                else:
                    pilot_response = requests.get(pilot)
                    pilot_output = json.loads(pilot_response.content.decode('utf-8'))
                    pilot_check.update({pilot_output['name']: pilot})
                    pilot_list.append(pilot_output['name'])

            output_object = {
                "name": ship_output['name'],
                "pilots": {
                    json.dumps(pilot_list)
                }
            }
            result.append(output_object)
            pilot_list = []
    json_obj = json.dumps(result, default=set_default)
    print(json_obj)
    sys.exit(0)


if __name__ == '__main__':
    starship_pilots()