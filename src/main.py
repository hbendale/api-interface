from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask import request
import json
from flask import jsonify, make_response

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    country = db.Column(db.String(80))

    def __init__(self, id, name, age, country):
        self.id = id
        self.name = name
        self.age = age
        self.country = country


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods=['GET'])
def home_page():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/create_employee', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return "Server responded for GET request!"

    if request.method == 'POST':
        data = json.loads(request.data)
        id = data["id"]
        name = data['name']
        age = data['age']
        country = data['country']
        employee = EmployeeModel(id, name, age, country)
        db.session.add(employee)
        db.session.commit()
        return "POST Data received; Employee has been created successfully in the Database"

@app.route('/search_employee', methods=['GET'])
def RetrieveSingleEmployee():
    args = request.args
    id = args.get("id")
    employee = EmployeeModel.query.filter_by(id=id).first()
    data = dict()
    if employee:
        data[employee.id] = [employee.name, employee.age, employee.country]
    return make_response(jsonify(data), 200)

@app.route('/get_all_employees')
def RetrieveDataList():
    if request.method == 'GET':
        employees = EmployeeModel.query.all()
        if employees:
            data = dict()
            for employee in employees:
                data[employee.id] = [employee.name, employee.age, employee.country]
            return make_response(jsonify(data), 200)
        else:
            return "Database is empty"

@app.route('/update_employee/<int:id>', methods=['GET', 'POST'])
def update(id):
    # args = request.args
    # id = args.get("id")
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if employee:
            data = json.loads(request.data)
            if "name" in data.keys():
                employee.name = data['name']
            if "age" in data.keys():
                employee.age = data['age']
            if "country" in data.keys():
                employee.country = data['country']

            db.session.add(employee)
            db.session.commit()
            return "Employee Data updated successfully"
        else:
            return f"Employee with id = {id} Does not exist"

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'DELETE':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return "Employee data deleted"
        else:
            return "No Employee found!"
    return "Invalid request method! Please use DELETE method to delete Employee data."

app.run(host='0.0.0.0', port=5000)