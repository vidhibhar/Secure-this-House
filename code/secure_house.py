#!/usr/bin/env python3
import sys


owner = sys.argv[1]
keys = sys.argv[2::1]
firefighterKey = "FIREFIGHTER_SECRET_KEY"
onlydoor = "LOCKED" 
peps = list()

while True:
    try:
        first = input().split()
    
        if(first[0] == "INSERT" and first[1] == "KEY"):
            #set user name and name of key equal to variables
            users = first[2] 
            keyPut = first[3] 
            
            print("KEY ", keyPut, " INSERTED BY ", users)
    
        elif(first[0] == "TURN" and first[1] == "KEY"):
            if(first[2] == users and (keyPut == "FIREFIGHTER_SECRET_KEY" or keyPut in keys)): 
                #prints success and unlocks door if user is the same and if key is valid 
                print("SUCCESS ", users, " TURNS KEY ", keyPut)
                onlydoor = "UNLOCKED"

            else: 
                print("FAILURE ", first[2], " UNABLE TO TURN KEY ", keyPut)
                
        elif(first[0] == "ENTER" and first[1] == "HOUSE"):
            if(onlydoor == "UNLOCKED" and first[2] == users ):
                #gives access to user if user is same door is already unlocked from before
                #then prints it and locks door again
                peps.append(users) #add person to list to store
                print("ACCESS ALLOWED")
                onlydoor = "LOCKED"
            else:
                print("ACCESS DENIED")

        elif(first[0] == "WHO'S" and first[1] == "INSIDE?"): 
            #if the list is 0 then prints no one is home
            if(len(peps) == 0):
                print("NOBODY HOME")
            else:
            #else it prints whoever is in the list
                print(", ".join(peps))

        elif(first[0] == "CHANGE" and first[1] == "LOCKS"):
            #checks is owner is in house and if the user wanting 
            # to change lock is owner. then keys are changed  
            if(owner in peps and first[2] == owner):
                print("OK")
                keys = first[3::1]
            else:
                #else the access is denied
                print("ACCESS DENIED")
        
        elif(first[0] == "LEAVE" and first[1] == "HOUSE"): 
            u = first[2]
            #if person is in the list then they are removed 
            if u in peps:
                print("OK")
                peps.remove(u)
            else:
                #or else not here is printed
                print(u," NOT HERE")

        else: 
            #prints error is none of the user input matches
            print("ERROR")
    
    #breaks error 
    except EOFError:
       break
