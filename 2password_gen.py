#imported modules
import string
import secrets

#User interface to request test password length
def get_length():
    requested_length = input("How many characters do you need? ")
    
#test input is int and convert
    try : 
        int(requested_length)
        length = int(requested_length)

#test for secure password length
        validation = False if length < 14 else True
        if validation == False :
            print("A 14 character password will take a hacker more than a million years to crack! Give them a hard time and increase your choice.")
            get_length()
        else : 
            print("Great, here is you password: ")
            options = list(string.ascii_letters + string.digits + string.punctuation)
            password = ''.join(secrets.choice(options) for i in range(length))
            print(password)

    except : 
        print("Input is not valid, please use only numbers.") 
        get_length()

get_length()

