import random
import time
import json
from functools import reduce

from PlayerCountry import PlayerCountry
from EnemyCountry import EnemyCountry

class World:
    def __init__(self):
        self.enemy_nations = []
        self.player_nation = PlayerCountry("")
        self.initialize_enemy_nations()

    def initialize_enemy_nations(self):
        with open('Countries.json', 'r') as json_file:
            countries_list = json.load(json_file)
            self.enemy_nations = []
            for c in countries_list:
                self.enemy_nations.append(EnemyCountry(c))

    @staticmethod
    def command_help():
        print("!army - view size of army")
        print("!population - view size of population")
        print("!money - view your country's treasury")
        print("!war - go to war")
        print("!tension - view country's tension")
        print("!conscript - conscript people into the army")
        print("!explore - explore the world")
        print("!buy - buy more soldiers")
        print("!parade - hold a parade")

    def command_parade(self):
        print("Would you like to hold a parade? It will cost $10,000.")
        print("It will also reset your country's tension to zero percent!")
        print("1=yes/2=no")
        parade = input("")
        if parade == "1":
            if self.player_nation.afford_parade():
                time.sleep(0.1)
                print("Preparing parade...")
                time.sleep(0.5)
                print("Carrying out parade...")
                time.sleep(1)
                if random.randint(0, 100) < 90:
                    print("The parade was a success!")
                    time.sleep(0.5)
                    print("Your country's tension is now zero percent!")
                    time.sleep(0.5)
                    print(
                        "Following the parade, a visiting group of 100 civilians have decided to live in {0}!".format(
                            self.player_nation.name))
                else:
                    print("The parade was a disaster!")
                    time.sleep(0.5)
                    print("All the parade did was show off your frivolous spending habits!")
                    time.sleep(1)
                    print("Tension in your country has risen by 51%! A civil war is possible!")
                    time.sleep(0.5)
                    print("Furthermore, the country of {0} lies in ruins! You lose an additional $10,000.".format(
                            self.player_nation.name))
            else:
                print("You cannot afford a parade!")

        else:
            print("")
        return True

    def command_buy(self):
        print("What would you like to buy?")
        time.sleep(0.5)
        print("1 = 100 soldiers for $500")
        print("2 = 1000 soldiers for $5,000")
        print("3 = 1500 soldiers for $7,000")
        print("4 = 2000 soldiers for $9,500")
        print("5 = 5000 soldiers for £20,000")
        buy = input("")
        if buy == "1":
            self.buy_troops(100, 500)
        elif buy == "2":
            self.buy_troops(1000, 5000)
        elif buy == "3":
            self.buy_troops(1500, 7000)
        elif buy == "4":
            self.buy_troops(2000, 9500)
        elif buy == "5":
            self.buy_troops(5000, 20000)
        else:
            print("Incorrect command!")

    def buy_troops(self, troops, cost):
        if self.player_nation.buy_troops(troops, cost):
            print("Hired {0} troops for ${1}".format(troops, cost))
        else:
            print("You could not afford the troops")

    def command_explore(self):
        print("Are you sure you would like to explore the world?")
        print("You have the chance to find soldiers and people, but it could end in disaster.")
        print("1=yes/2=no")
        explore = input("")
        if explore == "1":
            if self.player_nation.population < 400 or self.player_nation.army < 100:
                print("Can not explore with this few people!")
            else:
                print("Sending 500 people to explore...")
                time.sleep(0.5)
                print("Exploring...")
                time.sleep(1)
                if random.randint(0, 100) < 60:
                    print('Success!')
                    if random.randint(0, 100) < 75:
                        print('You have found 200 people, 100 soldiers and $200!')
                        self.player_nation.money += 200
                        print("Following this success, your country's tension has decreased by 4 percent.")
                        self.player_nation.army += 100
                        self.player_nation.population += 200
                        self.player_nation.tension -= 4
                        if self.player_nation.tension < 0:
                            self.player_nation.tension = 0

                    else:
                        print("It's a miracle! You've stumbled across a group of 1000 soldiers and $2,500!")
                        self.player_nation.money += 2500
                        print("Follow this success, your country's tension has decreased by 15 percent.")
                        self.player_nation.army += 1000
                        self.player_nation.tension -= 15
                        if self.player_nation.tension < 0:
                            self.player_nation.tension = 0

                else:
                    print('It was a disaster!')
                    print('You have lost 400 civilians and 100 soldiers!')
                    print("You have also lost $500.")
                    print("Your country's tension has increased by 20%.")
                    self.player_nation.money -= 500
                    self.player_nation.army -= 100
                    self.player_nation.population -= 400
                    self.player_nation.tension += 20

        if explore == "2":
            print("")

    def command_conscript(self):
        print('How many people would you like to conscript?')
        print('(1000 people conscripted = tension increase of 10%)')
        con = int(input(""))
        if con > self.player_nation.population:
            print("Can't conscript more people than live in your country.")
        elif con < 100:
            print("You must conscript more than 100 people.")
        elif con + self.player_nation.army > 10000:
            print("You can only conscript up to 10000 troops!")
        else:
            self.player_nation.army += con
            self.player_nation.population -= con
            self.player_nation.tension += (con / 1000)
            print("You have conscripted %d people" % con)
            print("Your population is now %d" % self.player_nation.population)
            print("Your tension is now %d percent" % self.player_nation.tension)

    def command_war(self):
        print("Which country would you like to go to war with?")
        time.sleep(0.1)
        print("1 = United States of America")
        print("2 = United Kingdom")
        print("3 = France")
        print("4 = Germany")
        print("5 = Russia")

        target = int(input(""))
        if target in range(1, 6):
            self.war(self.enemy_nations[target-1])
        return True

    def war(self, target):
        """
        :param EnemyCountry target:
        :return:
        """
        victory = (self.player_nation.army / (self.player_nation.army + target.army) * 100)
        print("{0} has an army of {1} men. Your chance of winning is {2} percent.".format(target.name, target.army, victory))
        time.sleep(0.5)
        print("Would you like to go to war with {0}?".format(target.name))
        print("1=yes/2=no")
        answer = int(input(""))
        if answer == 1:
            if not target.defeated:
                print("Your troops are travelling to {0}...".format(target.name))
                time.sleep(1)
                print("Your troops are fighting...")
                time.sleep(1)
                if self.player_nation.war(target):
                    print('Success! Your troops defeated the opposition soldiers!')
                    print('You were also able to convert {0} enemy soldiers!'.format(target.victory_troops))
                    print("Your net profit from the war was $500.")
                    print("As a result of your success, your country's tension has decreased by 10%.")
                else:
                    print('Failure! Your troops were defeated, %d of your men survived the battle.' % self.player_nation.army)
                    print("As a result of your failure, your country's tension has increased by 5%")
                    time.sleep(1)
                    print("The defeat cost you $500")
            else:
                print("You have already conquered {0}!".format(target.name))
        return target

    def civil_war(self):
        print('Civil war! The country has turned against you!')
        if random.randint(0, 100) < 60:
            time.sleep(1)
            print(
                'The uprising has been put down. Sadly, half of your soldiers have died and 5000 civilians have fled')
            time.sleep(1)
            print("Following the war, your country's tension is down to 10 percent.")
            self.player_nation.tension = 10
            self.player_nation.army = self.player_nation.army / 2
            self.player_nation.population -= 5000
        else:
            time.sleep(1)
            print('The uprising could not be put down!')
            if random.randint(0, 100) < 25:
                print("Luckily, you have escaped with a tenth of your army and 400 civilians.")
                self.initialize_enemy_nations()
                self.player_nation.tension = 0
                self.player_nation.population = 400
                self.player_nation.army = self.player_nation.army / 10
            else:
                print("You have lost everything and everyone. You are captured and sentenced to death.")
                print("Game over")
                time.sleep(5)
                print("New game:")

    def run(self):
        print("Type !help for a list of commands")
        while True:
            command = input("Type a command: ")
            if command == "!help":
                self.command_help()

            elif command == "!parade":
                if not self.command_parade():
                    continue

            elif command == "!buy":
                self.command_buy()

            elif command == "!money":
                print("Your country has $%d" % self.player_nation.money)

            elif command == "!explore":
                self.command_explore()

            elif command == "!conscript":
                self.command_conscript()

            elif command == "!army":
                print("The size of your army is %d" % self.player_nation.army)

            elif command == "!population":
                print("The population of your country is %d" % self.player_nation.population)

            elif command == "!war":
                if not self.command_war():
                    continue

            elif command == "!tension":
                print("Your country's tension is %d percent" % self.player_nation.tension)
                time.sleep(0.1)
                print("A country's tension goes up if a war is lost.")
                print("A country's tension goes down if a war is won.")
                print("If a country's tension is above 50%, a civil war may begin.")

            else:
                print("Incorrect command!")

            if self.player_nation.money < 0:
                time.sleep(1)
                print("You have no money!")
                self.player_nation.money = 0

            if self.player_nation.tension > 50:
                time.sleep(1)
                print("Your tension is now above 50 percent! There is a chance of civil war.")
                if random.randint(0, 100) < 40:
                    time.sleep(2)
                    self.civil_war()
                else:
                    time.sleep(3)
                    print('There was no civil war. For now.')
                    time.sleep(2)
                    print("Your country's tension is now 35 percent.")
                    self.player_nation.tension = 35

            if self.won():
                time.sleep(2)
                print("YOU HAVE WON, CONGRATULATIONS!")
                time.sleep(20)

    def won(self):
        return reduce((lambda x, y: x and y.defeated), self.enemy_nations)
