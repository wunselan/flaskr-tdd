from app import db
from models import Flaskr


# Create the database and the DB table
db.create_all()

# Commit the changes
db.session.commit()
