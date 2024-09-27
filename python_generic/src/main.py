from collections import defaultdict
import datetime
from datetime import datetime, timedelta, timezone
from errno import errorcode
from io import StringIO
import re
import pandas as pd
import matplotlib.pyplot as plt
import os
import os
import json
import mysql.connector
import pytz
import ssl


# acquisico cartella corrente
script_dir = os.path.dirname(os.path.abspath(__file__))

# acquisisco configurazione
f = open(os.path.join(script_dir, './conf/conf.json'))
conf_data = json.load(f)
f.close()


print(conf_data)

# acquisisco filepath login.log
# file_path = os.path.join(script_dir, conf_data['files']['inputsDir'],conf_data['files']['loginLogFilename'])