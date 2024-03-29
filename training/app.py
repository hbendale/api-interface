from backend import magic_numbers, day_calculator, employee
from fastapi import FastAPI


app = FastAPI()

data = employee.EmployeeDB()


@app.get("/")
async def _root():
    return "Hello and welcome to your deep dive session! You can find the tasks in the README under api-interface/training. Good luck!"

@app.get("/lucky_number/")
async def _lucky_number():
    """
    Task 1:
    
    GET /lucky_number/
    
    by calling this endpoint a response is expected like
    
    200 Your lucky number for the day is: 42
    
    consider using the backend feature 'magic_numbers.get_magic_number()'
    
    """
    return "Implement me!"



@app.get("/greetings/")
async def _greetings():
    """
    Task 2:
    
    GET /greetings/
    
    by calling this endpoint with a mandatory parameter 'name' a response is expected like
    
    200 Welcome DiveIn
    
    if the query parameter 'name' is omitted a status code 404 is expected
    
    """
    return "Implement me!"


@app.get("/weekday_calculator/")
async def _weekday_calculator():
    """
    Task 3:
    
    GET /weekday_calculator/
    
    by calling this endpoint with a mendatory header 'n' a response is expected like
    
    200 5 days from now is a Monday
    
    if the header 'n' is omitted a status code 422 is expected with some details on the missing header
    if the header 'n' is not a valid number a status code 422 is expected with some details on expected data type
    
    consider using the backend feature 'day_calculator.get_weekday_in_n_days(n)'
    
    """
    return "Implement me!"


def user_loader(username, password):
    user = {"DiveIn": "1234", "Chris":"hello"}

    # implement me

    return None


@app.get("/login/")
async def _login():
    """
    Task 4:
    
    GET /login/
    
    by calling this endpoint with the mandatory baseAuth header (username: DiveIn password: 1234) an response is expected like
    
    200 Login successful!
    
    if the baseAuth header is omitted a status code 401 is expected with some details on the missing baseAuth
    if no valid username and/or password are provided a status code 401 is expected with the hint that username/password is invalid
    
    consider implementing user_loader() with check for DiveIn:1234
    
    """
    return "Implement me!"


db = employee.EmployeeDB()
db.create(employee.Employee(name="Alice", age=20))
db.create(employee.Employee(name="Bob", age=42))
db.create(employee.Employee(name="Charles", age=50))


@app.get("/employee/")
async def _employee():
    """
    Read all
    
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
    
    """
    return "Implement me!"


@app.post("/employee/", response_model=employee.Employee)
async def _create_employee():
    """
    Create
    
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
        
    if the endpoint is called without payload a status code 422 is expected with some information on the needed payload
    if the key 'age' is not a valid int a status code 422 is expected with some information on the expexted data type
    
    consider using the backend feature 'db.create(employee=employee)'
    
    """
    return "Implement me!"


@app.get("/employee/{id}", response_model=employee.Employee)
async def _read_employee():
    """
    Read
    
    GET /employee/{id}
    
    by calling this endpoint with the 'id' a response is expected like
    
    200 {
            "id": 1,
            "name": "Alice",
            "age": 20
        }
        
    if the path parameter 'id' does not correspond to an id in the db a status code 404 is expected with some information that no resource for the id is found    
    
    consider using the backend feature 'db.read(id=id)'
    
    """
    return "Implement me!"
    
    
@app.put("/employee/{id}", response_model=employee.Employee)
async def _update_employee():
    """
    Update
    
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
        
    if the endpoint is called without payload a status code 422 is expected with some information on the needed payload
    if the path parameter 'age' or 'id' is not a valid int a status code 422 is expected with some information on the expected data type
    if the resource for the path parameter 'id' is not found in the backend a status code 404 is expected with some information on the missing resource
    
    consider using the backend feature 'db.update(id=id, employee=employee)'
    
    """
    return "Implement me!"


@app.delete("/employee/{id}", response_model=employee.Employee)
async def _delete_employeelogin():
    """
    Delete
    
    DELETE /employee/{id}
    
    by calling this endpoint with 'id' a response is expected like
    
    200 {
            "id": 4
            "name": "DiveIn",
            "age": 99
        }
        
    if the resource for the pathparameter 'id' is not found in the backend a status code 404 is expected with some information on the missing resource
    
    consider using the backend feature 'db.delete(id=id)'
    
    """
    return "Implement me!"