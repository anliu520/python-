#anliu
'''
main...
'''
from core import inteface
import configparser
import os
import logging.config

logging.config.fileConfig('../conf/logging.conf')
logger = logging.getLogger("simpleExample")

#Define path
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Define role list
role_list = ["files","templates","vars","handlers","meta","default","tasks"]

#Get the configured service name
config = configparser.ConfigParser()
config.read("../conf/service.conf")
# config.read("/usr/ansible_install/conf/service.conf")
#print(type(config.sections()))
#flag = config.sections().index("mysql")
#print(config.sections()[config.sections().index("nginx")])

def role_creat():
    '''
    Create role directory
    :return:
    '''
    for i in range(len(role_list)):
        #print(type(i))
        inteface.role_frame(config.sections()[0] + "/" + role_list[i])

#define hosts contain list

tempdata = [
    {
        "Groupname": "nginx",
        "Items": [
            {
                "name": "server01",
                "ansible_ssh_host": "192.168.42.61",
                "ansible_ssh_port": "22",
                "ansible_ssh_user": "root",
                "ansible_python_interpreter": "/usr/bin/python"
            },
            {
                "name": "server02",
                "ansible_ssh_host": "192.168.42.3",
                "ansible_ssh_port": "22",
                "ansible_ssh_user": "root",
                "ansible_python_interpreter": "/usr/bin/python"
            },
        ]
    },
]

def interactive():
    #print(tempdata[0])
    tempdata[0]["Groupname"] = config.sections()[0]
    #tempdata[0] = input(">>>:")
    num = 0
    for item in tempdata[0]["Items"]:
        list_name = config.get(config.sections()[0],"name")
        list_host = config.get(config.sections()[0],"ansible_ssh_host")
        print(list_host.split(" ")[num])
        print(list_name.split(" ")[num])
        item["name"] = list_name.split(" ")[num]
        item["ansible_ssh_host"] = list_host.split(" ")[num]
        item["ansible_ssh_port"] = config.get(config.sections()[0],"ansible_ssh_port")
        item["ansible_ssh_user"] = config.get(config.sections()[0],"ansible_ssh_user")
        item["ansible_python_interpreter"] = config.get(config.sections()[0], "ansible_python_interpreter")
        num +=1

#interactive()

def hosts_creat():
    '''
    create hosts
    :return:
    '''
    #print(inteface.check_hosts(tempdata))
    groupname = inteface.check_hosts(tempdata)
    if groupname:
        inteface.genHostsFile(tempdata,groupname)
    else:
        logger.error("groupname is exist...")
        exit()
    #inteface.genHostsFile(tempdata)

def exec_run(sname):
    #pass
    os.chdir(base_path + "/data/ansible")
    os.system("ansible-playbook -i hosts %s"%(sname + ".yaml"))


def run():
    #role_creat()
    interactive()
    hosts_creat()
    #exec_run(config.sections()[0])

    print("this is a main...")