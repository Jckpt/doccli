from menu_module import m_welcome
from requests import get

VERSION = "v2.5"

def check_update() -> None:

    response = get(
        "https://api.github.com/repos/TowarzyszFatCat/doccli/releases/latest"
    )

    if response.json()["name"] != VERSION:

        print(f"Wersja programu: {VERSION}")
        print(f'Dostępna jest nowa: {response.json()["name"]}')
        print(f"Możesz pobrać nową wersję na stronie programu!\n")
        input("Naciśnij enter by pominąć...")


if __name__ == "__main__":
    check_update()
    m_welcome()