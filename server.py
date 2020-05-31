
#2017038015신윤성
#서버를 생성하는 파일. socket모듈을 이용해 서버를 생성하고, 클라이언트가 그 서버에 접속한다.
#접속이 확인되면 스레드를 생성해 플레이어 한 명당 한 개씩 스레드를 가지고 플레이한다.
#reply가 상대방을 의미한다. reply객체를 상대에게 보냄으로써 상대의 상태를 화면에 그릴 수 있다.

import socket
from _thread import * #접속한 클라이언트마다 새로운 쓰레드 생성.
import pickle
from game import Player
import pygame as pg

port = 5555
server = "25.66.112.229"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 생성.

try:
    s.bind((server, port))  #소켓을 bind를 이용해 포트와 ip번호 튜플로 묶는다.
except socket.error as e:
    str(e)

s.listen(2)  #2명까지 접속을 허용

print("waiting for a connection....")

key_set = {'right': pg.K_RIGHT, 'left': pg.K_LEFT, 'up': pg.K_UP, 'down': pg.K_DOWN, 'drop': pg.K_SPACE}
players = [Player('left', key_set), Player('right', key_set)]


def thread_client(conn, player):  #스레드 생성
    conn.send(pickle.dumps(players[player]))

    while True:
        try:
            data = pickle.loads(conn.recv(2048*3))
            players[player] = data              #player번째 클라이언트가 받는 객체

            if not data:
                print("disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]   #2번째 플레이어면 0번째 객체가 상대방
                else:
                    reply = players[1]   #아닐시 1번째 객체가 상대방

                print("receiving", data)
                print("sending", reply)  #서버와 통신이 되는 지 체크

            conn.sendall(pickle.dumps(reply))  #상대방 정보를 보냄
        except:
            break
    print("lost connection")
    conn.close()


if __name__ == "__main__":
    cur_player = 0
    while True:
        conn, addr = s.accept()        #접속할 때 까지 기다린다.
        print("Connected to:", addr)

        start_new_thread(thread_client, (conn, cur_player)) #그 한 명의 스레드 함수 실행
        cur_player += 1