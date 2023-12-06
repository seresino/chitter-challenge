from peewee import *

db = PostgresqlDatabase('chitter-challenge', user='rubyseresin', password='', host='localhost')

class Person(Model):
    name = CharField()
    username = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.