from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db_obj = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    '''
    Code line --> 
    app.config.from_object('flask_config.DevelopmentConfig')
    goes to file flask_config.py and reads configuration class DevelopmentConfig
    '''
    app.config.from_object('flask_config.DevelopmentConfig')

    db_obj.init_app(app)

    with app.app_context():
        import flask_routes  # Import routes
        return app
