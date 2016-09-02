#!/usr/bin/env python3
import yaml

CONFIG_DIR = 'config/config.yaml'
config = {}

with open(CONFIG_DIR, 'r') as stream:
    try:
        config = (yaml.load(stream))
    except:
        print(exc)

