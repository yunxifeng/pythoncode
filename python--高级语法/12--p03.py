# Server:服务器端--改良版

import time
# socket模块负责socket编程
import socket
# 模拟服务器的函数
def serverFunc():
    # 1.建立socket实例
    # socket.AF_INET: 使用IPV4协议族
    # socket.SOCK_DGRAM: 使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定IP和port
    # 127.0.0.1: 本机
    # 7852: 除0-1023, 随意指定, 但不能冲突
    # 地址是一个tuple类型, (ip, port)
    addr1 = ("127.0.0.1", 7852)
    # 绑定ip地址和端口号
    sock.bind(addr1)

    # 3.接受对方消息
    # 等待方式为死等, 没有其他可能性
    # recvfrom接受的返回值是一个tuple, 前一项表示数据, 后一项表示发送方地址
    # 参数的含义是缓冲区大小
    # rst = socket.recvfrom(500)
    # 当server执行后,运行到这里会等待对方发送消息
    data1, addr2 = sock.recvfrom(500)

    print(data1)
    print(type(data1))

    # 发送过来的数据是bytes格式,必须通过解码才能得到str格式内容
    # decode默认参数是utf-8
    text = data1.decode()
    print(type(text))
    print(text)

    # 4.反馈
    rsp = "I am not hungry."
    # 发送的数据需要编码成bytes格式
    # encode默认参数是utf-8
    data2 = rsp.encode()
    # sendto是UDP模式
    sock.sendto(data2, addr2)

if __name__ == "__main__":
    # 死循环,让服务器营救运行
    while True:
        try:
            serverFunc()
        except Exception as e:
            print(e)
        time.sleep(1)