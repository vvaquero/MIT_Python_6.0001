
# You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
# decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area,
# you realize you are going to have to save for several years before you can afford to make the down
# payment on a house. In Part A, we are going to determine how long it will take you to save enough
# money to make the down payment given the following assumptions:

def calculate_X_months_savings(months, test_portion_saved, annual_salary, semi_annual_raise=0.07, r=0.04):
    total_savings = 0

    for month in range(months):
        if month % 6 == 0 and month != 0:
            # update the salary rise:
            annual_salary = annual_salary * (1 + semi_annual_raise)

        # calculate new monthly savings
        monthly_salary = annual_salary / 12
        saved_per_month = monthly_salary * (test_portion_saved / 10000)
        additional_savings_per_month = total_savings * r / 12
        final_monthly_savings = saved_per_month + additional_savings_per_month

        # update total savings
        total_savings += final_monthly_savings

    return total_savings


annual_salary = 10000
total_cost = 1000000
semi_annual_raise = 0.07
num_max_months = 36
margin = 100
search_acc = 0.0001

# total_cost = float(input('Insert the house total cost: '))
# portion_saved = float(input('Insert the portion you save every month: '))
# annual_salary = float(input('Insert your annual salary: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

total_down = total_cost * portion_down_payment

low_value = 0
high_value = 10000
test_portion_saved = (high_value-low_value)//2
x_months_savings = calculate_X_months_savings(num_max_months, test_portion_saved, annual_salary)
print(x_months_savings)

num_bisec = 1
while (abs(x_months_savings - total_down) >= margin) and (num_bisec < 10000):
    if x_months_savings > total_down:
        # rate is too much for X months
        high_value = test_portion_saved
    else:
        # rate is too low
        low_value = test_portion_saved

    test_portion_saved = (high_value + low_value) // 2
    num_bisec += 1

    x_months_savings = calculate_X_months_savings(num_max_months, test_portion_saved, annual_salary)
    print(num_bisec, x_months_savings, test_portion_saved)


print(f'Best savings rate {test_portion_saved/10000}')
print(f'Steps in bisec search {num_bisec}')

