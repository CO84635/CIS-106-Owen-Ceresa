#Dl1
def dl1 (mylist):
    n = int(input("Number of items for your list"))
    for n in range(0,n,1):
        s = int(input("Enter an integer"))
        mylist.append(s)
    return mylist
def displaylist(mylist):
    for item in mylist:
        print(item)

#main
mylist = []
mylist = dl1(mylist)
displaylist(mylist)
print(mylist)
#Dl2
mylist.insert(0,99)
print(mylist)
#Dl3
mylist[0] = 100
print(mylist)
#Dl4
mylist2 = [500, 600, 700, 800, 900]
mylist.extend(mylist2)
print(mylist)
#Dl5
mylist.remove(800)
print(mylist)
#Dl6
mylist.pop(2)
print(mylist)
#Dl7
grades =  ["A", "B", "C", "A", "A", "C"]
#Dl8
count_of_A = grades.count("A")
print("Number of A grades was:", count_of_A)
#Dl9
position_of_B = grades.index("B")
print("Position of the first B grade:", position_of_B)
#DL10
if "F" in grades:
    Finding_F = grades.index("F")
    print("Position of the first F Grade: ", Finding_F)
else:
    print("The Grade F is not in the list.")
#DL11
mylist2.clear()
print("Cleared list 2: ", mylist2)
#DL12
del mylist2
print(mylist2)
#Dl13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
#Dl14
sort_players = sorted(players)
print(sort_players)
#Dl15
players2 = players.copy()
print(players2)
#Dl16
players2.reverse()
print("Regular player list:", players)
print("Reversed player list", players2)
