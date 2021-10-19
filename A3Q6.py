array=input("Enter the array: ").split(" ")
l=len(array)
flag=True
for j in range(l):
    array[j]=int(array[j])
for i in range(l):
    if(i==l-1):
        break
    if(array[i]>array[i+1]):
        print("NO")
        flag=False
        break
if(flag==True):
    print("YES")