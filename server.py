import socket
from _thread import * #접속한 클라이언트마다 새로운 쓰레드 생성.
import pickle
from game import Player
import pygame as pg

port = 5555
server = "25.66.112.229"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

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
        conn, addr = s.accept()
        print("Connected to:", addr)

        start_new_thread(thread_client, (conn, cur_player))
        cur_player += 1