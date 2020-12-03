revenue = float(input("Enter your company's revenue: "))
expenses = float(input("Enter your company's expenses: "))

profit = revenue - expenses

if profit > 0:
    print("Your company is in the positive!")
    print(f"Profit: {profit}")
    print(f"Efficiency: {profit/revenue:.2f}")
    employee_cnt = int(input("Enter your company's employee count: "))
    print(f"Profit per Employee: {profit/employee_cnt:.2f}")
elif profit < 0:
    print("Your company is in the negative!")
    print(f"Profit: {profit}")
elif profit == 0:
    print("Your company broke even!")
    print(f"Profit: {profit}")