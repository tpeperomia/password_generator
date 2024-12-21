# 🔐 Random Password Generator (Flask + Python)
A lightweight Flask web app designed to experiment with Python modules while generating secure random passwords. This project explores secure password generation, hashing, and IP-based visitor location retrieval. This is my first project using Flask.

## 🚀 Features:
Secure Password Generation – Utilizes Python's secrets module to generate cryptographically secure random passwords.  
Customizable Password Length – Users can specify the desired number of characters for password generation.  
Security Check – Ensures the generated password meets security requirements before returning it.  
Salting and Hashing – Passwords can optionally be salted and hashed with bcrypt.  
Visitor Tracking – Uses requests to fetch the IP address from HTTP headers and retrieve location details. This data is not stored or logged just returned on the results page if inputs are suspicious.  

### 🛠️ Tech Stack:
Python – Core backend logic  
Flask – Lightweight web framework  
bcrypt – Secure hashing and salting  
requests – For HTTP requests and IP location lookup  
secrets – For cryptographically secure password generation  

### 📦 Installation:
``` bash
git clone https://github.com/yourusername/random-password-generator.git  
cd random-password-generator  
pip install -r requirements.txt  
python app.py  
```

### 🌐 Usage:
Visit the app in your browser at localhost:5000  
Enter the desired password length  
Choose whether to hash the password or return it as plaintext  
View the secure password and your approximate location  
