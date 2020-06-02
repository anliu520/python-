#Author:Anliu

"""客户端"""
import socket
import json,struct
import os,hashlib
client = socket.socket()
client.connect(("localhost",6969))
#f1 = open("mysql.tar.gz","wb")
#f1 = open("aaa.text","wb")

#存放包头信息
head_syn = {
    "filename": None,
    "filepath": None,
}

#存放系统信息
base_path = {
    "filename":None,
    "filepath":None
}

while True:
    head_syn["filename"] = input("源文件名:>>>")
    head_syn["filepath"] = input("源文件路径:>>>")
    base_path["filename"]  = input("目的文件名:>>>")
    base_path["filepath"] = input("目的文件路径:>>>")

    #mgs = input(">>>:")
    try:
        if len(head_syn) == 0: continue
        head_syn_json = json.dumps(head_syn)
        client.send(head_syn_json.encode())
        #接收包头长度
        obj = client.recv(4)
        head_size = struct.unpack("i",obj)[0]   #1024*4 = 4096 bety 2^4096
        #data = client.recv(1024)
        print(head_size)

        #接收报头
        head_bytes = client.recv(head_size)

        #解析报头对数据的描述
        head_json = head_bytes.decode("utf-8")
        head_dic = json.loads(head_json)
        print(head_dic)

        #解析报头
        file_size = head_dic["file_size"]
        file_md5 = head_dic["file_md5"]

        print(file_size,file_md5)

        #接收数据
        with open(os.path.join(base_path["filepath"],base_path["filename"]),"wb") as f1:
            recv_size = 0
            while recv_size < file_size:
                res = client.recv(1024)
                f1.write(res)
                recv_size += len(res)
                print("总大小：%s 已下载大小：%s" %(file_size,recv_size))

        #校验数据
        file_md5_add = hashlib.md5(open(os.path.join(base_path["filepath"], base_path["filename"]), 'rb').read()).hexdigest()
        if file_md5 == file_md5_add:
            print("文件传输完成....")
        else:
            print("文件有差错....")

        #while True:
            #client.send(mgs.encode("utf-8"))
            #data = client.recv(1024000)
            #print("revc:",data.decode())
            #f1.write(data)
            #f1.flush()
    except json.decoder.JSONDecodeError as key:
        print("文件不存在....")

#f1.close()
client.close()