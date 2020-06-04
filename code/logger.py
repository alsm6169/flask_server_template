import logging
import logging.config
import main_config


def get_logger() -> object:
    logging.config.fileConfig(main_config.run_conf_data['LOGGER_CONFIG_FILE'])
    return logging.getLogger('python_logger')
