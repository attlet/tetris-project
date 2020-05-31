import pygame as pg
from game import Player
from game import AI_Player
from setting import *
successes, failures = pg.init()
print("{0} successes and {1} failures in start.py".format(successes, failures))

screen = pg.display.set_mode(size)
pg.display.set_caption("HiPy Tetris")
clock = pg.time.Clock()


def solo_play():
    run = True
    key_set = {'right': pg.K_RIGHT, 'left': pg.K_LEFT, 'up': pg.K_UP, 'down': pg.K_DOWN, 'drop': pg.K_SPACE}
    player = Player('center', key_set)

    screen.fill(WHITE)
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            player.key_input(event)

        player.move_piece()
        player.fall_time_check()
        player.draw_board(screen)
        clock.tick(FPS)
        pg.display.flip()
        if player.is_game_over():
            run = False
            print("게임 오버 구현하기.")


def multi_play():
    run = True
    key_set1 = {'right': pg.K_RIGHT, 'left': pg.K_LEFT, 'up': pg.K_UP, 'down': pg.K_DOWN, 'drop': pg.K_RETURN}
    key_set2 = {'right': pg.K_d, 'left': pg.K_a, 'up': pg.K_w, 'down': pg.K_s, 'drop': pg.K_SPACE}
    player1 = Player('left', key_set1)
    player2 = Player('right', key_set2)
    Player.make_multi(player1, player2)
    screen.fill(WHITE)
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            player1.key_input(event)
            player2.key_input(event)

        player1.move_piece()
        player2.move_piece()
        player1.fall_time_check()
        player2.fall_time_check()
        player1.draw_board(screen)
        player2.draw_board(screen)
        clock.tick(FPS)
        pg.display.flip()
        if player1.is_game_over() or player2.is_game_over():
            run = False
            print("게임 오버 구현하기")


def computer_play():
    run = True
    ai_player = AI_Player('center')
    screen.fill(WHITE)
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    ai_player.env.ai_step()
        ai_player.env.ai_step()  # 이 line 주석처리 하면 엔터 누를때 마다 한번씩 행동함.
        ai_player.draw_board(screen)
        clock.tick(FPS)
        pg.display.flip()
        if ai_player.is_game_over():
            run = False
            print("게임 오버 구현하기")

def online_play():
    run = True
    n = Network()
    p = n.getp()    #플레이어 한 명 서버 연결
    screen.fill(WHITE)
    run_bgm(play_music)
    while run:
        clock.tick(FPS)
        p2 = n.send(p)  #상대방 플레이어 에게 p1의 객체를 넘긴다. p2는 reply객체를 받는다.

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            p.key_input(event)
            # p2.key_input(event)

        p.move_piece()
        # p2.move_piece()
        p.fall_time_check()    #자신의 board에서 블럭을 움직이고 체크하는 것.
        # p2.fall_time_check()
        # p.draw_board()
        redraw(screen, p, p2)  #p1 p2 둘 다 스크린에 그림.
        # p2.draw_board()
        pg.display.update()

        pg.display.flip()
        if p.is_game_over() or p2.is_game_over():
            run = False
            print("게임 오버 구현하기")



def main_menu():
    run = True
    menu_list = ['Play Game', 'Multi Play', 'vs Computer', 'Online Play', 'Exit']
    cur_menu = 0
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    cur_menu = (cur_menu + 1) % len(menu_list)
                if event.key == pg.K_UP:
                    cur_menu = (cur_menu + len(menu_list) - 1) % len(menu_list)
                if event.key == pg.K_RETURN:
                    if cur_menu == 0:
                        solo_play()
                    if cur_menu == 1:
                        multi_play()
                    if cur_menu == 2:
                        computer_play()
                    if cur_menu == 3:
                        online_play()
                    elif cur_menu == 4:
                        run = False
                        pg.display.quit()
                        quit()

        screen.fill(WHITE)
        menu_font = pg.font.SysFont("arial", 30, True, False)
        menu_text = []
        for text in menu_list:
            if menu_list[cur_menu] == text:
                menu_text.append(menu_font.render(text, True, colors[1]))
            else:
                menu_text.append(menu_font.render(text, True, colors[0]))

        i = 0
        for text in menu_text:
            screen.blit(text, [size[0] / 4, size[1] / 2 - 125 + i * 50])
            i += 1

        pg.display.flip()
        clock.tick(FPS)
    pg.quit()


if __name__ == "__main__":
    main_menu()
