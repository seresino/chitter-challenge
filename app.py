import os
from flask import Flask, request, render_template
from lib.database_connection import *
from lib.person import *
from lib.peep import *
from peewee import *
from datetime import *

# Create a function to create and configure the Flask app
def create_app():
    app = Flask(__name__)

    # Define your Peewee database instance
    db = PostgresqlDatabase(
        'chitter-challenge',  # Your database name
        user='rubyseresin',  # Your PostgreSQL username
        password='',  # Your PostgreSQL password
        host='localhost'  # Your PostgreSQL host
    )

    # Initialize the database connection in the Flask app context
    @app.before_request
    def before_request():
        db.connect()

    @app.after_request
    def after_request(response):
        db.close()
        return response

    # Define your routes
    @app.route('/', methods=['GET'])
    def get_peeps():
        peeps = Peep.select()
        return render_template('index.html', peeps=peeps)
    

    return app

# Create the Flask app using the create_app function
app = create_app()


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':

    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
