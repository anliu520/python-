#anliu
import os,sys
import logging.config
import configparser

logging.config.fileConfig('../conf/logging.conf')
logger = logging.getLogger("simpleExample")

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(base_path)

def role_frame(direction):
    '''
    This function is used to create a role directory
    :param direction:
    :return:
    '''
    try:
        os.chdir(os.path.dirname(os.path.dirname(__file__)) + "/data/ansible/roles")
    except FileNotFoundError as key:
        logger.error(key)
        exit()

    if not os.path.isdir(direction):
        os.makedirs(direction)
    else:
        logger.debug("create ./data/ansible/roles exist")


'''
def mod_hosts(sname):
    config_hosts = configparser.ConfigParser()
    #config_hosts.read("../data/ansible/hosts")
    config_hosts[sname] = {
        'ansible_ssh_host': "192.168.42.61",
        'ansible_ssh_port': "22",
        'ansible_ssh_user': "root",
        'ansible_ssh_pass': "123456",
    }
    #config_hosts["nginx"] = ["192.168.42.1","192.168.42.2"]

    with open(base_path + "/data/ansible/hosts","a") as configfile:
        config_hosts.write(configfile)

    #if not config_hosts.has_section(sname):
    #    config_hosts.add_section(sname)
    #    config_hosts.write(open(base_path + "/data/ansible/hosts"))
    #else:
    #    logger.debug(base_path + "/data/ansible/hosts " + sname + " already is exsit")

#mod_hosts("nginx")


def mod_hosts():
    tempdata = [
        {
            "Groupname": "Group1",
            "Items": [
                {
                    #"name": "Srv01",
                    "ansible_ssh_host": "172.16.100.20",
                    "ansible_ssh_port": "22",
                    "ansible_ssh_user": "work",
                    "ansible_python_interpreter": "/usr/bin/python"
                },
                {
                    #"name": "Srv02",
                    "ansible_ssh_host": "172.16.100.30",
                    "ansible_ssh_port": "22",
                    "ansible_ssh_user": "work",
                    "ansible_python_interpreter": "/usr/bin/python"
                },
            ]
        },
    ]
    return tempdata
    
'''

def check_hosts(tempdata):

    with open(base_path + "/data/ansible/hosts","r",encoding="utf-8") as file2:
        for i in tempdata:
            groupname = i.get("Groupname")
            for i in file2:
                print(i.strip())
                print("[" + groupname + "]".strip())
                if i.strip() == "[" + groupname + "]".strip():
                    print(groupname)
                    return None
                else:
                    flag = groupname

    return flag

#print(check_hosts("nginx"))

def genHostsFile(tempdata,groupname):
    print(groupname)
    '''
    get hosts file
    :param tempdata: hosts message list
    :return:
    '''
    try:
        with open(base_path + "/data/ansible/hosts","a") as file1:
            file1.write("[" + groupname + "]\n")
            for i in tempdata:
                print(i.get("Items"))
                for server in i.get("Items"):
                    name = server.get("name")
                    ansible_ssh_host = server.get("ansible_ssh_host")
                    ansible_ssh_port = server.get("ansible_ssh_port")
                    ansible_ssh_user = server.get("ansible_ssh_user")
                    ansible_python_interpreter = server.get("ansible_python_interpreter")

                    info = "ansible_ssh_host={0} ansible_ssh_port={1} ansible_ssh_user={2} ansible_python_interpreter={3}".format(
                        ansible_ssh_host, ansible_ssh_port, ansible_ssh_user, ansible_python_interpreter)
                    line = name + " " + info + "\n"
                    #line = info + "\n"
                    file1.write(line)

    except Exception as err:
        logger.error(err)
        return False

    return True