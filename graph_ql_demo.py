import strawberry

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from strawberry.fastapi import GraphQLRouter



@strawberry.type
class Person:
    name: str
    age: int
    country: str

@strawberry.type
class PersonRepresentation:
    id: int
    person: 'Person'

persons: List[Person] = []

persons.append(Person(name="Alice", age=24, country="Germany"))
persons.append(Person(name="Bob", age=42, country= "Switzerland"))

def get_persons(root) -> "Person":
    return persons


    
@strawberry.type
class Query:
    persons: List[Person] = strawberry.field(resolver=get_persons)
    
@strawberry.type
class Mutation:
    @strawberry.field
    def create_person(self, name: str, age: int, country: str) -> Person:
        person = Person(name=name, age=age, country=country)
        persons.append(person)
        return Person(name=name, age=age, country=country)
    
    @strawberry.field
    def remove_person(self, name: str) -> Person:
        for person in persons:
            if person.name == name:
                persons.remove(person)
                return person
        return None

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")