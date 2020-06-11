from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base
import logging
log = logging.getLogger('pythonLogger') # This handler comes from config>logger.conf

# global database object, it has NOT YET been initialized
db_obj = SQLAlchemy()

# produce our own MetaData object, it has NOT YET been initialized
metadata = MetaData()

# base class for declarative class definitions
Base = automap_base()


def orm_init():
    log.info('Binding metadata and reflecting the database')
    # IMPORTANT: Before first call to bind metadata to active db engine
    # see flask_routes.py @routes.before_app_first_request
    metadata.bind = db_obj.engine
    # Optional - BEGIN
    # we can reflect it ourselves from a database, using options
    # metadata.reflect(extend_existing=True,autoload_replace=True)
    # such as 'only' to limit what tables we look at...or reflect views also
    # metadata.reflect(only=['film', 'actor'], views=True, extend_existing=True, autoload_replace=True)
    # Optional - END
    # calling prepare() just sets up mapped classes and relationships
    Base.prepare(db_obj.engine, reflect=True)