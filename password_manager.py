master_pwd= input("What is the master password? ")

# function is an executable reusable line of code
def view():
    pass

def add():
    name= input ("Account Name: ")
    pwd = input ("Password: ")
# with automatically closes files for us better than file open wich requieres file.close()
# modes:w- overwrite, r-read a-append mode(adds or created new file )
# f is our file name
    with open ("password.txt", 'a') as f:
        f.write(name+""+pwd)

  
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
