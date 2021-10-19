x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
if (x < y):
    number = x
    BMM = y
else:
    number = y
    BMM = x
if (number == 0):
    print("K.M.M is not available. ")
else:
    for i in range(1,number):
        if (x % i == 0 and y % i == 0):
            BMM = i
    KMM = int((x * y) / BMM)
    print("K.M.M : ",KMM)
print("B.M.M : ", BMM)