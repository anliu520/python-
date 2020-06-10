#Author:Anliu
import socket,os
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #回收重用端口
#server.bind(("127.0.0.1",8888))
server.bind(("0.0.0.0",8888))
server.listen()
print("等待数据")
while True:
    conn,addr = server.accept()
    print("数据来了...")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            reg = os.popen(data.decode("utf-8")).read()
            print(reg)
            if len(reg) == 0:
                reg = "输入内容为空"
            conn.send(str(len(reg.encode("utf-8"))).encode("utf-8"))
            conn.send(reg.encode())
        except ConnectionResetError as key:
            break
#        conn.close()