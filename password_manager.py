from cryptography.fernet import Fernet

#we have already created the key
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)


def load_key():
    file = open ("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd= input("What is the master password? ")

key = load_key() + master_pwd.encode()
fer= Fernet(key)

# key + password + text to encrypt = random text
# randomtext + key + password = text to encrypt
# function to store a key  and function to retreive a key.



# function is an executable reusable line of code
def view():
     with open ("password.txt", 'r') as f:
        # create a loop through the  lines of the file
        for line in f.readlines():
        # strip the carage return from our line wth rstrip()
             data =line.rstrip()
        #using the .split()
        user, passw = data.split("|")
        print("User:", user, "Password:",fer.decrypt(passw.encode()).decode())


def add():
    name= input ("Account Name: ")
    pwd = input ("Password: ")
# with automatically closes files for us better than file open wich requieres file.close()
# modes:w- overwrite, r-read a-append mode(adds or created new file )
# f is our file name
    with open ("password.txt", 'a') as f:
        f.write(name+"|"+ fer.encrypt(pwd.encode()).decode() + "\n")

  
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
