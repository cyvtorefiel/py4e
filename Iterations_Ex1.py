#Computes, Counts, Averages

total = 0
count = 0
average = 0

while (True):
    num = input("Enter a number: ")
    if (num == "done"):
        if (count == 0):
            print(0, 0, 0)
            break
        else:
            print(total, count, average)
            break
    else:
        try:
            n = int(num)
        except:
            n = -1

        if (n > 0):
            total += n
            count += 1
            average = total/count
        else:
            print("Invalid input")
