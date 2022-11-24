from backend import magic_numbers, day_calculator, employee
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

data = employee.EmployeeDB()


@app.get("/")
async def _root():
    return "Hello World"

@app.get("/lucky_number/")
async def _lucky_number():
    """
    Task 1:
    
    GET /lucky_number/
    
    by calling this endpoint an response is expected like
    
    200 Your lucky number for the day is: 42
    
    consider using the backend feature 'magic_numbers.get_magic_number()'
    
    """
    return f"Your lucky number for the day is: {magic_numbers.get_magic_number()}"



@app.get("/greetings/{name}")
async def _greetings(name: str):
    """
    Task 2:
    
    GET /greetings/
    
    by calling this endpoint with a mandatory parameter 'name' an response is expected like
    
    200 Welcome DiveIn
    
    if the parameter 'name' is omitted a status code 404 is expected
    
    """
    return f"Welcome {name}"


@app.get("/weekday_calculator/")
async def _weekday_calculator(n: int):
    """
    Task 3:
    
    GET /weekday_calculator/
    
    by calling this endpoint with a mendatory header 'n' an response is expected like
    
    200 5 days from now is a Monday
    
    (if the header 'n' is omitted a status code 400 is expected with some details on the missing header)
    (if the header 'n' is not a valid float a status code 400 is expected with some details on expected data type)
    
    consider using the backend feature 'day_calculator.get_weekday_in_n_days(n)'
    
    """
    return f"{n} days from now is a {day_calculator.get_weekday_in_n_days(n)}"


def user_loader(username, password):
    user = {"DiveIn": "1234", "Chris":"hello"}

    if user.get(username):
        if password == user.get(username):
            return {'username': username}

    return None


@app.get("/login/")
async def _login(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Task 4:

    GET /login/
    
    by calling this endpoint with the mandatory baseAuth header (username: DiveIn password: 1234) an response is expected like
    
    200 Login successful!
    
    (if the baseAuth header is omitted a status code 401 is expected with some details on the missing baseAuth)
    if no valid username and/or password are provided a status code 401 is expected with the hint that username/password is invalid
    
    consider implementing user_loader() with check for DiveIn:1234
    
    """
    if user_loader(credentials.username, credentials.password):
        return "Login successful!"
        
    raise HTTPException(status_code=401, detail=f"No valid username/password!")


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
    return db.get_all()


@app.post("/employee/", response_model=employee.Employee)
async def _create_employee(employee: employee.Employee):
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

    (if the endpoint is called without payload a status code 400 is expected with some information on the needed payload)
    (if the key 'age' is not a valid int a status code 400 is expected with some information on the expexted data type)

    consider using the backend feature 'db.create(employee=employee)'
    
    """
    return db.create(employee=employee)


@app.get("/employee/{id}", response_model=employee.Employee)
async def _read_employee(id: int):
    """
    Read

    GET /employee/{id}

    by calling this endpoint with the 'id' a response is expected like

    200 {
            "id": 1,
            "name": "Alice",
            "age": 20
        }

    if the id does not correspond to an id in the db a status code 404 is expected with some information that no resource for the id is found    

    consider using the backend feature 'db.read(id=id)'
    
    """
    try:
        return db.read(id=id)
    except:
        raise HTTPException(status_code=404, detail=f"employee with id: {id} not found!")
    
    
@app.put("/employee/{id}", response_model=employee.Employee)
async def _update_employee(id: int, employee: employee.Employee):
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

    (if the endpoint is called without payload a status code 400 is expected with some information on the needed payload)
    (if the key 'age' or 'id' is not a valid int a status code 400 is expected with some information on the expexted data type )
    (if the resource for the key 'id' is not found in the backend a status code 404 is expected with some information on the missing resource)

    consider using the backend feature 'db.update(id=id, employee=employee)'
    
    """
    try:
        return db.update(id=id, employee=employee)
    except:
        raise HTTPException(status_code=404, detail=f"employee with id: {id} not found!")


@app.delete("/employee/{id}", response_model=employee.Employee)
async def _delete_employeelogin(id: int):
    """
    Delete

    DELETE /employee/{id}

    by calling this endpoint with 'id' a response is expected like

    200 {
            "id": 4
            "name": "DiveIn",
            "age": 99
        }

    if the resource for the header 'id' is not found in the backend a status code 204 is expected with some information on the missing resource

    consider using the backend feature 'db.delete(id=id)'
    
    """
    try:
        return db.delete(id=id)
    except:
        raise HTTPException(status_code=404, detail=f"employee with id: {id} not found!")