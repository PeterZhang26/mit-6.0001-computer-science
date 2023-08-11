# Problem Set 1b

annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(
#     input("Enter the percent of your salary to save, as a decimal : ")
# )

# Known variables
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
months = 36


def calculate_current_savings(portion_saved):
    monthly_salary = annual_salary / 12
    current_savings = 0
    for month in range(36):
        current_savings += monthly_salary * portion_saved
        current_savings += (current_savings * r) / 12
        if month % 6 == 0 and month > 0:
            monthly_salary += monthly_salary * semi_annual_raise
    return current_savings

# Saving 100% of salary, more than down payment cost
if calculate_current_savings(1) >= total_cost * portion_down_payment:

    # Initial guess between 0-100% of monthly salary saved
    low = 0
    high = 10000
    portion_saved = ((low + high) / 2) / 10000
    epsilon = 100
    steps = 0

    while (
        abs(calculate_current_savings(portion_saved) - total_cost * portion_down_payment)
        >= epsilon
    ):
        if calculate_current_savings(portion_saved) > total_cost * portion_down_payment:
            high = portion_saved * 10000
            portion_saved = ((low + high) / 2) / 10000
        else:
            low = portion_saved * 10000
            portion_saved = portion_saved = ((low + high) / 2) / 10000
        steps += 1

    print(f"Best savings rate is: {portion_saved}")
    print(f"Steps in bisection search: {steps}")
    # Calculated savings is within $34 of total amount needed
    print(
        f"Based on the code completion, current savings after three years will be: {calculate_current_savings(portion_saved)}"
    )
else:
    print("It is not possible to pay the down payment in three years.")