# 시스템 관련 변수
string_logic = 0

# 시스템 프린트 변수
str_line = "=" * 120

str_error = '''
다시 입력해주세요
'''

str_exit = '''
프로그램을 종료합니다.
'''

# 기본 프린트 변수
str_page_main ='''
● 1. 게임 시작
● 2. 세이브 파일 불러오기
● 0. 게임 종료
'''

str_page_create_character = '''
앞으로 여정을 함께할 에이전트의 이름을 입력해주세요(1~12자).
'''

str_page_load_save = '''
아직 구현되지 않은 콘텐츠입니다.
'''

str_page_exit = '''
프로그램을 종료합니다.
'''

str_page_prologue = '''
프롤로그를 보시겠습니까?
'''

# 프린트 모음 딕셔너리
dict_print = {"line" : str_line, "error" : str_error, "main" : str_page_main, "create_character" : str_page_create_character, "load_save" : str_page_load_save, "exit" : str_exit, "prologue" : str_page_prologue}

def make_string_func(input):
    if input in list(dict_print):
        return dict_print[input]
    else:
        input = str(input)
        return "\n" + input + "\n"

def str_print_func(data):
    string = make_string_func(data)
    print(dict_print["line"] + "\n" + string + "\n" + dict_print["line"])
