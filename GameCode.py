import random
import time
import os

us = 1
uk = 1
fr = 1
ge = 1
ru = 1
army = 5000
population = 25000
tension = 10
money = 50000
xxx = 100


def initialize():
    global us
    global uk
    global fr
    global ge
    global ru
    global army
    global population
    global tension
    global money
    global xxx

    us = 1
    uk = 1
    fr = 1
    ge = 1
    ru = 1
    army = 5000
    population = 25000
    tension = 10
    money = 50000
    xxx = 100


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


def command_parade():
    global money
    global tension
    print("Would you like to hold a parade? It will cost $10,000.")
    print("It will also reset your country's tension to zero percent!")
    print("1=yes/2=no")
    parade = input("")
    if parade == "1":
        money = money - 10000
        if money < 0:
            money = money + 10000
            print("You do not have enough money to have a parade.")
        else:
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
                print("Following the parade, a visiting group of 100 civilians have decided to live in %s!" % country)
            else:
                print("The parade was a disaster!")
                time.sleep(0.5)
                print("All the parade did was show off your frivolous spending habits!")
                time.sleep(1)
                print("Tension in your country has risen by 51%! A civil war is possible!")
                tension = tension + 51
                time.sleep(0.5)
                print("Furthermore, the country of %s lies in ruins! You lose an additional $10,000." % country)
                money = money - 10000
                if money < 0:
                    money = 0
                else:
                    return False

    else:
        print("")
    return True


def command_buy():
    global army
    global money

    print("What would you like to buy?")
    time.sleep(0.5)
    print("1 = 100 soldiers for $500")
    print("2 = 1000 soldiers for $5,000")
    print("3 = 1500 soldiers for $7,000")
    print("4 = 2000 soldiers for $9,500")
    print("5 = 5000 soldiers for £20,000")
    buy = input("")
    if buy == "1":
        buy_soldiers(100, 500)
    elif buy == "2":
        buy_soldiers(1000, 5000)
    elif buy == "3":
        buy_soldiers(1500, 7000)
    elif buy == "4":
        buy_soldiers(2000, 9500)
    elif buy == "5":
        buy_soldiers(5000, 20000)
    else:
        print("Incorrect command!")


def buy_soldiers(soldiers, cost):
    global army
    global money
    if money > cost:
        print("You have purchased {0} soldiers".format(soldiers))
        army = army + soldiers
        money = money - cost
    else:
        print("No money. Could not purchase soldiers.")


def command_explore():
    global population
    global army
    global money
    global tension

    print("Are you sure you would like to explore the world?")
    print("You have the chance to find soldiers and people, but it could end in disaster.")
    print("1=yes/2=no")
    explore = input("")
    if explore == "1":
        if population < 400 or army < 100:
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
                    money = money + 200
                    print("Following this success, your country's tension has decreased by 4 percent.")
                    army = army + 100
                    population = population + 200
                    tension = tension - 4
                    if tension < 0:
                        tension = 0

                else:
                    print("It's a miracle! You've stumbled across a group of 1000 soldiers and $2,500!")
                    money = money + 2500
                    print("Follow this success, your country's tension has decreased by 15 percent.")
                    army = army + 1000
                    tension = tension - 15
                    if tension < 0:
                        tension = 0

            else:
                print('It was a disaster!')
                print('You have lost 400 civilians and 100 soldiers!')
                print("You have also lost $500.")
                print("Your country's tension has increased by 20%.")
                money = money - 500
                army = army - 100
                population = population - 400
                tension = tension + 20

    if explore == "2":
        print("")


def command_conscript():
    global population
    global army
    global tension
    print('How many people would you like to conscript?')
    print('(1000 people conscripted = tension increase of 10%)')
    con = int(input(""))
    if con > population:
        print("Can't conscript more people than live in your country.")
    elif con < 100:
        print("You must conscript more than 100 people.")
    elif con + army > 10000:
        print("You can only conscript up to 10000 troops!")
    else:
        army = army + con
        population = population - con
        tension = tension + (con / 1000)
        print("You have conscripted %d people" % con)
        print("Your population is now %d" % population)
        print("Your tension is now %d percent" % tension)


