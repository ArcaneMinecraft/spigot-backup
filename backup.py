#!/usr/bin/env python3
import yaml
import logging
import tarfile
import time
import os
import shutil

logging.getLogger().setLevel(logging.INFO)

#Load config
config_file = "config.yaml"
mysql_config = "mysql.cnf"
config = {}
logging.info("Reading config")
with open(config_file, "r") as stream:
    try:
        config = (yaml.load(stream))
    except:
        print(exc)

#get stuff from config
backup_dir = config ["backup-dir"]
backup_name = config ["backup-name"]

dbs_to_backup = config["dbs-to-backup"]

server_root = config["server-root"] 
server_files = config["server-files-to-backup"]

#create backup filename using date format YYYY-MM-DD
backup_filepath = backup_dir + backup_name + "-" + time.strftime("%Y-%m-%d-%H") + ".tar.gz"
logging.info("Generating archive")
backup_tarball = tarfile.open(backup_filepath, "w:gz")

def wipe_directory (path_to_dir):
    shutil.rmtree (path_to_dir)
    os.makedirs (path_to_dir)

for db in dbs_to_backup:
    logging.info ("Dumping DB: " + db)
    db_backup_file_name = db + ".sql"
    export_db_command = "mysqldump --defaults-extra-file=" + mysql_config + " " + db + " > " + "tmp/" \
                        + db_backup_file_name  
    os.system(export_db_command)
    backup_tarball.add("tmp/" + db_backup_file_name, backup_name +  "/dbs/" + db_backup_file_name)

wipe_directory ("tmp/")
    
logging.info ("Backing up server files")
for server_file in server_files: 
    full_path = server_root + server_file
    backup_tarball.add(full_path, backup_name + "/server-files/" + server_file)
backup_tarball.close()

logging.info("Backup generated at: " + backup_filepath)
