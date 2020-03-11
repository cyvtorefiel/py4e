#Grade Equivalent

#Asks for user input
score = input("Enter score: ")
try:
    s = float(score)
except:
    s = -1

if (s >= 0.0 and s <= 1.0):
    if (s >= 0.9):
        print("A")
    elif (s >= 0.8):
        print("B")
    elif (s >= 0.7):
        print("C")
    elif (s >= 0.6):
        print("D")
    elif (s < 0.6):
        print("F")

else:
    print("Error, input is out of range or is not a numeric input")
