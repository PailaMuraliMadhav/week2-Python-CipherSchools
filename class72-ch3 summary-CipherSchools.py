#if statement
name ="murali"
if name=="Murali"  or name=="murali":
    print("you are murali")
elif name=="Madhav" or name=="madhav":
    print("you are Madhav")
else:
    print("you are not murali or madhav")

#while
i=0
while i<10:
    print(i)
    i+=1

#for loop
for i in range(1,11,2):
    print(i)

#break keyword
for  i in range(1,11,2):
    if i==5:
        break
    print(i)

#continue
for i in range(1,11):
    if i==5:
        continue
    print(i)