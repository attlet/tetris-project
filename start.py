#start파일에 포함되는 온라인 플레이 함수.
#p는 플레이어 한 명의 객체를 받아온다. 이를 움직이고 조작한 뒤 상대에게 그 정보를 보낸다.
#상대는 그 정보를 받고 자신이 조작한 정보를 다시 서버로 보내 계속 주고 받는다.

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




