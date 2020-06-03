import os
import platform
import sys
from pathlib import Path
from flask import Flask, request, jsonify, make_response
from marshmallow import ValidationError

import GlobalValues

# Global Initialization - BEGIN
# Global Initialization - END

# Flask Code - BEGIN
app = Flask(__name__)
app.config['DEBUG'] = True

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'URL NOT FOUND'}, 404))

@app.route('/module/v01/functions/whatisthere', methods=['GET'])
def get_what_is_there():
    try:
        print('inside what_is_there')
        response_code = 200
        response_msg =jsonify({'OK': 'ALL GOOD'})
    except ValidationError as err:
        response_code = 400
        response_msg =jsonify(err.messages)
    except RuntimeError as err:
        response_code = err.code
        response_msg =jsonify(err.messages)
    return make_response(response_msg,response_code)
# Flask Code - END

#Main - START
print('platform.python_version(): ', platform.python_version())
print('sys.version: ', sys.version)
print('__name__: ', __name__)

if len(sys.argv) != 2:
    run_config_file = Path('../config/') / GlobalValues.RUN_PARAMAS_DEFAULT_FILENM
else:
    run_config_file = Path(sys.argv[1])

if GlobalValues.set_run_config_map(run_config_file) == 1:
    print('unable to read configuration file, exiting')
    exit(1)

app.run()
#Main - END