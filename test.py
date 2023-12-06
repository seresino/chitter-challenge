# import peewee
import psycopg2
from peewee import Model, PostgresqlDatabase, CharField, IntegerField
from lib.person import *

# Replace the following with your PostgreSQL database connection details
db = PostgresqlDatabase('test', user='rubyseresin', password='', host='localhost')

# Replace the following with your PostgreSQL database connection details
db.connect()

# db.create_tables([Person])

new_person = Person.create(name='Jack Doe', age=25)

people_over_21 = Person.select().where(Person.age > 21)
for person in people_over_21:
    print(person.name, person.age)


db.close()