#anliu
import os,configparser
#from conf import vm_config
from core import LogHandler

configer = configparser.ConfigParser()
configer.read(os.path.join("/opt/vmcreat2/conf","vm_config.conf"))
#print(configer.get("conf","src_conf_path"))

def create_dir(section,key):
    os.makedirs(configer.get(section, key))
    LogHandler.logger.error("%s Directory created successfully..." % configer.get("conf", dir))

def judge_path(section,key):
    if os.path.isdir(configer.get(section,key)):
        LogHandler.logger.debug("%s directory already exists... "%configer.get("conf","src_conf_path"))

    else:
        create_dir(section,key)

def main():
    #judge config of src
    judge_path("conf","src_conf_path")
    #judge config of det
    judge_path("conf","det_conf_path")
    #judge_image of src
    judge_path("image","src_image_path")
    #judge image of det
    judge_path("image","det_image_path")
    #judge db of path
    judge_path("db","db_path")

    return 1