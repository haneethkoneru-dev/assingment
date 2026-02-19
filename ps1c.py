starting_salary = float(input("Enter the starting salary: "))
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
annual_return = 0.04
semi_annual_raise = 0.07
months = 36
epsilon = 100 
steps = 0
best_rate = None
def calculate_savings(rate):
    current_savings = 0
    annual_salary = starting_salary
    monthly_return = annual_return / 12
    for month in range(1, months + 1):
        monthly_salary = annual_salary / 12
        current_savings += current_savings * monthly_return
        current_savings += monthly_salary * rate
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
    return current_savings
if calculate_savings(1.0) < down_payment - epsilon:
    print("It is not possible to pay the down payment in three years.")
else:
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000
        savings = calculate_savings(rate)

        if abs(savings - down_payment) <= epsilon:
            best_rate = rate
            break
        elif savings < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    print("Best savings rate:", format(best_rate, ".4f"))
    print("Steps in bisection search:", steps)