# Client:客户端
import socket
def clientFunc():
    # 1.实例化一个socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.发送消息
    text1 = "I love Python."
    data = text1.encode()
    sock.sendto(data, ("127.0.0.1", 7852))
    # 3.接受反馈
    data, addr = sock.recvfrom(200)
    text2 = data.decode()
    print(text2)
if __name__ == "__main__":
    clientFunc()