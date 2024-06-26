# Training

This repo hosts code for deep dive training session

## setup app with

    pip install -r requirements.txt

## run application with

    uvicorn app:app --host 0.0.0.0 --port 8080 --reload

open <http://127.0.0.1:8080/docs> for UI
use Preview -> Preview Running Application to access the running webserver

---

## Task 1

    GET /lucky_number/

by calling this endpoint an response is expected like

    200 Your lucky number for the day is: 42

consider using the backend feature 'magic_numbers.get_magic_number()'

---

## Task 2

    GET /greetings/

by calling this endpoint with a mandatory parameter `name` an response is expected like (if `name` is set to DiveIn)

    200 Welcome DiveIn

if the query parameter 'name' is omitted a status code 404 is expected

usefull link for fastapi: <https://fastapi.tiangolo.com/tutorial/query-params/>

---

## Task 3

    GET /weekday_calculator/

by calling this endpoint with a mendatory header 'n' an response is expected like

    200 5 days from now is a Monday

if the header `n` is omitted a status code 422 is expected with some details on the missing header\
if the header `n` is not a valid number a status code 422 is expected with some details on expected data type

consider using the backend feature `day_calculator.get_weekday_in_n_days(n)`

usefull link for fastapi: <https://fastapi.tiangolo.com/tutorial/header-params/>

---

## Task 4

    GET /login/

by calling this endpoint with the mandatory baseAuth header (username: DiveIn password: 1234) a response is expected like

    200 Login successful!

if the baseAuth header is omitted a status code 401 is expected with some details on the missing baseAuth\
if no valid username and/or password are provided a status code 401 is expected with the hint that username/password is invalid

consider implementing `user_loader()` with check for DiveIn:1234 (username:password)

usefull link for fastapi: <https://fastapi.tiangolo.com/advanced/security/http-basic-auth/>

---

## Task 5

consider using the 'db' to perform CRUD operations

### Read all

    GET /employee/

by calling this endpoint a response is expected like

    200 [
          {
              "id": 1,
              "name": "Alice",
              "age": 20
          },
          {
              "id": 2,
              "name": "Bob",
              "age": 42
          },
          {
              "id": 3,
              "name": "Charles",
              "age": 50
          }
      ]

consider using the backend feature `db.get_all()`

---

### Create

    POST /employee/

by calling this endpoint with a payload like

    {
        "name": "DiveIn",
        "age": 42
    }

a response is expected like

    200 {
            "id": 4
            "name": "DiveIn",
            "age": 42
        }

if the endpoint is called without payload a status code 422 is expected with some information on the needed payload\
if the key 'age' is not a valid int a status code 422 is expected with some information on the expected data type

consider using the backend feature 'db.create(employee=employee)'

---

### Read

    GET /employee/{id}

by calling this endpoint with the 'id' a response is expected like

    200 {
            "id": 1,
            "name": "Alice",
            "age": 20
        }

if the path parameter 'id' does not correspond to an id in the db a status code 404 is expected with some information that no resource for the id is found\
consider using the backend feature 'db.read(id=id)'

usefull link for fastapi: <https://fastapi.tiangolo.com/tutorial/path-params/>

---

### Update

    PUT /employee/{id}

by calling this endpoint with a payload like

    {
        "id": 4
        "name": "DiveIn",
        "age": 99
    }

a response is expected like

    200 {
            "id": 4
            "name": "DiveIn",
            "age": 99
        }

if the endpoint is called without payload a status code 422 is expected with some information on the needed payload\
if the path parameter 'id' or key 'age' is not a valid int a status code 422 is expected with some information on the expected data type\
if the resource for the path parameter 'id' is not found in the backend a status code 404 is expected with some information on the missing resource

consider using the backend feature 'db.update(id=id, employee=employee)'

---

### Delete

    DELETE /employee/{id}

by calling this endpoint with 'id' a response is expected like

    200 {
            "id": 4
            "name": "DiveIn",
            "age": 99
        }

if the resource for the path parameter 'id' is not found in the backend a status code 404 is expected with some information on the missing resource

consider using the backend feature 'db.delete(id=id)'

---

## Introduction to Swagger

Here is some documentation which we would recommend you to read:

1. [What is OpenAPI?](https://swagger.io/docs/specification/about/)
2. [Basic Structure of swagger code](https://swagger.io/docs/specification/basic-structure/)
3. [Describing Request Body](https://swagger.io/docs/specification/describing-request-body/)
4. [Describing Responses](https://swagger.io/docs/specification/describing-responses/)
5. [Basic Authentication](https://swagger.io/docs/specification/authentication/basic-authentication/)
6. [AWS API Gateway Tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-tutorials.html)
7. [Azure API Gateway Tutorial](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish)
