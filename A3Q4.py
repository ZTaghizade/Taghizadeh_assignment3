num=int(input("Enter the number: "))
i=1
res=1
while(True):
    res=res*i
    if(res==num):
        print("YES")
        break
    if(res>num):
        print("NO")
        break
    else:
        i += 1
