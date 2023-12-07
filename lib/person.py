from peewee import *

db = PostgresqlDatabase('chitter-challenge', user='rubyseresin', password='', host='localhost')

class Person(Model):
    name = CharField()
    email = CharField()
    password = CharField()
    logged_in = BooleanField(default=False)

    class Meta:
        database = db # This model uses the "people.db" database.