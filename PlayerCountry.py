from random import randint


class PlayerCountry:
    def __init__(self, name, army=5000, population=25000, money=50000, tension=10):
        self.name = name
        self.army = army
        self.population = population
        self._money = money
        self._tension = tension

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if value < 0:
            self._money = 0
        else:
            self._money = value

    @property
    def tension(self):
        return self._tension

    @tension.setter
    def tension(self, value):
        if value < 0:
            self._tension = 0
        else:
            self._tension = value

    def buy_troops(self, troops, cost):
        if self.money > cost:
            self.army += troops
            self.money -= cost
            return True
        else:
            return False

    def afford_parade(self, cost=10000):
        return self.money > cost

    def parade(self, civilians=100):
        if randint(0, 100) < 90:
            self.tension = 0
            self.population += civilians
            return True
        else:
            self.tension += 51
            self.money -= 1000
            return False

    def war(self, target):
        """
        :param EnemyCountry.EnemyCountry target:
        :return:
        """
        victory = (self.army / (self.army + target.army) * 100)
        if randint(0, 100) < victory:
            target.defeated = True
            self.army += target.victory_troops
            self.money += target.victory_money
            self.tension -= 10
            return True
        else:
            self.army = self.army / 1.5
            self.tension += 5
            self.money -= 500
            return False
