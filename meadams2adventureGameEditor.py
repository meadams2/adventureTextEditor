"""Marianne Adams
CS120 Adventure Game Text Editor
User should be able to create their own game and save it"""
import json
def main():
    userChoice = getMenuChoice()
    if userChoice == 1:
        getDefaultGame()
        print(game)
    if userChoice == 2:
        loadGame("adventureGame.json")
        print("Loaded game.")
    if userChoice == 3:
        saveGame()
    if userChoice == 4:
        editField()
        editNode()
    if userChoice == 5:
        playGame()
        playNode()

def getMenuChoice():
    print("""0: Exit
1: Load default game
2: Load a game file
3: Save current game
4: Edit or add a node
5: Play current game""")
    userChoice = input("What will you do?")
    return userChoice

def playGame(currentGame):
    keepGoing = True
    while keepGoing:
        if currentNode == quit
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)
def playNode(game, nodeKey):
    currentNode = game[nodeKey]
    (description, menu1, node1, menu2, node2) = currentNode
    print(f"""{description}
    1: {menu1}
    2: {menu2}""")
    nodeChoice = input("1 or 2?")
    if nodeChoice.isnumeric():
        nodeChoice = int(nodeChoice)
        if nodeChoice == 1:
            newNode = node1
            currentNode = newNode
        else:
            newNode = node2
            currentNode = newNode
    else:
        print("Give me a number, pookie.")
    return currentNode
def getDefaultGame():
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
    print(game)
    outFile = open("adventureEditor.json", "w")
    json.dump(game, outFile)
    outFile.close()
    return game

