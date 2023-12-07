import os
from flask import Flask, request, render_template
from lib.database_connection import *
from lib.person import *
from lib.peep import *
from peewee import *
from datetime import *

# Create a new Flask app
app = Flask(__name__)

# Define your Peewee database instance
db = PostgresqlDatabase(
    'chitter-challenge',  # Your database name
    user='rubyseresin',  # Your PostgreSQL username
    password='',  # Your PostgreSQL password
    host='localhost'  # Your PostgreSQL host
)

# Connect to the database
db.connect()
new_user = Person(name='barry', email='barry@example.com', password='password')
new_peep = Peep(content='First Peep!', user_id=1)
new_user.save()
new_peep.save()

# == Your Routes Here ==



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':

    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
