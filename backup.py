#!/usr/bin/env python3
import yaml
import logging
import os.path
import tarfile
import time
import ftplib

CONFIG_DIR = "myconfig.yaml"
config = {}

logging.getLogger().setLevel(logging.INFO)
logging.info("Reading config")

with open(CONFIG_DIR, "r") as stream:
    try:
        config = (yaml.load(stream))
    except:
        print(exc)

#config info
WORLD_DATA_PATH = os.path.join(config["server-root"], config["main-world-name"])
FTP_HOST = config["ftp-server-host"]
FTP_USER = config["ftp-server-host"]
FTP_PASSWORD = config["ftp-password"]

backup_files = [WORLD_DATA_PATH, WORLD_DATA_PATH + "_nether", WORLD_DATA_PATH + "_the_end"]

backup_filename = "arcane-daily-" + time.strftime("%Y-%m-%d-%H%M") + ".tar.gz"

backup_tarball = tarfile.open(backup_filename, "w:gz")
for backup_file in backup_files: 
    backup_tarball.add(backup_file, arcname=os.path.basename(backup_file))
backup_tarball.close()


