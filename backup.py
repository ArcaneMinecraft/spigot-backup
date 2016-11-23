#!/usr/bin/env python3
import yaml
import logging
import tarfile
import time

logging.getLogger().setLevel(logging.INFO)

#Load config
config_file = "config.yaml"
config = {}
logging.info("Reading config")
with open(config_file, "r") as stream:
    try:
        config = (yaml.load(stream))
    except:
        print(exc)

#config info
server_root = config["server-root"] 

#Specify which files to backup
backup_files = config["paths-to-backup"]
backup_dir = config ["backup-dir"]
backup_name = config ["backup-name"]

#create backup filename using standard date format YYYY-MM-DD
backup_filepath = backup_dir + backup_name + time.strftime("%Y-%m-%d-%H") + ".tar.gz"
logging.info("Generating archive")
backup_tarball = tarfile.open(backup_filepath, "w:gz")

for backup_file in backup_files: 
    full_path = server_root + backup_file
    backup_tarball.add(full_path, backup_file)
backup_tarball.close()

logging.info("Backup generated at: " + backup_filepath)
