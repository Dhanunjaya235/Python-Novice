# LOGGING IN PYTHON

#Using logging instead of print statements for exceptions

import logging

# Basic Configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

# Logging Levels
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# Logging Messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Logging Variables
name = 'Alice'
logging.info(f'{name} is a name')

# Logging Functions
def greet(name):
    return f'Hello, {name}!'
logging.info(greet('Bob'))

# Logging Exceptions
try:
    x = 1 / 0
except ZeroDivisionError:
    logging.error('Cannot divide by zero!')
