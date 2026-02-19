annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = 0.25
annual_return = 0.04
down_payment = total_cost * portion_down_payment
current_savings = 0
monthly_return = annual_return / 12
months = 0
while current_savings < down_payment:
    months += 1
    current_savings += current_savings * monthly_return
    monthly_salary = annual_salary / 12
    current_savings += monthly_salary * portion_saved
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
print("Number of months:", months)
