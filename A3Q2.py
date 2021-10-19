import random
n=0
n=int(input("Enter the size of array: "))
array=[]
for i in range(n):
    while(True):
        rnd=random.randint(-100,100)
        if rnd not in array:
            break
    array.append(rnd)
print(array)
