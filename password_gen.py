#imported modules
import string
import secrets

#User interface to request test password length
requested_length = input("How many characters do you need? ")
length = int(requested_length)

#test for secure password length
validation = False if length < 10 else True
if validation == True :
    print("Great, here is you password: ")
else : 
    print("Input is not valid, please use only numbers and more than 10.")
    requested_length

#create list of random options (letteres/int/symbols)
options = list(string.ascii_letters + string.digits + string.punctuation)

#create password
password = ''.join(secrets.choice(options) for i in range(length))

print(password)

