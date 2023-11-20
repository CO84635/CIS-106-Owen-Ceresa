file_path = "mybattingdata.txt"
def playerdata(file_path):
    playernames = []
    battingaverages = []

    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split(',')
            playernames.append(data[0])
            battingaverages.append(float(data[1]))

    return playernames, battingaverages

def displaypplayerdata(playernames, battingaverages):
    print("Player's Data:")
    for i in range(len(playernames)):
        print(f"Name: {playernames[i]}, Batting Averages: {battingaverages[i]}")

def searchplayerdata(playernames, battingaverages, searchname):
    for i in range(len(playernames)):
        if playernames[i] == searchname:
            return playernames[i], battingaverages[i]

playernames, battingaverages = playerdata("mybattingdata.txt")
displaypplayerdata(playernames, battingaverages)

r = str(input("Would you like to search a lastname? (Y/N): "))
while r == "Y":
    searchname = input("Please enter a lastname to search: ")
    searchedname, searchedaverage = searchplayerdata(playernames, battingaverages, searchname)

    print(f"Found that: {searchedname}, Batting Average: {searchedaverage}")

    r = str(input("Would you like to run this program again? (Y/N)"))