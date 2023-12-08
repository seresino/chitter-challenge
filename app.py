import os
from flask import Flask, request, render_template, redirect, session, url_for
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
        peeps = (Peep
                .select(Peep, Person)
                .join(Person))
        for person in Person.select():
            if person.logged_in == True:
                print(f"this user_id is logged in: {person.id}")
                return redirect(url_for('get_account_page', id=person.id))
        return render_template('index.html', peeps=peeps)
    
    @app.route('/<int:id>', methods=['GET'])
    def get_account_page(id):
        person = Person.get(Person.id == id)
        peeps = (Peep
                .select(Peep, Person)
                .join(Person))
        return render_template('account.html', person=person, peeps=peeps)
    
    @app.route('/<int:id>', methods=['POST'])
    def post_account_page(id):
        person = Person.get(Person.id == id)
        content = request.form['content']
        post_time = datetime.now()
        peep = Peep(content=content, post_time=post_time, user_id=person.id)
        peep.save()
        return redirect(url_for('get_account_page', id=person.id))
    
    @app.route('/logout/<id>', methods=['POST'])
    def post_logout(id):
        try:
            person = Person.get(Person.id == id)
            person.logged_in = False
            person.save()  # Save the updated 'logged_in' status to the database
            print(f"this user_id is logged out: {person.id}, status: {person.logged_in}")
            peeps = (Peep
                .select(Peep, Person)
                .join(Person))
            return redirect(url_for('get_peeps'))
        except Person.DoesNotExist:
            print("User not found", "error")
        
    @app.route('/login', methods=['GET'])
    def get_login():
        return render_template('login.html')
    
    @app.route('/login', methods=['POST'])
    def post_login():
        email = request.form['email']
        password = request.form['password']
        try:
            persons = Person.select().where(Person.email == email)
            if password == persons[0].password:
                person = persons[0]
                person.logged_in = True
                person.save()  # Save the updated 'logged_in' status to the database
                return redirect(f"/{person.id}")
            person.save()
        except Person.DoesNotExist:
            print("User not found", "error")

        

    @app.route('/signup', methods=['GET'])
    def get_signup():
        return render_template('signup.html')
    
    @app.route('/signup', methods=['POST'])
    def post_person():
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        person = Person(name=name, email=email, password=password, logged_in=True)
        # if not person.is_valid():
        #     return render_template('index.html', person=person, errors=person.generate_errors()), 400
        person.save()

        return redirect(f"/{person.id}")

    
    # @app.route('/login', methods=['POST'])
    # def post_login():
    #     email = request.form['email']
    #     password = request.form['password']

    #     try:
    #         person = Person.get(Person.email == email, Person.password == password)
    #         session['user_id'] = person.id
    #         return redirect(url_for('get_peeps'))
    #     except Person.DoesNotExist:
    #         return "Invalid login credentials", 400



    # ...

    return app

# Create the Flask app using the create_app function
app = create_app()


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':

    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
