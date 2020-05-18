import socket
from _thread import * #접속한 클라이언트마다 새로운 쓰레드 생성.
import sys
import pickle
from start import Player
import pygame as pg

port = 5555
server = "192.168.219.148"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 객체. 인자 하나는 어드레스 패밀리(주소체계.ipv4의미), 두번째는 소켓 타입.

try:
    s.bind((server, port)) #5555포트에서 server에 연결하도록 함. ' '을 앞에 넣으면 모든 인터페이스 연결가능.
except socket.error:
    print("server error")

s.listen(2)
#해당 소켓이 총 몇개의 동시접속까지를 허용할지 정함.

print("waiting for a connection....")
key_set = {'right': pg.K_RIGHT, 'left': pg.K_LEFT, 'up': pg.K_UP, 'down': pg.K_DOWN, 'drop': pg.K_SPACE}
players = [Player('left', key_set), Player('right', key_set)]

def thread_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(12000))
            players[player] = data

            if not data:
                print("disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("receiving", data)
                print("sending", reply)

            conn.sendall(pickle.dump(reply))
        except:
            break
    print("lost connection")
    conn.close()

curplay = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(thread_client, (conn, curplay))
    curplay += 1


