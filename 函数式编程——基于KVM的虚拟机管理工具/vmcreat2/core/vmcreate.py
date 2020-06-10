#anliu
'''
 the script is used created vm .
'''

import shutil,os,sys,uuid
from xml.etree import ElementTree as ET

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import vm_config
from core import LogHandler


def copy_vm_conf(src_name,det_name):
    '''
    The function is to copy the virtual machine configuration file.
    :param src_name: Source file name: default to the system type you entered.
    :param det_name: Destination file name: the default is the name of the virtual machine you want to create.
    :return: Return 1 means the file is copied successfully, return 0 means the file is copied failed
    '''

    if os.path.isfile(os.path.join(vm_config.conf["src_conf_path"],src_name + ".xml")) :
        shutil.copyfile(os.path.join(vm_config.conf["src_conf_path"],src_name + ".xml"),os.path.join(vm_config.conf["det_conf_path"],det_name + ".xml"))
        flag = 1
    else:
        print("The source file does not exist, please check the system type or install a new virtual machine system...")
        flag = 0

    return flag


def copy_vm_image(src_name,det_name):
    '''
    The function is to copy the virtual machine iamge file.
    :param src_name: Source file name: default to the system type you entered.
    :param det_name: Destination file name: the default is the name of the virtual machine you want to create.
    :return: Return 1 means the file is copied successfully, return 0 means the file is copied failed
    '''

    if os.path.isfile(os.path.join(vm_config.image["src_image_path"],src_name + ".img")):
        shutil.copyfile(os.path.join(vm_config.image["src_image_path"],src_name + ".img"),os.path.join(vm_config.image["det_image_path"],det_name + ".img"))
        flag = 1
    else:
        print("The source file does not exist, please check the system type or install a new virtual machine system...")
        flag = 0

    return flag

def mod_vm_conf(message):
    '''

    :param message:
    :return:
    '''

    tree = ET.parse(os.path.join(vm_config.conf["det_conf_path"],message["vm_name"] + ".xml"))
    root = tree.getroot()

    for node1 in root.iter("name"):
        print(node1.tag,node1.text)
        node1.text = message["vm_name"]

    for node2 in root.iter("uuid"):
        print(node2.tag,node2.text)
        node2.text = str(uuid.uuid1())

    for node3 in root.iter("memory"):
        print(node3.tag,node3.text)
        node3.text = str(message["vm_mem_max"])

    for node4 in root.iter("currentMemory"):
        node4.text = str(message["vm_mem_curr"])

    for node5 in root.iter("vcpu"):
        node5.text = str(message["vm_cpu_max"])
        node5.attrib["current"] = str(message["vm_cpu_curr"])

    for node6 in root.iter("source"):
        try:
            print(node6.attrib["file"])
            node6.attrib["file"] = os.path.join(vm_config.image["det_image_path"],message["vm_name"] + ".img")

        except KeyError as key:
            pass

    for node7 in root.iter("graphics"):
        print(node7.tag,node7.text,node7.attrib)
        node7.attrib["port"] = message["vm_vnc_port"]

    tree.write(os.path.join(vm_config.conf["det_conf_path"],message["vm_name"] + ".xml"))

    return 1

#mod_vm_conf("test02",2048000,3096000,2,1,"5988")


def define_vm(det_mane):

    os.chdir(vm_config.conf["det_conf_path"])
    os.system("virsh define %s" %det_mane + ".xml")
    os.system("virsh start %s" %det_mane)

#define_vm("test02")