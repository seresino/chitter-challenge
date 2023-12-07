from peewee import *
from lib.person import *
from datetime import *

db = PostgresqlDatabase('chitter-challenge', user='rubyseresin', password='', host='localhost')

class Peep(Model):
    content = CharField()
    post_time = DateTimeField(default=datetime.now)
    user_id = ForeignKeyField(Person, backref='peeps')
    

    class Meta:
        database = db # This model uses the "people.db" database.