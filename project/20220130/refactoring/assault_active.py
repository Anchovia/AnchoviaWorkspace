from sys import exit
import assault_print as a_print

def active_game_start(class_Page):
    page_new = class_Page.dict_page_all["create_character_name"]
    return page_new


def active_load_game(page_now):
    a_print.print_str_system_dummy_error_func() # 더미데이터 오류
    page_new = page_now
    return page_new

def active_quit_game():
    a_print.print_str_system_quit_func()
    exit()

def active_error(page_now):
    a_print.print_str_error_func()
    page_new = page_now
    return page_new

def active_create_player_name(class_Page, class_Player, cmd_input):
    player_name = cmd_input
    class_Player.update_player_name(player_name)
    
    a_print.print_str_create_character_name_func(player_name)

    page_new = class_Page.dict_page_all["prologue"]
    return page_new

def active_prologue_print_func(class_Page):
    a_print.print_str_story_prologue()
    page_new = class_Page.dict_page_all["in_game"]
    return page_new

def active_change_page_ingame(class_Page):
    page_new = class_Page.dict_page_all["in_game"]
    return page_new
