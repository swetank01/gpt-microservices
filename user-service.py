from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
    # Code for user registration
    # Retrieve user details from request data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    # Save user to database or perform other necessary operations
    # ...

    return 'User registered successfully'

@app.route('/login', methods=['POST'])
def login_user():
    # Code for user authentication
    # Retrieve user credentials from request data
    username = request.json['username']
    password = request.json['password']

    # Perform authentication logic
    if username == 'john_doe' and password == '123456':
        authentication_successful = True
    else:
        authentication_successful = False

    if authentication_successful:
        return 'Login successful'
    else:
        return 'Login failed'

if __name__ == '__main__':
    app.run(port=5000)
