pwd= input("What is the master password? ")


while True:
    mode= input("Would you like to add a new password or view existing ones.Type view or add.Press Q to quit").lower()
    if mode == "q":
        break
    
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue
