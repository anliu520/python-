#anliu

'''
Handle of log file to obtain log mode.
'''
import logging.config
import os

logging.config.fileConfig(os.path.join("/opt/vmcreat2/conf","logging.conf"))
logger = logging.getLogger("simpleExample")