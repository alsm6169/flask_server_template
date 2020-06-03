import platform
import sys
from pathlib import Path
from flask import Flask, jsonify, make_response
from marshmallow import ValidationError
from flask_sqlalchemy import SQLAlchemy

import app_config
import Database_Pandas as dbp

# Global Initialization - BEGIN

# Global Initialization - END

# Main - START
print('platform.python_version(): ', platform.python_version())
print('sys.version: ', sys.version)
print('__name__: ', __name__)

if len(sys.argv) != 2:
    run_config_file = Path('../config/') / app_config.RUN_PARAMS_DEFAULT_FILENM
else:
    run_config_file = Path(sys.argv[1])

if app_config.set_run_config_map(run_config_file) == 1:
    print('unable to read configuration file, exiting')
    exit(1)

# Main - END

# Flask Code - BEGIN
app = Flask(__name__)
# goes to file flask_config.py and class DevelopmentConfig
app.config.from_object('flask_config.DevelopmentConfig')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return make_response(jsonify({'Error': 'URL NOT FOUND'}, 404))


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(jsonify({'Error': 'BAD REQUEST'}, 400))


@app.route('/module/v01/functions/actor_list', methods=['GET'])
def get_actor_list():
    try:
        print('inside actor_list')
        dbp.get_all_actors()
        actor_df = dbp.get_all_actors_df()
        response_code = 200
        response_msg = actor_df.to_json(orient='records')
    except ValidationError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    except RuntimeError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    return make_response(response_msg, response_code)

app.run()
# Flask Code - END

