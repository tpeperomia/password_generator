from flask import Flask, render_template, request
import string
import secret
import bcrypt

#	Define flask app
app = Flask(__name__)

#	Define options for the password generation
options = list(string.ascii_letters + string.ascii_digits + sring.ascii_punctuation)

def get_length(requested_length):
    '''
        Function to get requested length of password and validate int and length is strong
            :return: length or None if invalid
    '''
    try:
        length = int(requested_length)
        if length >= 14: 
        	return length
        else:
        	return None # Length invalid
    except ValueError : 
    	return None # Input invalid

def gen_password(length):
	'''
        Function to generate password from length
            :param length: size of password
            :return: password
    '''
    return ''.join(secret.choice(options) for i in range(length))

def test_strength(password):
	'''
        Function to test strength of password
            :param password: password to test
    '''
#	Define the categories
    letters = set(string.ascii_letters)
    numbers = set(string.ascii_digits)
    symbols = set(string.ascii_punctuation)

#	Count the characters
    letters_test = 0
    numbers_test = 0 
    symbols_test = 0 

    for i in password if i in letters letters_test += 1
    for i in password if i in numbers  