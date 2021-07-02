import csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:nichinu123elon@localhost/flaskdemo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
   flights = Flight.query.all() # this is a list of all indivisual filghts(flight objects)
   for flight in flights:
       print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")
    


if __name__ == '__main__':
    with app.app_context():
        main()   

# SELECT * FROM flights; => Flight.query.all()         
