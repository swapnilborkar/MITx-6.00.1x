monthlyInterestRate = annualInterestRate/12
updatedbalance = balance
fixedPayment = 0

while updatedbalance > 0:
    fixedPayment += 10
    updatedbalance = balance
    month = 1

    while month <= 12 and updatedbalance > 0:
        updatedbalance -= fixedPayment
        interest = monthlyInterestRate * updatedbalance
        updatedbalance += interest
        month += 1
    updatedbalance = round(updatedbalance,2)
print("Lowest Payment:" + str(round(fixedPayment)))
