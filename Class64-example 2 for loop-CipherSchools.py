#logic 
#num="1256"
#int(num[0])--->1
#int(num[1])---->2

total =0
num=(input("enter a number: "))
for i in range(0, len(num)):
    total +=int(num[i])
print(total)