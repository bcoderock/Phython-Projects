pwd= input("What is the master password? ")

# function is an executable reusable line of code
def view():
    pass

def add():
    pass

while True:
    mode= input("Would you like to add a new password or view existing ones.Type view or add.Press Q to quit").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
