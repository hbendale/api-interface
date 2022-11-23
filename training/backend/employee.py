from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    id: int = None
    name: str
    age: int


class EmployeeDB:
    db: List[Employee] = []
    index: int = 0

    def create(self, employee: Employee) -> Employee:
        self.index += 1
        item = Employee(id=self.index, name=employee.name, age=employee.age)
        self.db.append(item)

        return item

    def read(self, id: int) -> Employee:
        for item in self.db:
            if item.id == id:
                return item

        raise ValueError(f"employee with id {id} not found!")

    def update(self, id: int, employee: Employee) -> Employee:
        for item in self.db:
            if item.id == id:
                index = self.db.index(item)
                employee.id = id
                self.db[index] = employee
                return employee
                
        raise ValueError(f"employee with id {employee.id} not found!")

    def delete(self, id: int) -> Employee:
        for item in self.db:
            if item.id == id:
                index = self.db.index(item)
                
                return self.db.pop(index)

        raise ValueError(f"employee with id {id} not found!")

    def get_all(self):

        return self.db