import DataManager
from random import randrange
from datetime import datetime
import DataManager as dm
rouletteDict = {}

def startGame(playerBetColors, playerBetValue):
    populateDict(rouletteDict)
    players = DataManager.loadPlayers()
    return spinRoulette(players,playerBetColors,playerBetValue)

def populateDict(rouletteDictToPopulate):
    keys = range(37)
    for key in keys:
        if key == 0:
            rouletteDictToPopulate[key] = "G"
        elif key % 2 == 0:
            rouletteDictToPopulate[key] = "B"
        else:
            rouletteDictToPopulate[key] = "R"

    return rouletteDictToPopulate

def getRouletteResult():
    return rouletteDict[randrange(37)]

def showDict():
    for key in rouletteDict:
        print(str(key)+" = "+rouletteDict[key])

def calculatePrize(amount, color):
    if color == "G":
        return float(amount) * 10
    elif color == "B":
        return float(amount) * 2
    elif color == "R":
        return float(amount) * 2

def spinRoulette(players, userColor, userBet):

    GameLogs = []
    GameLogs.append("Log z ostatniej gry")
    GameLogs.append(f"Obstawiłeś kolor {userColor}, pieniążkami o wartości {userBet}")

    # ===Zebranie zakładów od graczy, gracz 0 to użytkownik===
    for player in players:
        if player.id != '0':
            player.setBet()
            GameLogs.append(f'Gracz {player.name}, obstawił kolor {player.getColorBet()}, wartością {player.BetValue}')
        else:
            player.setBetHoomanPlayer(userBet,userColor)
    rouletteResut = getRouletteResult()
    GameLogs.append(f'Ruletka wylosowala {rouletteResut}')
    gameDataJson = {}
    gameDataJson["GameDate"] = str(datetime.now())
    gameDataJson["Winners"] = []
    gameDataJson["Loosers"] = []

    # ===Rozwiązanie gry + stworzenie wpisu do pliku z historią gier===
    for player in players:
        if rouletteDict[player.BetNumber] == rouletteResut:
            GameLogs.append(f'Gracz {player.name} wygrał {calculatePrize(player.BetValue,rouletteResut)}')
            gameDataJson["Winners"].append({"ID": player.id, "Bet": player.BetValue, "Prize": calculatePrize(player.BetValue, rouletteResut)})
            player.updatePlayerAccountBalance(calculatePrize(player.BetValue, rouletteResut))
        else:
            GameLogs.append(f'Gracz {player.name} źle obstawił przegrał swoje życiowe oszczędności')
            gameDataJson["Loosers"].append({"ID":player.id, "Bet": player.BetValue})
            player.updatePlayerAccountBalance(float(player.BetValue) * -1)
    dm.addGameData(gameDataJson)
    return GameLogs





