import os
from ConfigParser import ConfigParser

def config(path='/etc/ameh.ini'):
    if not os.path.isfile(path):
        raise RuntimeError("Config file not found: '%s'" % path)

    conf = ConfigParser()
    conf.read(path)
    return conf

