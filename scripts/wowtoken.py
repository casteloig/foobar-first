import requests
import argparse

auth_uri = "https://us.battle.net/oauth/token"


def auth(client_id, client_secret):
    """
    Retrieves the bearer token of Battle.net using client_id and client_secret

    Parameters
    ----------
        client_id : str
            client_id of battlenet
        client_secret: str
            client_secret of the client_id

    Returns
    -------
        str -> the bearer token
    """

    payload = {"grant_type": "client_credentials"}
    try:
        response = requests.post(
            auth_uri, auth=(client_id, client_secret), data=payload
        )
    except requests.exceptions.RequestException as e:
        print(f"Request error")
        raise SystemExit(e)

    try:
        response = response.json()["access_token"]
    except LookupError as e:
        print(f"Token cloud not be decoded")
        raise SystemExit(e)

    return response


def getPrice(region, bearer):
    """
    Retrieves price (gold, silver, bronze) of the region's token

    Parameters
    ----------
        region: str
            Region whose token's price we want to know
        bearer: str
            bearer token to get the information

    Returns
    -------
        str -> gold cost
        str -> silver cost
        str -> bronze cost
    """

    uri = f"https://{region}.api.blizzard.com/data/wow/token/index?"
    namespace = f"namespace=dynamic-{region}"

    uri = f"{uri}{namespace}"
    if region == "cn":
        uri = "https://gateway.battlenet.com.cn/data/wow/token/index?namespace=dynamic-cn&locale=zh_CN"

    header = {}
    header["Authorization"] = f"Bearer {bearer}"

    try:
        response = requests.get(uri, headers=header)
    except requests.exceptions.RequestException as e:
        print("Request error")
        raise SystemExit(e)

    priceString = str(response.json()["price"])
    bronze = priceString[len(priceString) - 2 : len(priceString)]
    silver = priceString[len(priceString) - 4 : len(priceString) - 2]
    gold = priceString[0 : len(priceString) - 4]

    return gold, silver, bronze


def main():

    parser = argparse.ArgumentParser(
        description="Retrieve the token's price of all regions"
    )
    parser.add_argument("--id", type=str, help="Client ID of Blizzard's API")
    parser.add_argument("--secret", type=str, help="Client ID of Blizzard's API")
    args = parser.parse_args()

    client_id = args.id
    client_secret = args.secret

    bearer = auth(client_id, client_secret)
    for i in ["us", "eu", "kr", "tw", "cn"]:
        gold, silver, bronze = getPrice(i, bearer)
        print(f"Region = {i} -> gold: {gold}, silver: {silver}, bronze: {bronze}")


if __name__ == "__main__":
    main()
