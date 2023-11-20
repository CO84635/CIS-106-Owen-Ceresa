def display_names(names):
    print("Lastnames: ")
    for name in names:
        print(name)

def display_names_reverse(names):
    print("LastNames in Reverse Order: ")
    for name in reversed(names):
        print(name)

last_names = ["Thompson", "Ceresa", "Hunt", "Batt", "Merlet", "Rymza", "Donlea", "Toniolo", "Dorion", "Haefs"]

display_names(last_names)

display_names_reverse(last_names)