import platform
import sys
from pathlib import Path

import main_config
from flask_init import create_app

# Global Initialization - BEGIN

# Global Initialization - END

# Main - START
print('platform.python_version(): ', platform.python_version())
print('sys.version: ', sys.version)
print('__name__: ', __name__)

if len(sys.argv) != 2:
    run_config_file = Path('../config/') / main_config.RUN_PARAMS_DEFAULT_FILENM
else:
    run_config_file = Path(sys.argv[1])

if main_config.set_run_config_map(run_config_file) == 1:
    print('unable to read configuration file, exiting')
    exit(1)
db_con_str = main_config.get_db_con_str()
# print('main_config.get_db_con_str(): ', db_con_str)

# Flask Code - BEGIN
"""App entry point."""

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
# Flask Code - END

# Main - END
