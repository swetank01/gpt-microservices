# Database

-  Adding database integration to the microservices will enable you to store and retrieve data from a persistent storage solution. Here's an example of how you can integrate a SQLite database into the User Service:

Great! Adding database integration to the microservices will enable you to store and retrieve data from a persistent storage solution. Here's an example of how you can integrate a SQLite database into the User Service:

1. Install the necessary package:
   ```bash
   pip install sqlalchemy
   ```

2. Import the required modules and create a database connection in the User Service:

   ```python
   from flask import Flask, request
   from sqlalchemy import create_engine, Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   app = Flask(__name__)
   Base = declarative_base()
   engine = create_engine('sqlite:///user.db', echo=True)  # SQLite database file

   # Define the User model
   class User(Base):
       __tablename__ = 'users'

       id = Column(Integer, primary_key=True)
       username = Column(String(50), unique=True)
       email = Column(String(100), unique=True)
       password = Column(String(100))

   Base.metadata.create_all(bind=engine)  # Create tables in the database
   Session = sessionmaker(bind=engine)
   ```

3. Modify the user registration endpoint to save user data in the database:

   ```python
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
   ```

4. Update the user login endpoint to perform authentication against the database:

   ```python
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
   ```

With these modifications, the User Service will now store user data in a SQLite database. You can interact with the User Service's endpoints (`/register` and `/login`) to register users and perform login authentication, with the data being persisted in the `user.db` SQLite file.

You can adapt a similar approach to integrate a database into the Product Service by defining a model for products and performing CRUD operations accordingly.

Note: This is a simplified example using SQLite for demonstration purposes. In a real-world scenario, you might use a more robust database system like MySQL, PostgreSQL, or MongoDB, and handle more complex operations and error cases.