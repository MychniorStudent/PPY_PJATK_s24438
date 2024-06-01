import json
from datetime import datetime
from random import randrange
import DataManager as dm
class Player:
    def __init__(self, playerInitData):
        self.id = playerInitData["id"]
        self.modification_date = playerInitData["modification_date"]
        self.name = playerInitData["name"]
        self.account_balance = playerInitData["account_balance"]
        self.isAddicted = playerInitData["isAddicted"]
        self.story = playerInitData["story"]

    def preparePlayerJSON(self):
            data = {}
            data['id'] = self.id
            data['modification_date'] = self.modification_date
            data['name'] = self.name
            data['account_balance'] = self.account_balance
            data['isAddicted'] = self.isAddicted
            data['story'] = self.story
            return data

    def updatePlayerStory(self,newStory):
        self.story = newStory
        self.modification_date = datetime.now()

    def tryToRemoveAddiction(self):
        self.isAddicted = True
        self.modification_date = datetime.now()

    def updatePlayerAccountBalance(self,newAccountBalance):
        self.account_balance += float(newAccountBalance)
        self.modification_date = str(datetime.now())
        dm.updatePlayerData(self.preparePlayerJSON())

    def calculateNextBet(self):
        if self.isAddicted:
            return self.account_balance // 2
        else:
            return self.account_balance // 4

    def chooseNextBetNumber(self):
        return randrange(37)

    def setBet(self):
        self.BetValue = self.calculateNextBet()
        self.BetNumber = self.chooseNextBetNumber()

    def setBetHoomanPlayer(self, betValue, betColor):
        self.BetValue = betValue
        if betColor == "G":
            self.BetNumber = 0
        elif betColor == "B":
            self.BetNumber = 2
        else:
            self.BetNumber = 1

    def getColorBet(self):
        if self.BetNumber == 0:
            return "G"
        elif self.BetNumber % 2 == 0:
            return "B"
        else:
            return "R"

    def clearBet(self):
        self.BetValue = -1
        self.BetNumber = -1


    def showPlayerInfo(self):
        print(self.id, self.name, self.account_balance, self.isAddicted, self.story)

