#anliu

import shutil,os
import logging.config

logging.config.fileConfig('./conf/logging.conf')
logger = logging.getLogger("simpleExample")

# Copy ansible configuration file to working directory
if not os.path.isdir("./data/ansible"):
    shutil.copytree("/etc/ansible/","./data/ansible")
else:
    logger.debug("create ./data/ansible exist")
