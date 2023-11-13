def ComputeCommission(sales):
    if sales > 100000.00:
        CommissionRate = 0.10
    elif sales < 100000.00:
        CommissionRate = 0.05
    Commission = sales * CommissionRate
    NextYrTarget = 0.05 * sales

    return Commission, NextYrTarget

lastname = str(input("What is your lastname?: "))
sales = float(input("What is the sales?: "))
Commission, NextYrTarget = ComputeCommission(sales)
print(f"Dear {lastname}, your commision is {Commission} & next year's target is {NextYrTarget} ")
