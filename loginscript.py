loop = 'true'
while(loop=='true'):
    Username = raw_input("Enter Your Name:")
    Password = raw_input("Enter Your Password")
    if(Username=="Guest1" and Password=="Guest1"):
        print("You Logged In Successfull")+Username
        loop='false'
        loop1='true'
        while(loop1==true):
            command = raw_input(Username+"{} > > ")
            if(command=="exit" or command=="Exit"):
                break
            else:
                print command + " is not a valid command!"
     else:
         print('Invalid Credentials!');
