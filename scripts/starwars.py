import requests
import sys

try:
    planets_full_json = requests.get("https://swapi.dev/api/planets").json()
except Exception as e:
    print(f"Error ocurred while getting API information: {e}")
    exit()

planets_results = planets_full_json["results"]


url = "http://localhost:4002/factorial"


def factorial_planet(planet):
    """
    Prints the planet's gravity factorial

    Parameters
    ----------
        planet : str
            planet name (first letter must be capital letter)

    Returns
    -------
        None
    """

    flag = False

    for iterator in planets_results:
        if iterator["name"] == planet:
            flag = True
            print(f'Gravity: {iterator["gravity"]}')
            gravity_string = iterator["gravity"].split()

            if gravity_string[0] != "N/A":
                request = {}  # dictionary tipe
                number = int(round(float(gravity_string[0])))
                request["number"] = number
                try:
                    response = requests.post(url, json=request)
                    print(f"Factorial {str(response.json())}")
                except Exception as e:
                    print(e)

    if flag == False:
        print("There is no planet with that name")


def factorial_all():
    """
    Prints the gravity factorial of the list of all planets contained in the
    global variable 'planets_result'

    Parameters
    ----------
        None

    Returns
    -------
        None
    """

    for iterator in planets_results:
        print(f'Planet: {iterator["name"]}')
        print(f'Gravity: {iterator["gravity"]}')
        gravity_string = iterator["gravity"].split()

        if gravity_string[0] != "N/A":
            request = {}  # dictionary type
            number = int(round(float(gravity_string[0])))
            request["number"] = number
            try:
                response = requests.post(url, json=request)
                print(f"Factorial {str(response.json())}")
            except Exception as e:
                print(e)


if len(sys.argv) > 4:
    print("Too many arguments")
    sys.exit()

elif len(sys.argv) == 3:
    if sys.argv[1] != "planet":
        print(
            'Only two arguments if the first is "planet" and the second is "<planet name>"'
        )
    else:
        print(f"Calculating planet {sys.argv[2].capitalize()}")
        factorial_planet(sys.argv[2].capitalize())

elif len(sys.argv) == 2 and sys.argv[1] == "all":
    print("Calculating all planets")
    factorial_all()

else:
    print("Wrong arguments")
