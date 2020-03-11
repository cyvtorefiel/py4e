#Computation of Pay Rate

#Asks for user input for hours
hours = input("Enter work hours: ")
try:
    h = int(hours)
except:
    h = -1

#If input is valid will continue
if (h > 0):
    #Asks for user input for rate
    rate = input("Enter work rate: ")
    try:
        r = int(rate)
    except:
        r = -1

    if (r > 0):
        #Converts hours and rate to float
        hours = float(hours)
        rate = float(rate)

        #Computes for pay rate
        if (hours>40):
            pay = (40*rate)+((hours-40)*15)
        else:
            pay = (hours*rate)

        #Prints the pay rate
        print("Pay rate: ", pay)

    else:
        print("Error, please enter numeric input")
        
#If input is invalid, will print
else:
    print("Error, please enter numeric input")
