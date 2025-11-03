x = input("enter password")
attempts = 0

while x != "metroid110":
    attempts += 1
    x = input("enter password:")
    if x == "metroid110":
        print("access granted")
        
        
    elif x == "mario110":
        print("sorry, that's an outdated password")
        
    
    else:
        print("wrong password")
    print(attempts)
