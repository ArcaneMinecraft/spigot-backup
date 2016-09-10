!/usr/bin/env python3
import yaml
import logging
import os.path

CONFIG_DIR = 'config.yaml'
config = {}

logging.getLogger().setLevel(logging.INFO)
logging.info("Reading config")

with open(CONFIG_DIR, 'r') as stream:
    try:
        config = (yaml.load(stream))
    except:
        print(exc)

WORLD_DATA_PATH = os.path.join(config['server-root'], 'Main')
print (WORLD_DATA)



