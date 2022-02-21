from assult_print import str_print_func

str_page_main ='''
● 1. 게임 시작
● 2. 세이브 파일 불러오기
● 0. 게임 종료
'''

# 페이지 변수
list_main_page = ["create_name", "load_save", "exit"]

# 정상 입력 판단 한수
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
def input_judgment_func(page, cmd_input):
    cmd_input = int(cmd_input)
    if page == "main":
        page = input_main_judgment_func(cmd_input)
        return page
        
    else:
        return page

# 메인 화면 판단 함수
def input_main_judgment_func(cmd_input):
    if cmd_input == 1:
        page = list_main_page(cmd_input + 1)
        return page

# 출력 판단 함수
def print_judgment_func(page):
    if page == "main":
        str_print_func(str_page_main)
