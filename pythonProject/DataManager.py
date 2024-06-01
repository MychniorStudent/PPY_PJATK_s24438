import json
from Player import Player

#playersFile = "C:\\Users\\mmano\\Desktop\\python\\players.json"
playersFile = "players.json"
#gamesFile = "C:\\Users\\mmano\\Desktop\\python\\games.json"
gamesFile = "games.json"



# ===Data manager===
def loadPlayers():
    listOfPlayers = []
    playersData = readPlayersFile()
    for player in playersData:
        listOfPlayers.append(Player(player))
    return listOfPlayers

def loadPlayerById(PlayerId):
    listOfPlayers = loadPlayers()

    for player in listOfPlayers:
        if player.id == str(PlayerId):
            return player
def readJsonFile(fileName):
    file = open(fileName)
    data = json.load(file)
    file.close()
    return data

def readPlayersFile():
    return readJsonFile(playersFile)

def readGamesFile():
    return readJsonFile(gamesFile)

def updatePlayerData(playersDataJSON):
    collectionIndex = 0
    file = open(playersFile)
    data = json.load(file)
    file.close()
    for player in data:
        if player['id'] == playersDataJSON['id']:
            break
        collectionIndex += 1
    data[collectionIndex] = playersDataJSON
    file = open(playersFile, "w")
    jsonString = json.dumps(data)
    file.write(jsonString)
    file.close()

def addGameData(gameDataJSON):
    file = open(gamesFile)
    data = json.load(file)
    file.close()
    data.append(gameDataJSON)
    file = open(gamesFile,"w")
    file.seek(0)
    file.write(json.dumps(data))
    file.close()

def getWonGamesForPlayerByIdJSON(playerId):
    resultCollection = {}
    file = open(gamesFile)
    data = json.load(file)
    file.close()
    for game in data:
        for winner in game['Winners']:
            if winner['ID'] == str(playerId):
                resultCollection[game["GameDate"]] = winner
                break
    return resultCollection


def getLostGamesForPlayerByIdJSON(playerId):
    resultCollection = {}
    file = open(gamesFile)
    data = json.load(file)
    file.close()
    for game in data:
        for loser in game['Loosers']:
            if loser['ID'] == str(playerId):
                resultCollection[game["GameDate"]] = loser
                break
    return resultCollection