import requests
import json
import sys


def main(film_input=sys.argv[1]):
    api_url = 'https://swapi.co/api/'
    film_id = 0
    pilot_list = []
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
    elif film_input.lower == 'the force awakens':
        film_id = 7
    else:
        print(f'{film_input} is not a valid input. The input one of the following:\n\n'
              f'[+] A New Hope\n'
              f'[+] The Empire Strikes Back\n'
              f'[+] Return of the Jedi\n'
              f'[+] The Phantom Menace\n'
              f'[+] Attack of the Clones\n'
              f'[+] Revenge of the Sith\n'
              f'[+] The Force Awakens')

    response = requests.get(f'{api_url}films/{film_id}')
    if response.status_code == 200:
        output = json.loads(response.content.decode('utf-8'))
        for ship in output['starships']:
            ship_response = requests.get(ship)
            ship_output = json.loads(ship_response.content.decode('utf-8'))
            for pilot in ship_output['pilots']:
                pilot_response = requests.get(pilot)
                pilot_output = json.loads(pilot_response.content.decode('utf-8'))
                pilot_list.append(pilot_output['name'])
            result = {
                "name": ship_output['name'],
                "pilots": {
                    json.dumps(pilot_list)
                }
            }
            print(result)
            pilot_list = []


if __name__ == '__main__':
    main()