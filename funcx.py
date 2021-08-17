from datetime import datetime
import requests

GREETINGS = ["hello", "hi", "halo", "hola", "gm", "good morning"]

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def coordinates(self):
        resultT1 = requests.get("http://ip-api.com/json/")
        resultT2 = resultT1.json()
        lat = round(resultT2["lat"])
        lon = round(resultT2["lon"])

        return lat, lon

def customs(user):
    print(f"Welcome Back, {user}")
    print(f"Eva Is Online. Initiation Time is {datetime.now()}")
    print("All Servers Online")


def isGreeting(term):
    if term in GREETINGS:
        return True

    return False