import json
import os

RUN_PARAMS_DEFAULT_FILENM = 'run_params.json'
run_conf_data = {}
basedir = os.path.abspath(os.path.dirname(__file__))

def set_run_config_map(run_config_file):
    global run_conf_data
    try:
        with open(run_config_file) as fp:
            run_conf_data = json.load(fp)
    except IOError as err:
        print(err)
        return (1)
    return (0)

def get_db_con_str():
    # Example: 'postgresql://scott:tiger@localhost:5432/mydatabase'

    # without password
    # db_con_str = f'postgresql://' \
    #              f'{run_conf_data["DB_USER"]}' \
    #              f'@' \
    #              f'{run_conf_data["DB_SERVER"]}:' \
    #              f'{run_conf_data["DB_PORT"]}/' \
    #              f'{run_conf_data["DB_NAME"]}'

    # with password
    pwd = os.getenv('DB_PWD')  # get password from environment variable DB_PWD
    db_con_str = f'postgresql://' \
                 f'{run_conf_data["DB_USER"]}:' \
                 f'{pwd}@' \
                 f'{run_conf_data["DB_SERVER"]}:' \
                 f'{run_conf_data["DB_PORT"]}/' \
                 f'{run_conf_data["DB_NAME"]}'
    os.environ['SQLALCHEMY_DATABASE_URI'] = db_con_str
    return db_con_str


