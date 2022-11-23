# Training
This repo hosts code for deep dive training session

## run application with
    uvicorn app:app --host 0.0.0.0 --port 8080 --reload
    
open /docs for UI
use Preview -> Preview Running Application to access the running webserver



# Task 1

    GET /lucky_number/

by calling this endpoint an response is expected like

    200 Your lucky number for the day is: 42

consider using the backend feature 'magic_numbers.get_magic_number()'



# Task 2
    
    GET /greetings/
    
by calling this endpoint with a mandatory parameter 'name' an response is expected like
    
    200 Welcome DiveIn
    
if the parameter 'name' is omitted a status code 404 is expected

usefull link for fastapi: https://fastapi.tiangolo.com/tutorial/path-params/



# Task 3:
    
    GET /weekday_calculator/
    
by calling this endpoint with a mendatory header 'n' an response is expected like
    
    200 5 days from now is a Monday
    
(if the header 'n' is omitted a status code 400 is expected with some details on the missing header)
(if the header 'n' is not a valid float a status code 400 is expected with some details on expected data type)
    
consider using the backend feature 'day_calculator.get_weekday_in_n_days(n)'

usefull link for fastapi: https://fastapi.tiangolo.com/tutorial/query-params/


# Task 4:

    GET /login/
    
by calling this endpoint with the mandatory baseAuth header (username: DiveIn password: 1234) an response is expected like
    
    200 Login successful!
    
(if the baseAuth header is omitted a status code 401 is expected with some details on the missing baseAuth)
if no valid username and/or password are provided a status code 401 is expected with the hint that username/password is invalid
    
consider implementing user_loader() with check for DiveIn:1234

usefull link for fastapi: https://fastapi.tiangolo.com/advanced/security/http-basic-auth/


# Task 5

consider using the 'db' to perform CRUD operations

## Read all

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

consider using the backend feature 'db.get_all()'
    

## Create

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

(if the endpoint is called without payload a status code 400 is expected with some information on the needed payload)
(if the key 'age' is not a valid int a status code 400 is expected with some information on the expexted data type)

consider using the backend feature 'db.create(employee=employee)'


## Read

    GET /employee/{id}

by calling this endpoint with the 'id' a response is expected like

    200 {
            "id": 1,
            "name": "Alice",
            "age": 20
        }

if the id does not correspond to an id in the db a status code 404 is expected with some information that no resource for the id is found    
consider using the backend feature 'db.read(id=id)'

## Update

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

(if the endpoint is called without payload a status code 400 is expected with some information on the needed payload)
(if the key 'age' or 'id' is not a valid int a status code 400 is expected with some information on the expexted data type )
(if the resource for the key 'id' is not found in the backend a status code 404 is expected with some information on the missing resource)

consider using the backend feature 'db.update(id=id, employee=employee)'


## Delete

    DELETE /employee/{id}

by calling this endpoint with 'id' a response is expected like

    200 {
            "id": 4
            "name": "DiveIn",
            "age": 99
        }

if the resource for the header 'id' is not found in the backend a status code 204 is expected with some information on the missing resource
consider using the backend feature 'db.delete(id=id)'