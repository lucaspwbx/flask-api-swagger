import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db_name = "conn_dev"

# creating connexion app instance
connex_app = connexion.App(__name__, specification_dir="swagger/")

# geting underlying flask instance
app = connex_app.app

# sql alchemy stuff
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://localhost/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create sql alchemy db instance
db = SQLAlchemy(app)

# initialize marshmallow
ma = Marshmallow(app)
