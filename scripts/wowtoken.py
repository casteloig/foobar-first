from typing import Type
import requests
from requests import HTTPError
import sys
import os


auth_uri = "https://us.battle.net/oauth/token"
client_id = os.getenv("CLIENT_ID", "")
client_secret = os.getenv("CLIENT_SECRET", "")


def auth():
    payload = {"grant_type": "client_credentials"}
    response = requests.post(auth_uri, auth=(client_id, client_secret), data=payload)

    return response.json()["access_token"]


def getPrice(region, bearer):
    uri = f"https://{region}.api.blizzard.com/data/wow/token/index?"
    namespace = f"namespace=dynamic-{region}"

    uri = f"{uri}{namespace}"
    if region == "cn":
        uri = "https://gateway.battlenet.com.cn/data/wow/token/index?namespace=dynamic-cn&locale=zh_CN"

    header = {}
    header["Authorization"] = f"Bearer {bearer}"

    response = requests.get(uri, headers=header)

    print(response.json()["price"])


def main():
    bearer = auth()
    getPrice("us", bearer)
    getPrice("eu", bearer)
    getPrice("cn", bearer)


if __name__ == "__main__":
    main()
