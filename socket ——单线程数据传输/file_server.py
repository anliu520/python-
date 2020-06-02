#Author:Anliu

'''
服务端
'''

import socket,os,hashlib
import json,struct
md5 = hashlib.md5()
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #回收重用端口
server.bind(("localhost",6969))
server.listen(5)
print("等待数据")
while True:
    conn, addr = server.accept()
    print(conn, addr)
    print("数据来了")

    head_ack = {
        "file_size": "",
        "file_md5": ""
    }
    while True:
        try:
            data_sec = conn.recv(1024).decode()
            #data = eval(data_sec)
            data = json.loads(data_sec)
            print("recv:",type(data))
            print(os.path.join(data["filepath"],data["filename"]))
            #data = eval(data)
            if not data:
                break

            elif os.path.isfile(os.path.join(data["filepath"],data["filename"])):
                file_size = os.path.getsize(os.path.join(data["filepath"],data["filename"]))
                file_md5 = hashlib.md5(open(os.path.join(data["filepath"],data["filename"]),'rb').read()).hexdigest()
                head_ack["file_size"] = file_size
                head_ack["file_md5"] = file_md5
                head_ack_json = json.dumps(head_ack).encode("utf-8")

                #发送包头长度。
                conn.send(struct.pack("i",len(head_ack_json)))  #固定长度为4

                #发送包头
                conn.send(head_ack_json)

                #发送真实数据
                with open(os.path.join(data["filepath"],data["filename"]),"rb") as f1:
                    for a in f1:
                        conn.send(a)

                #conn.send(head_ack_json.encode())
            else:
                conn.send(b"The file doesn't exsit...")


            #f1 = open(os.path.join(data["filepath"],data["filename"]),"rb")
            #for line in f1:
            #   print(f1.readable())
                #print(reg)
                #conn.send(reg.encode())
            #    conn.send(line)
            #    print("yifasong")
                #num += 1
                #if num > 10: break
        except ConnectionResetError as key1:
            break
        except json.decoder.JSONDecodeError as key2:
            break
#server.close()
