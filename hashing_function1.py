import bcrypt
import string
import random

#   Quick UI to get length and gen password
requested_length = input("How many characters do you need? ")
length = int(requested_length)
options = list(string.ascii_letters + string.digits + string.punctuation)
password = ''.join(random.choice(options) for i in range(length))


#   Turn string into byte string for bcrypt
b_password = password.encode('utf-8')

def hashing(b_password) :
    '''
        Function to salt and hash the password
        :para b_password: Generated raw password byte string
        :return hashed_password: Hashed password decoded 
    '''
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(b_password, salt)
    return hashed_password.decode('utf-8')

print(hashing(b_password))

'''
#   Test if password is same as hash
#   Quick UI to get attempt

to_check = input("What do you think your password is?")

def password_check(to_check) :
    
        Function to test if password is the same as hash
        :param to_check: password to check
        :return match: If the password matches the stored hash
    
    b_to_check = to_check.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_to_check = bcrypt.hashpw(b_to_check, salt)

    if hash_to_check == hashed_password : 
        print("You got it") 
    else :
        print("Try again")

password_check(to_check)
'''