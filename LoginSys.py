users={"ahmed":1394,"ali":6078,"amr":9345}
username=(input("please enter your name: ")).lower()
password=int(input("please enter your password: "))
if username in users and users[username] == password:  
    print(username,"is logged in")  
else:  
     print("incorrect username or password")  
      
