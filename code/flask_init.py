from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError, Schema, fields, validate
import logging

db_obj = SQLAlchemy()

log = logging.getLogger('pythonLogger') # This handler comes from config>logger.conf

def create_app(flask_config):
    """Construct the core application."""
    log.info(flask_config)
    app = Flask(__name__, instance_relative_config=False)

    '''
    Code line --> 
    app.config.from_object('flask_config.DevelopmentConfig')
    goes to file flask_config.py and reads configuration class DevelopmentConfig
    '''
    app.config.from_object(flask_config)

    db_obj.init_app(app)

    with app.app_context():
        import flask_routes  # Import routes
        return app


'''To validate the input parameters'''
def some_custom_check(data):
    '''can be replaced with customized check'''
    if not data:
        raise ValidationError('some_custom_check for title failed')
class TitleValidator(Schema):
    '''https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html'''
    title = fields.Str(required=True, validate=[validate.Length(min=1, max=50), some_custom_check])

