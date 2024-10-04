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
            print(game)
            userChoice = getMenuChoice()
        elif userChoice == 2:
            loadGame("game.json")
            print("Loaded game.")
            userChoice = getMenuChoice()
            
        elif userChoice == 3:
            print("Save game.")
            saveGame(game)
            userChoice = getMenuChoice()
            
        elif userChoice == 4:
            print("Edit or add a node")
            editNode(game)
            userChoice = getMenuChoice()
            
        elif userChoice == 5:
            print("Play current game.")
            playGame(game)
            userChoice = getMenuChoice()
            
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
    print(json.dumps(currentGame, outFile, indent=2))
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

def editNode(game):
    """lists all current node content. gets node name. return edited newNode"""
    print("Current status of game:")
    print(json.dumps(game, indent=2))
    print("Existing node names: ")
    for nodeName in game.keys():
        print(f" {nodeName}")
    newNodeName = input("Name of node to edit or create?")
    if newNodeName in game.keys():
        newContent = game[newNodeName]
    else:
        newContent = ["","","","",""]
    (desc, menu1, node1, menu2, node2) = newContent
    newDesc = editField("description", desc)
    newMenu1 = editField("Menu 1", menu1)
    newNode1 = editField("Node 1", node1)
    newMenu2 = editField("Menu 2", menu2)
    newNode2 = editField("Node 2", node2)
    
    game[newNodeName] = [newDesc, newMenu1, newNode1, newMenu2, newNode2]
    
    return game

def editField(prompt, currentVal):
    """gets a field name
       print field current value
       if user presses 'enter' immediately-retain current value
       otherwise: use new value"""
    newVal = input (f"{prompt} ({currentVal}): ")
    if newVal == "":
        newVal = currentVal
    
    return newVal
    
main()