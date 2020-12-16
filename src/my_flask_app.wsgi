import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/gileno/Documents/API/src')
from my_flask_app import app as application
application.secret_key = 'teste'
