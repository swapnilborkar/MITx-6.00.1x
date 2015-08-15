months = 13
total = 0.0

for i in range(1, months, 1):

    monthlyInterestRate = (annualInterestRate/12)
    minimumMonthlyPayment = monthlyPaymentRate * balance
    total = total + minimumMonthlyPayment
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    print "Month: " + str(i)
    print "Minimum monthly payment: " + "%.2f" % minimumMonthlyPayment
    print "Remaining balance: "+ str(round(balance, 2))
    if i==12:
        print("Total paid: " + str(round(total, 2)))
        break
print "Remaining balance: "+ str(round(balance, 2))