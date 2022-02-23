import assult_print as a_print
import assult_active as a_active

# 출력 판단 함수
def print_judgment_func(class_page):

    page_now = class_page.now_page_output() # 현재 페이지
    list_page_all = class_page.list_page_all_output() # 전체 페이지 리스트

    page_error = class_page.page_error_output() # 에러 페이지

    if page_now in list_page_all:
        a_print.str_print_func(page_now)
    
    else:
        a_print.str_print_func(page_error)

# 정상 입력 판단 함수
def input_succeed_judgment_func(cmd_input):
    # 입력이 숫자인가?
    if(cmd_input.isdigit() == True):
        # 입력이 정수인가?
        if(float(cmd_input) == int(cmd_input)):
            return True # 참 리턴
        # 아닐때
        else:
            return False # 거짓 리턴
    # 아닐때
    else:
        return False # 거짓 리턴

# 입력 판단 함수
def input_judgment_func(class_page, cmd_input):
    page_now = class_page.now_page_output() # 현재 페이지 변수

    page_main = class_page.page_main_output() # 메인 페이지 변수
    page_create_character = class_page.page_create_character_output # 캐릭터 생성 페이지 변수

    # 현재 페이지가 캐릭터 생성 페이지일 때
    if page_now == page_create_character:
        page_now = input_create_character_judgment_func(class_page, cmd_input)
        return page_now

    # 현재 페이지가 메인일 때
    elif page_now == page_main:
        page_now = input_main_judgment_func(class_page, cmd_input)
        return page_now

    else:
        return page_now

# 메인 화면창 판단 함수
def input_main_judgment_func(class_page, cmd_input):
    page_now = class_page.now_page_output() # 현재 페이지 변수

    list_page_main = class_page.list_page_main_output() # 메인 페이지 리스트
    
    page_error = class_page.page_error_output() # 에러 페이지 변수

    if cmd_input > -1 and cmd_input < 4:
        page_now = a_active.active_func(class_page, cmd_input)
        page_now = list_page_main[cmd_input - 1]

        return page_now
    
    else:
        a_print.str_print_func(page_error)
        return page_now

# 닉네임 생성창 판단 함수
def input_create_character_judgment_func(class_page, cmd_input):
    page_now = class_page.now_page_output() # 현재 페이지 변수
    
    page_error = class_page.page_error_output() # 에러 페이지 변수

    if len(cmd_input) > 0 and len(cmd_input) < 13:
        page_now = a_active.active_func(class_page, cmd_input)
        return page_now
    
    else:
        a_print.str_print_func(page_error)
        return page_now
