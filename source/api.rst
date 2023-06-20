API Documentation
=================

.. currentmodule:: user_service

/register
----------

.. http:post:: /register

   Register a new user.
   **CURL**
   
   .. sourcecode:: http

      {
          "username": "john",
          "email": "john@example.com",
          "password": "password123"
      }
   **Request**
   
   .. sourcecode:: http

      POST /register HTTP/1.1
      Host: example.com
      Content-Type: application/json

      {
          "username": "john",
          "email": "john@example.com",
          "password": "password123"
      }

   **Response**
   
   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: text/plain

      User registered successfully.


/login
------

.. http:post:: /login

   Login a user.

   **Request**
   
   .. sourcecode:: http

      POST /login HTTP/1.1
      Host: example.com
      Content-Type: application/json

      {
          "username": "john",
          "password": "password123"
      }

   **Response**
   
   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: text/plain

      Login successful.

   .. sourcecode:: http

      HTTP/1.1 401 Unauthorized
      Content-Type: text/plain

      Login failed.
