import string
import random

#	Test line
length = 3

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
		print('Success')
	else:
		print('fail')
		return gen_pass(length)

#	Logic
password = gen_pass(length)

while True: 
	result = test_set(password)
	if result:
		password = result 
	else: 
		break

print(f'Here is your password {password}')