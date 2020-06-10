#Author:Anliu

import socket
client = socket.socket()
#client.connect(("127.0.0.1",8888))
client.connect(("192.168.42.3",8888))
while True:
    mgs = input(">>>:").strip()
    if len(mgs) == 0: continue
    client.send(mgs.encode("utf-8"))
    data = client.recv(1024)
    #print(data.decode("utf-8"))
    cmd_size = 0
    received_data = b""
    while cmd_size < int(data.decode("utf-8")):
        cmd_data = client.recv(1024)
        cmd_size += len(cmd_data)
        received_data += cmd_data
        #print(cmd_data.decode("utf-8"))
    else:
        #print("命令执行完毕...",cmd_size)
        print(received_data.decode())


