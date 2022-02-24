page_now = "page_main"

page_main = "page_main"
page_create_character_name = "page_create_character_name"
page_prologue = "page_prologue"
page_in_game = "page_in_game"

dict_page_all = {"main" : page_main, "create_character_name" : page_create_character_name, "prologue" : page_prologue, "in_game" : page_in_game}

class Page:
    def __init__(self, page_now = page_now, dict_page_all = dict_page_all):
        self.page_now = page_now
        self.dict_page_all = dict_page_all
    
    def update_page_now(self, page_now):
        self.page_now = page_now

    def output_page_now(self):
        return self.page_now
    
    def output_page_all(self):
        return self.dict_page_all
