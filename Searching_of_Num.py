Num = (input("please enter number:"))
val= (input("please enter the number you are searching for:"))
count=0
for i in range(len(Num)):
    if Num[i]==val: 
        count=count+1
print("This value repeated in the number "+str(count)+" times")
