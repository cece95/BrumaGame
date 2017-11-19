import json

class EnemyCountry:
    def __init__(self, json):
        self.defeated = False
        self.name = json['name']
        self.army = json['army']
        self.victory_money = json['victory_money']
        self.victory_troops = json['victory_troops']
