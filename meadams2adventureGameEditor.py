"""Marianne Adams
CS120 Adventure Game Text Editor
User should be able to create their own game and save it"""
import json
def main():
    """acts as homebase for program. calls menu, and passes off userChoice to respective functions"""
    userChoice = getMenuChoice()
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        if userChoice == 0:
            print("Quit")
            keepGoing = False
        elif userChoice == 1:
            print("Loaded default game")
            game = loadGame(game)
            keepGoing = False
        elif userChoice == 2:
            loadGame("game.json")
            print("Loaded game.")
            keepGoing = False
        elif userChoice == 3:
            print("Save game.")
            saveGame(game)
            keepGoing = False
        elif userChoice == 4:
            print("Edit or add a node")
#             editField()
#             editNode()
            keepGoing = False
        elif userChoice == 5:
            print("Play current game.")
            playGame(game)
            keepGoing = False
        else:
            print("We've been through this pookie. Quitting game.")
            keepGoing = False

def getMenuChoice():
    """prints menu and returns user choice"""
    print("""0: Exit
1: Load default game
2: Load a game file
3: Save current game
4: Edit or add a node
5: Play current game""")
    userChoice = input("What will you do?")
    userChoice = int(userChoice)
    return userChoice

def getDefaultGame():
    """what it says on the tin"""
    game = {
  "start": [
    "win or lose",
    "win",
    "win",
    "lose",
    "lose"
  ],
  "win": [
    "You win",
    "start over",
    "start",
    "quit",
    "quit"
  ],
  "lose": [
    "You lose",
    "start over",
    "start",
    "quit",
    "quit"
  ]
}
    return game

def saveGame(currentGame):
    """saves game to json file"""
    outFile = open("game.json", "w")
    json.dump(currentGame, outFile, indent=2)
    outFile.close()
    print("Saved game data to game.json.")
    
def loadGame(currentGame):
    """loads game to be read"""
    file = open("game.json", "r")
    game = json.load(file)
    print(game)
    file.close()
    
def playGame(game):
    """runs through game taking only game data"""
    keepGoing = True
    currentNode = "start"
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)
            
def playNode(game, currentNodeKey):
    """plays a node taking game data and currentNodeKey"""
    currentNode = game[currentNodeKey]
    if currentNode in game.keys():
        (description, menu1, node1, menu2, node2) = currentNode
        print(f"""{description}
    1: {menu1}
    2: {menu2}""")
        nodeChoice = input("1 or 2?")
        if nodeChoice.isnumeric():
            nodeChoice = int(nodeChoice)
            if nodeChoice == 1:
                nextNode = node1
                currentNode = newNode
            elif nodeChoice == 2:
                nextNode = node2
            else:
                print("You bovine. Enter 1 or 2.")
                nextNode = currentNode
        else:
            print("Give me a number, pookie.")
            nextNode = "quit"
    else:
        print("Babes. I don't know what that is. Are you on crack?")
        nextNode = "quit"
    return nextNode

main()