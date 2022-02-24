import assault_print as a_print
import assault_input as a_input
import assault_active as a_active

def judgment_system_func(class_Page, class_Player):
    # 현재 페이지 변수 생성
    page_now = class_Page.output_page_now()

    # 전체 페이지 딕셔너리 생성
    dict_page_all = class_Page.output_page_all()

    # 페이지 판단 함수 실행
    page_new = judgment_page_func(class_Page, class_Player, page_now, dict_page_all) # 함수 실행 결과 신규 페이지에 저장

    return page_new # 신규 페이지 반환

def judgment_page_func(class_Page, class_Player, page_now, dict_page_all):
    # 메인 페이지 판단
    if page_now == dict_page_all["main"]:
        # 메인 로직 판단 함수 실행
        page_new = judgment_logic_main_func(class_Page, page_now) # 함수 실행 결과 신규 페이지에 저장
        return page_new # 신규 페이지 반환

    # 캐릭터 이름 생성 페이지 판단
    elif page_now == dict_page_all["create_character_name"]:
        page_new = judgment_logic_create_character_name_func(class_Page, class_Player, page_now)
        return page_new
    
    # 프롤로그 페이지 판단
    elif page_now == dict_page_all["prologue"]:
        page_new = judgment_logic_prologue_func(class_Page, page_now)
        return page_new

    elif page_now == dict_page_all["in_game"]:
        page_new = judgment_logic_in_game_func(class_Page, class_Player, page_now)
        return page_new

    else:
        print("'judgment_page_func'에서 치명적 오류 발생!")
        a_active.active_quit_game()

def judgment_logic_main_func(class_Page, page_now):
    # 페이지 선택지 프린트
    a_print.print_str_page_select_func(page_now)

    # 커맨드 입력받음
    cmd_input = a_input.input_func()

    # 판단 부분
    try:
        cmd_input = int(cmd_input) # str형 cmd_input을 int형으로 변환

        # 입력이 1, 2, 0일 때
        if cmd_input > -1 and cmd_input < 3:
            page_new = judgment_active_main_func(class_Page, page_now, cmd_input)
            return page_new
        
        # 아닐때
        else:
            page_new = a_active.active_error(page_now)
            return page_new
    
    # 예외처리
    except ValueError:
        page_new = a_active.active_error(page_now)
        return page_new

def judgment_active_main_func(class_Page, page_now, cmd_input):
    # 입력이 1(게임 시작)일 떄
    if cmd_input == 1:
        page_new = a_active.active_game_start(class_Page)
        return page_new
    
    # 입력이 2(세이브 파일 불러오기)일 떄
    elif cmd_input == 2:
        page_new = a_active.active_load_game(page_now)
        return page_new

    # 입력이 0(게임 종료)일 때
    else:
        a_active.active_quit_game()

def judgment_logic_create_character_name_func(class_Page, class_Player, page_now):
    # 페이지 선택지 프린트
    a_print.print_str_page_select_func(page_now)

    # 커맨드 입력받음
    cmd_input = a_input.input_func()

    # 판단 부분
    try:
        if len(cmd_input) > 0 and len(cmd_input) < 13:
            page_new = judgment_create_character_name_func(class_Page, class_Player, cmd_input)
            return page_new
        
        else:
            page_new = a_active.active_error(page_now)
            return page_new
    
    except SyntaxError:
        page_new = a_active.active_error(page_now)
        return page_new
    
def judgment_create_character_name_func(class_Page, class_Player, cmd_input):
    page_new = a_active.active_create_player_name(class_Page, class_Player, cmd_input)
    return page_new

def judgment_logic_prologue_func(class_Page, page_now):
    # 페이지 선택지 프린트
    a_print.print_str_page_select_func(page_now)

    # 커맨드 입력받음
    cmd_input = a_input.input_func()

    cmd_input = cmd_input.upper() # 소문자를 대문자로 변환
    if cmd_input == "Y" or cmd_input == "N":
        page_new = judgment_prologue_func(class_Page, cmd_input)
        return page_new
        
    else:
        page_new = a_active.active_error(page_now)
        return page_new

def judgment_prologue_func(class_Page, cmd_input):
    if cmd_input == "Y":
        page_new = a_active.active_prologue_print_func(class_Page)
        return page_new
    
    else:
        page_new = a_active.active_change_page_ingame(class_Page)
        return page_new

def judgment_logic_in_game_func(class_Page, class_Player, page_now):
    # 페이지 선택지 프린트
    a_print.print_str_page_select_func(page_now)
