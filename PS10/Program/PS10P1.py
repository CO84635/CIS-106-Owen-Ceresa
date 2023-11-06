#Function for Next Months Sales
def NextMonthSales(month, sales):
    if month in ["Jan", "Feb", "Mar"]:
        forecast = 0.10
    elif month in ["Apr", "May", "Jun"]:
        forecast = 0.15
    elif month in ["Jul", "Aug", "Sep"]:
        forecast = 0.20
    elif month in ["Oct", "Nov", "Dec"]:
        forecast = 0.25
    else:
        forecast = 0.0

    next_sales = sales * (1 + forecast)
    return next_sales, forecast


r = input("Would you want to run this program? (Y/N): ")

while r == "Y":
    lastname = str(input("What is your last name?: "))
    month = str(input("What is the month? Ex: Jan, Feb, Mar: "))
    sales = float(input("What is the sales value?: "))
    next_sales, forecast = NextMonthSales(month, sales)
    print(f"Dear {lastname}, next months sales was calculated at ${next_sales} with a forecast percent of {forecast}")
    r = str(input("Would you like to run this program again?: "))
