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

str_page_create_name = '''
앞으로 여정을 함께할 에이전트의 이름을 입력해주세요(1~12자).
'''

str_page_load_save = "아직 구현되지 않은 콘텐츠입니다."

str_page_exit = "프로그램을 종료합니다."

# 프린트 모음 딕셔너리
dict_print = {"line" : str_line, "error" : str_error, "exit" : str_exit, "main" : str_page_main, "create_name" : str_page_create_name, "load_save" : str_page_load_save, "exit" : "아직 구현되지 않은 콘텐츠입니다."}

class Class_Print:
    def __init__(self, dict_print, page):
        self.dict_print = dict_print
        self.page = page

    def __str__(self):
        return self.dict_print["line"] + "\n" + self.dict_print[self.page] + "\n" + self.dict_print["line"] # 출력

def str_print_func(page):
    pt = Class_Print(dict_print, page)
    print(pt)
