# Assignment-2 - Paying Debt off in a Year
# Now write a program that calculates the minimum fixed monthly payment
''' writing a program for calculate the minimum fixed monthly payment'''
#needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month
# but instead is a constant amount that will be
# paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# The program should print out one line: the lowest monthly payment that will pay
# off all debt in under 1 year, for example:
# Lowest Payment: 180
# Assume that the interest is compounded monthly according to the balance at the
# end of the month (after the payment for that month is
# made).
# The monthly payment must be a multiple of $10 and is the same for all months.
# Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay. A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) +
# (Monthly interest rate x Monthly unpaid balance)
def calculate(month, bal, minimumpay, monthly_intrest_rate):
    '''calculate the remaining balance'''
    while month < 12:
        unpaid_bal = bal - minimumpay
        bal = unpaid_bal + (monthly_intrest_rate * unpaid_bal)
        month += 1
    return bal
def paying_debt(bal, annual_int_rate):
    '''paying the debt'''
    initial_balance = bal
    monthly_intrest_rate = annual_int_rate/12
    month = 0
    minimumpay = 10
    while calculate(month, bal, minimumpay, monthly_intrest_rate) > 0:
        bal = initial_balance
        minimumpay += 10
        month = 0
    print('lowestpayment:', minimumpay)
def main():
    ''' main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt(data[0], data[1]))
if __name__ == "__main__":
    main()