page_now = "main"

# 페이지 변수
page_error = "error"
page_main = "main"
page_create_character = "create_character"
page_load_save = "load_save"
page_exit = "exit"
page_prologue = "prologue"

# 페이지 리스트
list_main_page = [page_create_character, page_load_save, page_exit] # 1. 게임 시작[0] 2. 세이브 파일 불러오기[1] 0. 게임 종료[2]

list_page_bundle = [list_main_page]

dict_page_all = {"main" : page_main, "create_character" : page_create_character, "load_save" : page_load_save, "exit" : page_exit, "prologue" : page_prologue}
list_page_all = list(dict_page_all)

class Page:
    def __init__(self, page_now = page_now, dict_page_all = dict_page_all, list_page_all = list_page_all, page_error = page_error, page_create_character = page_create_character):
        self.page_now = page_now
        self.dict_page_all = dict_page_all
        self.list_page_all = list_page_all
        self.page_error = page_error
        self.page_create_character = page_create_character
    
    def page_update(self, page_now):
        self.page_now = page_now
    
    def page_create_character_output(self):
        return self.page_create_character

    def now_page_output(self):
        return self.page_now

    def list_page_all_output(self):
        return self.list_page_all
    
    def dict_page_all_output(self):
        return self.dict_page_all

    def page_error_output(self):
        return self.page_error
