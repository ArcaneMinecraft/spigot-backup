#!/usr/bin/env python3
import yaml
import logging
import os.path
import tarfile
import time
import paramiko


logging.getLogger().setLevel(logging.INFO)

#Load config
CONFIG_DIR = "myconfig.yaml"
config = {}
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
FTP_PORT = config["ftp-port"]
REMOTE_PATH =  config["remote-path"]

#Specify which files to backup
backup_files = [WORLD_DATA_PATH, WORLD_DATA_PATH + "_nether", WORLD_DATA_PATH + "_the_end"]

#create backup filename using standard date format YYYY-MM-DD
backup_filepath = "backups/arcane-daily-" + time.strftime("%Y-%m-%d-%H") + ".tar.gz"

logging.info("Generating archive")
backup_tarball = tarfile.open(backup_filepath, "w:gz")
for backup_file in backup_files: 
    backup_tarball.add(backup_file, arcname=os.path.basename(backup_file))
backup_tarball.close()


#setup SFTP connection with paramiko module
transport = paramiko.Transport((FTP_HOST, FTP_PORT))
transport.connect(username = FTP_USER, password = FTP_PASSWORD)

sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put(backup_filepath)
