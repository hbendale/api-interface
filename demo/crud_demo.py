from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List



class Person(BaseModel):
    name: str
    age: int
    country: str = None

class PersonRepresentation(BaseModel):
    id: int
    person: Person

class Data():
    persons: List[Person] = []
    
    def __init__(self) -> None:
        self.persons.append(Person(name="Alice", age=20, country="Germany"))
        self.persons.append(Person(name="Bob", age=42))
        
    def get_all(self) -> List[PersonRepresentation]:
        res : List[PersonRepresentation] = []
        for person in self.persons:
            res.append(PersonRepresentation(id=self.persons.index(person), person=person))
        return res
        
    def create(self, person: Person) -> PersonRepresentation:
        if person in self.persons:
            raise ValueError()

        self.persons.append(person)
        return PersonRepresentation(id=self.persons.index(person), person=person)
        
    def read(self, id: int) -> PersonRepresentation:
        return PersonRepresentation(id=id, person=self.persons[id])
        
    def update(self, id: int, person: Person) -> PersonRepresentation:
        self.persons[id] = person
        return PersonRepresentation(id=id, person=self.persons[id])
        
    def delete(self, id: int) -> PersonRepresentation:
        return PersonRepresentation(id=id, person=self.persons.pop(id))
        

app = FastAPI()

data = Data()

@app.get("/")
async def _root():
    return {
        "message": "welcome! use /docs for swagger UI",
        "persons": data.get_all()
    }
    


@app.put("/create/", response_model=PersonRepresentation)
async def _create(person: Person):
    try:
        return data.create(person=person)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"person already exists")
        
@app.get("/read/{id}", response_model=PersonRepresentation)
async def _read(id: int):
    try:
        return data.read(id=id)
    except:
        raise HTTPException(status_code=404, detail=f"no person found for id: {id}")
    
    
@app.patch("/update/{id}", response_model=PersonRepresentation)
async def _update(id: int, person: Person):
    try:
        return data.update(id=id, person=person)
    except:
        raise HTTPException(status_code=404, detail=f"no person found for id: {id}")
    
@app.delete("/delete/{id}", response_model=PersonRepresentation)
async def _delete(id: int):
    try:
        return data.delete(id=id)
    except:
        raise HTTPException(status_code=404, detail=f"no person found for id: {id}")