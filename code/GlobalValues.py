import json
from timeit import default_timer

RUN_PARAMAS_DEFAULT_FILENM = 'run_params.json'
run_conf_data={}

def set_run_config_map(run_config_file):
    global run_conf_data
    try:
        with open(run_config_file) as fp:
            run_conf_data = json.load(fp)
    except IOError as err:
        print(err)
        return(1)
    return(0)