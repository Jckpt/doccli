from pypresence import Presence
from os import getpid

RPC = Presence(client_id="1206583480771936318")


def connect_discord() -> None:
    try:
        print(
            "[INFO] Łączenie z discordem... Jeżeli zajmuje to zbyt długo, możesz anulować łączenie za pomocą <CTRL C>"
        )
        RPC.connect()
        RPC.clear(getpid())
    except KeyboardInterrupt:
        print("Anulowano łączenie z discordem!")


def update_discord(state: str, details: str, time) -> None:
    RPC.update(
        state=f"{state}",
        details=f"{details}",
        large_image="icon_1",
        large_text="CLI do oglądania anime z docchi.pl! Teraz także na Windowsa!",
        start=int(time),
        buttons=[
            {
                "label": "Pobierz doccli dla Windowsa!",
                "url": "https://github.com/TowarzyszFatCat/doccli",
            },
            {
                "label": "Odwiedź docchi.pl",
                "url": "https://docchi.pl/",
            },
        ],
    )
