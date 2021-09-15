import logging
import os
from datetime import datetime

version = '2.1.1'

# File work directory
WD = os.path.dirname(os.path.realpath(__file__))
TIMESTAMP = datetime.now().strftime("%y%m%d-%H%M%S")

# Initialize log
log = logging.getLogger("main_log")
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter("[%(asctime)s] - %(levelname)s: %(message)s"))
log.addHandler(ch)
