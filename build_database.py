from config import db
from models import Person

# Data to initialize database with

PEOPLE = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny', 'lname': 'Easter'}
]

# Create the database

db.create_all()

# Iterate over the PEOPLE structure and populate the database

for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    db.session.add(p)

db.session.commit()
