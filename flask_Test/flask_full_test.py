from flask import Flask, render_template, request
import string
import random
import bcrypt

app = Flask(__name__)

# Define global options for password generation
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
            return None  # Invalid length
    except ValueError:
        return None  # Invalid input

def gen_pass(length): 
    '''
        Function to generate password from length
            :param length: size of password
            :return: password
    '''
    return ''.join(random.choice(options) for _ in range(length))

def test_set(password):
    '''
        Function to test strength of password
            :param password: password to test
    '''
    letters = set(string.ascii_letters)
    numbers = set(string.digits)
    symbols = set(string.punctuation)

    letters_test = sum(1 for char in password if char in letters)
    numbers_test = sum(1 for char in password if char in numbers)
    symbols_test = sum(1 for char in password if char in symbols)

    if letters_test > 0 and numbers_test > 0 and symbols_test > 0:
        return password
    else:
        return gen_pass(length)

def hash_password(password):
    '''
        Function to salt and hash generated password
            :param password: Generated password 
            :return: hashed_password
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
