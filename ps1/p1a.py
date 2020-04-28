

# You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
# decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area,
# you realize you are going to have to save for several years before you can afford to make the down
# payment on a house. In Part A, we are going to determine how long it will take you to save enough
# money to make the down payment given the following assumptions:

annual_salary = 80000
portion_saved = 0.15
total_cost = 500000

# total_cost = float(input('Insert the house total cost: '))
# portion_saved = float(input('Insert the portion you save every month: '))
# annual_salary = float(input('Insert your annual salary: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

monthly_salary = annual_salary / 12
total_down_payment = total_cost*portion_down_payment
saved_per_month = monthly_salary * portion_saved




months_needed = 0
while current_savings <= total_down_payment:
    # sum a new month
    months_needed += 1

    # calculate new monthly savings
    additional_savings_per_month = current_savings * r / 12
    final_monthly_savings = saved_per_month + additional_savings_per_month

    # update total savings
    current_savings += final_monthly_savings

print(f'You would need {months_needed}  months to the get down payment of {portion_down_payment}')

