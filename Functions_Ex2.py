#Grade Equivalent

def computegrade(score):
    if (s >= 0.9):
        a = "A"
    elif (s >= 0.8):
        a = "B"
    elif (s >= 0.7):
        a = "C"
    elif (s >= 0.6):
        a = ("D")
    elif (s < 0.6):
        a = ("F")

    return a


#Asks for user input
score = input("Enter score: ")
try:
    s = float(score)
except:
    s = -1

if (s >= 0.0 and s <= 1.0):
    print(computegrade(s))
else:
    print("Error, input is out of range or is not a numeric input")
