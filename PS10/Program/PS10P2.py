r = input("Would you want to run this program? (Y/N): ")

def SquareFootage(length, width, height):
    square_footage = (2 * length * width) + (2 * length * height) + (2 * width * height)
    gallons = square_footage / 50

    return square_footage, gallons
while r == "Y":
    length = float(input("What is the length?: "))
    width = float(input("What is the width?: "))
    height = float(input("What is the height?: "))
    square_footage, gallons = SquareFootage(length, width, height)
    print(f"The square footage is {square_footage} and uses {gallons} gallons of paint)")
    r = str(input("Would you like to run this program again? (Y/N)"))