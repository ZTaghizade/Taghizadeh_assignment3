num=int(input("Enter the number: "))
snum=str(num)
pwr=len(snum)
cnd=0
i=0
while(True):
    x=int(snum[i])
    cnd=cnd+(x**pwr)
    if(cnd==num):
        print("YES")
        break
    if(cnd>num or i==pwr-1):
        print("NO")
        break
    else:
        i += 1
    