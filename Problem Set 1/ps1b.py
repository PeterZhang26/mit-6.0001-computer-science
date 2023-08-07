# Problem Set 1b

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal : "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

monthly_salary = annual_salary/12
months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += (current_savings * r)/12
    current_savings += monthly_salary * portion_saved
    if months %6 == 0 and months > 0:
        monthly_salary += monthly_salary * semi_annual_raise
    months += 1

print(f"Number of months: {months}")