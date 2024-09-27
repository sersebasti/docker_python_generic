import os
import json

def get_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # acquisisco file di configurazione
    f = open(os.path.join(dir_path, 'conf.json'))
    conf_data = json.load(f)
    f.close()
    return conf_data
