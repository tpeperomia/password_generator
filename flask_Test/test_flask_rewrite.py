from flask import Flask, render_template, request
import string
import random # change to secret
import bcrypt

#	Define flask app
app = Flask(__name__)

#	Define options for the password generation
options = list(string.ascii_letters + string.digits + string.punctuation)

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
    return ''.join(random.choice(options) for i in range(length))

def test_set(password, length):
    '''
        Function to test strength of password
            :param password: password to test
    '''

#   Create test sets for verifying strength of password with mix of characters
    letters = set(string.ascii_letters)
    numbers = set(string.digits)
    symbols = set(string.punctuation)

#   Create counter for testing function
    letters_test = 0
    numbers_test = 0
    symbols_test = 0

#   Turn password into set
    password_test = set(password)

#   Count chars in password
    for char in password_test:
        if char in letters:
            letters_test += 1
        elif char in numbers:
            numbers_test += 1
        else:
            symbols_test += 1

#   Test all chars are represented
    if (letters_test > 0 and numbers_test > 0 and symbols_test > 0):
        return
    else:
        return gen_password(length)

def hashed_word(password) :
    '''
        Function to salt and hash generate password
        :para password: Generated password
        :return hashed_password: Hashed password decoded
    '''
    b_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(b_password, salt)
    return hashed_password.decode('utf-8')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = request.form.get('length')
        to_hash = request.form.get('to_hash')

        valid_length = get_length(length)
        if valid_length:
            password = gen_pass(valid_length)
            password = test_set(password)
            hashed_password = None
            if to_hash == 'Y':
                hashed_password = hash_password(password)
            return render_template('result.html', password=password, hashed_password=hashed_password)

        return render_template('index.html', error="Invalid length. Please choose a number >= 14.")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)