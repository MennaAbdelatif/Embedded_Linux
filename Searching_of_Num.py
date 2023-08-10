mylist = list(input("please enter list:"))
val= (input("please enter the number you are searching for:"))
count=0
for i in mylist:
    if i == val: 
        count +=1
print("This value repeated in the number "+str(count)+" times")
