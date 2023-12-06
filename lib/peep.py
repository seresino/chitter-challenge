from peewee import *

db = PostgresqlDatabase('test', user='rubyseresin', password='', host='localhost')

class Peep(Model):
    content = CharField()
    time = DateField()
    # user.id - foreign key to users: 
    

    class Meta:
        database = db # This model uses the "people.db" database.