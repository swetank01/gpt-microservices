from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
engine = create_engine('sqlite:///user.db', echo=True)  # SQLite database file
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))

Base.metadata.create_all(bind=engine)  # Create tables in the database

@app.route('/users', methods=['GET'])
def get_users():
    session = Session()
    users = session.query(User).all()

    user_list = []
    for user in users:
        user_dict = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        user_list.append(user_dict)

    return jsonify(user_list)

@app.route('/register', methods=['POST'])
def register_user():
    # Retrieve user details from request data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    session = Session()
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()

    return 'User registered successfully'

@app.route('/login', methods=['POST'])
def login_user():
    # Retrieve user credentials from request data
    username = request.json['username']
    password = request.json['password']

    session = Session()
    user = session.query(User).filter_by(username=username, password=password).first()

    if user:
        return 'Login successful'
    else:
        return 'Login failed'

if __name__ == '__main__':
    app.run(port=5000)