def command_war():
    global us
    global uk
    global fr
    global ge
    global ru

    print("Which country would you like to go to war with?")
    time.sleep(0.1)
    print("1 = United States of America")
    print("2 = United Kingdom")
    print("3 = France")
    print("4 = Germany")
    print("5 = Russia")

    target = input("")
    if target == "1":
        us = war(us, "The USA", 10000, 2000)

    if target == "2":
        uk = war(uk, "The UK", 7500, 1500)

    if target == "3":
        fr = war(fr, "France", 5000, 1000)

    if target == "4":
        ge = war(ge, "Germany", 4500, 750)

    if target == "5":
        ru = war(ru, "Russia", 50000, 7500)
    return True


def war(target, name, standing_army, conversion):
    global army
    global money
    global tension
    victory = (army / (army + standing_army) * 100)
    print("{0} has an army of {1} men. Your chance of winning is {2} percent.".format(name, standing_army, victory))
    time.sleep(0.5)
    print("Would you like to go to war with {0}?".format(name))
    print("1=yes/2=no")
    answer = int(input(""))
    if answer == 1:
        if target == 1:
            print("Your troops are travelling to {0}...".format(name))
            time.sleep(1)
            print("Your troops are fighting...")
            time.sleep(1)
            if random.randint(0, 100) < victory:
                target = 0
                print('Success! Your troops defeated the opposition soldiers!')
                print('You were also able to convert {0} enemy soldiers!'.format(conversion))
                army = army + conversion
                print("Your net profit from the war was $500.")
                money = money + 500
                print("As a result of your success, your country's tension has decreased by 10%.")
                tension = tension - 10
                if tension < 0:
                    tension = 0
            else:
                army = army / 1.5
                print('Failure! Your troops were defeated, %d men were killed.' % army)
                print("As a result of your failure, your country's tension has increased by 5%")
                tension = tension + 5
                time.sleep(1)
                print("The defeat cost you $500")
                money = money - 500
        else:
            print("You have already conquered {0}!".format(name))
    return target


def civil_war():
    global us
    global uk
    global fr
    global ge
    global ru
    global tension
    global army
    global population
    print('Civil war! The country has turned against you!')
    if random.randint(0, 100) < 60:
        time.sleep(1)
        print(
            'The uprising has been put down. Sadly, half of your soldiers have died and 5000 civilians have fled')
        time.sleep(1)
        print("Following the war, your country's tension is down to 10 percent.")
        tension = 10
        army = army / 2
        population = population - 5000
    else:
        time.sleep(1)
        print('The uprising could not be put down!')
        if random.randint(0, 100) < 25:
            print("Luckily, you have escaped with a tenth of your army and 400 civilians.")
            uk = 1
            us = 1
            fr = 1
            ru = 1
            ge = 1
            tension = 0
            population = 400
            army = army / 10
        else:
            print("You have lost everything and everyone. You are captured and sentenced to death.")
            print("Game over")
            time.sleep(5)
            print("New game:")
            start()


def start():
    global us
    global uk
    global fr
    global ge
    global ru
    global army
    global population
    global tension
    global money
    global xxx

    initialize()

    while True:
        command = input("Type a command: ")
        if command == "!help":
            command_help()

        elif command == "!parade":
            if not command_parade():
                continue

        elif command == "!buy":
            command_buy()

        elif command == "!money":
            print("Your country has $%d" % money)

        elif command == "!explore":
            command_explore()

        elif command == "!conscript":
            command_conscript()

        elif command == "!army":
            print("The size of your army is %d" % army)

        elif command == "!population":
            print("The population of your country is %d" % population)

        elif command == "!war":
            if not command_war():
                continue

        elif command == "!tension":
            print("Your country's tension is %d percent" % tension)
            time.sleep(0.1)
            print("A country's tension goes up if a war is lost.")
            print("A country's tension goes down if a war is won.")
            print("If a country's tension is above 50%, a civil war may begin.")

        else:
            print("Incorrect command!")

        if money < 0:
            time.sleep(1)
            print("You have no money!")
            money = 0

        if tension > 50:
            time.sleep(1)
            print("Your tension is now above 50 percent! There is a chance of civil war.")
            if random.randint(0, 100) < 40:
                time.sleep(2)
                civil_war()
            else:
                time.sleep(3)
                print('There was no civil war. For now.')
                time.sleep(2)
                print("Your country's tension is now 35 percent.")
                tension = 35

        if ru + ge + uk + us + fr == 0:
            time.sleep(2)
            print("YOU HAVE WON, CONGRATULATIONS!")
            time.sleep(20)


country = input("Please enter the name of your country: ")
time.sleep(0.5)
os.system('cls')
print("Your country is called %s" % country)
print("")
time.sleep(0.5)
print("Type !help to see commands")
start()
