import logging
import logging.config
import GlobalValues

def get_logger() -> object:
    logging.config.fileConfig(GlobalValues.run_conf_data['LOGGER_CONFIG_FILE'])
    return logging.getLogger('python_logger')