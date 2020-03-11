#Minimum and Maximum

def minimum(numbers):
    min = 0
    for i in numbers:
        if i < min:
            min = i
    return min

def maximum(numbers):
    max = 0
    for j in numbers:
        if j > max:
            max = j
    return max


total = 0
count = 0
numbers = set()
min_n = 0
max_n = 0

while (True):
    num = input("Enter a number: ")
    if (num == "done"):
        if (count == 0):
            print(0, 0, 0, 0)
            break
        else:
            print(total, count, min_n, max_n)
            break
    else:
        try:
            n = int(num)
        except:
            n = -1

        if (n >= 0):
            numbers.add(n)
            total += n
            count += 1
            #min_n = min(numbers)           //built-in min() function
            min_n = minimum(numbers)
            #max_n = max(numbers)           //built-in max() function
            max_n = maximum(numbers)

        else:
            print("Invalid input")
