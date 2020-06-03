import logging
import logging.config
import app_config


def get_logger() -> object:
    logging.config.fileConfig(app_config.run_conf_data['LOGGER_CONFIG_FILE'])
    return logging.getLogger('python_logger')
