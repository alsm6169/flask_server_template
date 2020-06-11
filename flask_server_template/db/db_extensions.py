from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base

# global database object, it has yet NOT been initialized
db_obj = SQLAlchemy()

# produce our own MetaData object, not yet initialized
metadata = MetaData()

# base class for declarative class definitions
Base = automap_base()
