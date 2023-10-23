def CompBattAvg(hits, atbats):
    battavg = hits / atbats

    return battavg

totalpcount = 0.0
r = input("Do you want to compute Batting Average? (y/n)")

while r == "y":
    lastname = str(input("What is your last name: "))
    hits = int(input("Enter hits:"))
    atbats = int(input("Enter At Bats: "))
    battavg = CompBattAvg(hits, atbats)
    totalpcount = totalpcount + 1
    print(f"Dear {lastname} your batting average was {battavg}")
    r = input("Do you want to compute batting average (y/n)")

print(f"Total players entered {totalpcount}")