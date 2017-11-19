import time
import os

from PlayerCountry import PlayerCountry
from EnemyCountry import EnemyCountry
from World import World


if __name__ == "__main__":
    world = World()
    country = input("Please enter the name of your country: ")
    player_country = PlayerCountry(country)
    world.player_nation = player_country
    time.sleep(0.5)
    os.system('cls')
    print("Your country is called %s" % country)
    print("")
    time.sleep(0.5)
    world.run()

