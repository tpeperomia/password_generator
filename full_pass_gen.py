#	Imported modules - using random for python tutor - change!
import string
import random
import bcrypt

#	UI to get length
requested_length = input("How many characters do you need? ")

def get_length(requested_length):

	'''
		Function to get requested length of password and validate int and length is strong
			:return: length
	'''
	try:
		int(requested_length)
		length = int(requested_length)

#	Test for secure password length
		validation = length >= 14
		if validation == True:
			return length
		else:
			print("A 14 character password will take a hacker more than a million years to crack! Give them a hard time and increase your choice.")
			new_length = input("How many characters do you need? ")
			return get_length(new_length)

#	Test gened password is int
	except ValueError:
		print("Input is not valid, please use only numbers.")
		new_length = input("How many characters do you need? ")
		return get_length(new_length) 

length = get_length(requested_length)

#	Create password options
options = list(string.ascii_letters + string.digits + string.punctuation)

def gen_pass(length): 
	'''
		Function to generate password from length
			:param length: size of passwrod
			:return: password
	'''
	return ''.join(random.choice(options) for i in range(length))

def test_set(password):
	'''
		Function to test strength of password
			:param password: password to test
	'''

#	Create test sets for verifying strength of password with mix of characters
	letters = set(string.ascii_letters)
	numbers = set(string.digits)
	symbols = set(string.punctuation)

#	Create counter for testing function
	letters_test = 0
	numbers_test = 0 
	symbols_test = 0  

#	Turn password into set 
	password_test = set(password)

#	Count chars in password
	for char in password_test:
		if char in letters:
			letters_test += 1
		elif char in numbers:
			numbers_test += 1
		else: 
			symbols_test += 1

#	Test all chars are represented
	if (letters_test > 0 and numbers_test > 0 and symbols_test > 0):
		return
	else:
		return gen_pass(length)

#	Call test on generated password
password = gen_pass(length)

while True: 
	result = test_set(password)
	if result:
		password = result 
	else: 
		break

print(f'Here is your password: {password}')


def hash(password) :
	'''
		Function to salt and hash generate password
		:para password: Generated password 
		:return hashed_password: Hashed password decoded 
	'''
	b_password = password.encode('utf-8')
	salt = bcrypt.gensalt()
	hashed_password = bcrypt.hashpw(b_password, salt)
	return hashed_password.decode('utf-8')


#	Check to hash or not
to_hash = input("Do you want to hash that password for safe storage? Y/N ")

if to_hash == "Y" :
	print(hash(password))
elif to_hash == "N" : 
	print("Store it safe then!")
else :
	new_to_hash = input("Not sure what you mean, please select Y or N: ")
	if new_to_hash == "Y" :
		print(hash(password))
	else : 
		print("Store it safe then!")


