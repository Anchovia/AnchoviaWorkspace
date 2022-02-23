from sys import exit
import assult_print as a_print
import assult_player_data as a_player_data

def active_func(class_page, cmd_input):
    page_now = class_page.now_page_output()

    page_main = class_page.page_main_output() # 메인 페이지 변수
    page_create_character = class_page.page_create_character_output() # 캐릭터 생성 페이지 변수
    page_load_save = class_page.page_load_save_output() # 세이브 로드 페이지 변수
    page_exit = class_page.page_exit_output() # 게임 종료 페이지 변수
    page_prologue = class_page.page_prologue_output()

    if page_now == page_main:
        pass

    elif page_now == page_create_character:
        player_name = a_player_data.creat_name_func(cmd_input)
        a_print.str_print_func(player_name)
        page = page_prologue
        return page

    elif page_now == page_load_save:
        a_print.str_print_func(page)
        page = page_main
        return page

    elif page_now == page_exit:
        a_print.str_print_func(page)
        exit()
