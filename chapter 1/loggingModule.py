# Libraries: logging

# Concepts: Setting up logging, different logging levels (INFO, ERROR, etc.), writing logs to files.

import logging

# Setting up logging
logging.basicConfig(
    level=logging.INFO,             # Set the logging level to INFO
    filename='app.log',             # Log messages will be saved to 'app.log'
    filemode='w',                   # Open the log file in write mode (overwrite existing content)
    format='%(name)s - %(levelname)s - %(message)s'  # Format of log messages
)

# Logging messages
logging.info('This is an info message')
logging.error('This is an error message')



# o/p => file => app.log
# ---
# root - INFO - This is an info message
# root - ERROR - This is an error message


