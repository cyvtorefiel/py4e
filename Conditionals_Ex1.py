#Computation of Pay Rate

#Asks for user input
hours = input("Enter work hours: ")
rate = input("Enter work rate: ")

#Converts hours and rate to float
hours = float(hours)
rate = float(rate)

#Computes for pay rate
if (hours > 40):
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
else:
    pay = (hours  * rate)

#Prints the pay rate
print("Pay rate: ", pay)
