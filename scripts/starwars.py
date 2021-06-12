import requests
import sys
import json


planets_full_json = requests.get('https://swapi.dev/api/planets').json()
count = planets_full_json["count"]
planets_results = planets_full_json["results"]

def factorial(number):
    number = int(round(number))

    if number > 1:
        return factorial(number-1)*number
    elif number < 1:
        return ("NAN")
    else:
        return 1


def factorial_planet(planet):
    flag = False

    for iterator in planets_results:
        if iterator["name"] == planet:
            flag = True
            print('Gravity: ' + iterator["gravity"])
            gravity_string = iterator["gravity"].split()
            
            if gravity_string[0] != 'N/A':
                print('Factorial: ' + str((factorial(float(gravity_string[0])))))

    if flag == False:
        print('There is no planet with that name')



def factorial_all():
    for iterator in planets_results:
        print('Planet: ' + iterator["name"])
        print('Gravity: ' + iterator["gravity"])
        gravity_string = iterator["gravity"].split()

        if gravity_string[0] != 'N/A':
            print('Factorial: ' + str((factorial(float(gravity_string[0])))))

        print()



if len(sys.argv) > 4:
    print('Too many arguments')
    sys.exit()

elif len(sys.argv) == 3:
    if sys.argv[1] != 'planet':
        print('Only two arguments if the first is "planet" and the second is "<planet name>"')
    else:
        print('Calculating planet ' + sys.argv[2].capitalize())
        factorial_planet(sys.argv[2].capitalize())

elif len(sys.argv) == 2 and sys.argv[1] == 'all':
    print('Calculating all planets')
    factorial_all()

else:
    print('Wrong arguments')








