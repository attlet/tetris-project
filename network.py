
#작성자: 2017038015 신윤성
#두 명의 클라이언트가 서로에게 정보를 주고 받을 수 있도록 하는 파일.
#pickle모듈을 이용해 객체를 주고 받을 수 있도록 했다.


import socket
import pickle

class Network:
    def __init__(self, address):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #클라이언트 소켓 생성
        self.server = address
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()                #서버에 연결 후 받는 객체 리턴

    def getp(self):
        return self.p

    def connect(self):
        self.client.connect(self.addr)
        return pickle.loads(self.client.recv(2048 * 3))

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))  # 서버에 정보를 보내고 받은 정보 리턴
            return pickle.loads(self.client.recv(2048 * 3))
        except socket.error as e:
            print(e)