# Microservices With ChatGPT

### Env
- Using virtualenv

```
pip3 install virtualenv
virtualenv -p 3.10 env
source env/bin/activate
python3 --version
```

# User Service




## Usage

Certainly! Here are some example cURL commands to test the microservices:

1. User Service:
- User Registration:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"username":"john_doe","email":"john.doe@example.com","password":"123456"}' http://localhost:5000/register
  ```

- User Login:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"username":"john_doe","password":"123456"}' http://localhost:5000/login
  ```

2. Product Service:
- Get all products:
  ```bash
  curl http://localhost:5000/products
  ```

- Get a specific product (replace `{product_id}` with an actual product ID):
  ```bash
  curl http://localhost:5000/products/{product_id}
  ```

- Update a product (replace `{product_id}` with an actual product ID):
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name":"New Product Name","price":99.99}' http://localhost:5000/products/{product_id}
  ```

You can run these commands in a terminal or command prompt to interact with the microservices. Make sure to replace `{product_id}` with an actual product ID when testing the Product Service.

Note that these are basic cURL examples for demonstration purposes. In a real-world scenario, you may need to handle authentication, error cases, and provide more detailed information in the requests and responses.