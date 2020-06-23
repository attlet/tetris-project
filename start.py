
#작성자: 2017038015신윤성
#start파일에 포함되는 온라인 플레이 함수.
#p는 플레이어 한 명의 객체를 받아온다. 이를 움직이고 조작한 뒤 상대에게 그 정보를 보낸다.
#상대는 그 정보를 받고 자신이 조작한 정보를 다시 서버로 보내 계속 주고 받는다.

def online_play(network):
    run = True
    p1 = network.getp()          #서버에서 객체 하나 받아옴
    screen.fill(WHITE)
    while run:
        p2 = network.send(p1)    #상대방 객체정보를 받아옴

        p1.init_attack_count()

        if p2.attack_count != 0:
            print(p2.attack_count)
            p1.online_attacked(p2.attack_count)
            p2.init_attack_count()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            if not p2.is_waiting():
                p1.key_input(event)

        if not p2.is_waiting():         #p2의 상황에 따라 움직임
            p1.move_piece()
            p1.fall_time_check()
            p1.cal_attack_count()

        p1.draw_board(screen)
        p2.draw_board(screen)           #p1과 p2를 화면에 그림
        pg.display.update()

        clock.tick(FPS)
        pg.display.flip()

        if p1.is_game_over() or p2.is_game_over():
            network.send(p1)
            run = False
            print("게임 오버 구현하기")






