# Problem Set 1b

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal : ")
)

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
        current_savings += (current_savings * r) / 12
        current_savings += monthly_salary * portion_saved
        if month % 6 == 0 and month > 0:
            monthly_salary += monthly_salary * semi_annual_raise
    return current_savings


annual_salary = 150000
print(calculate_current_savings(0.4411))

low = 0
high = 10000
portion_saved = ((low + high) / 2) / 10000
epsilon = 100
