#anliu
'''
main
'''
import os,sys,json,logging.config
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import vm_config
from core import vmcreate,JudgePath

logging.config.fileConfig(os.path.join("/opt/vmcreat2/conf","logging.conf"))
logger = logging.getLogger("simpleExample")

message = {
    "vm_name":None,
    "vm_type":None,
    "vm_cpu_max":None,
    "vm_cpu_curr":None,
    "vm_mem_max":None,
    "vm_mem_curr":None,
    "vm_vnc_port":None,
}

def interactive():
    '''
    The function is to realize the user interaction and
     make the information submitted by the user persistent.
    :return:
    '''

    message["vm_name"] = input("vm_name:")
    message["vm_type"] = input("vm_type:")
    message["vm_cpu_max"] = input("vm_cpu_max:")
    message["vm_cpu_curr"] = input("vm_cpu_curr:")
    message["vm_mem_max"] = 1024*1024*int(input("vm_mem_max:"))
    message["vm_mem_curr"] = 1024*1024*int(input("vm_mem_curr:"))
    message["vm_vnc_port"] = input("vm_vnc_port:")


    with open(os.path.join(vm_config.db["db_path"],message["vm_name"]),"w",encoding="utf-8") as f1:
        json.dump(message,f1)


def create_pross():
    label1 = vmcreate.copy_vm_conf(message["vm_type"], message["vm_name"])
    print(label1)
    if label1:
        label2 = vmcreate.mod_vm_conf(message)
        if label2:
            label3 = vmcreate.copy_vm_image(message["vm_type"], message["vm_name"])
            if label3:
                vmcreate.define_vm(message["vm_name"])
            else:
                logging.error("磁盘文件复制失败")
                #print("磁盘文件复制失败")
        else:
            logging.error("配置文件修改失败")
            #print("配置文件修改失败")
    else:
        logging.error("配置文件复制失败")
        #print("配置文件复制失败")

def run():
    '''

    :return:
    '''
    bar = JudgePath.main()
    if bar:
        interactive()
        create_pross()
    else:
        exit()

    #print("this is a run ...")
    logging.debug("this is a run ...")