from time import sleep

# 문자 출력 속도 변수
delay = 0.05

# 시스템 문자열
str_system_line = "=" * 120
str_system_error = '''
다시 입력해주세요.
'''
str_system_dummy_error = '''
아직 구현되지 않은 시스템입니다.
'''

str_system_quit = '''
프로그램을 종료합니다.
'''

# 페이지 선택 문자열
str_page_select_main = '''
● 1. 게임 시작
● 2. 세이브 파일 불러오기
● 0. 게임 종료
'''
str_page_select_create_character_name = '''
앞으로 모험을 함께 할 에이전트의 이름을 입력해주세요(1~12자).
'''
str_page_select_prologue = '''
프롤로그를 보시겠습니까(Y/N)?
'''

str_page_select_in_game = '''
■ [가능한 이동]
├─● 1. 총포상
├─● 2. 약국
├─● 3. 부트 캠프
├─● 4. 제작 공방
├─● 5. 터미널
└─● 0. 게임 종료
'''

# 스토리 문자열
str_story_prologue = '''
203X 년 저녁.
그 여느 때와 같이 평화롭던 지구 상공에 정체불명의 우주선이 갑작스럽게 등장하게 된다.
인류가 대책을 세울 틈도 없이 우주선에서 밝은 빛이 뿜어져 나오게 되고, 그 빛을 따라 외계 우주선들이 튀어나오게 된다.
외계인들은 놀라 도망치는 인간들을 공격하기 시작하였고, 인류는 속수무책으로 당하기 시작하며, 주요 도시들이 함락되기에 이른다.
하지만, 그 와중에 인류는 끝까지 항전하며 일부 우주선들을 파괴하였고, 특수한 약품이 들은 우주선 한 대를 나포하게 되었다.
인류는 이 우주선을 수색하게 되고, 우주선의 화물칸 속에는 미지의 약품이 들어있었다.
해당 약품들을 획득한 정부는 소수의 인간을 데려와 인체실험을 벌이게 되고, 해당 약품을 인간 동맥에 투약하면, 강력한 신체 능력을 갖출 수 있음을 알아내게 된다.
이에 정부는 이러한 인간들에게 ‘에이전트’라는 이름을 붙이고, 이들을 불러 모아 외계인들과 대적할 군대를 양성하기 시작하였다.
또한, 해당 약품을 제작해내기 위해 정부는 비밀리에 연구를 시작하게 된다.
'''

dict_page_select_all = {"page_main" : str_page_select_main, "page_create_character_name" : str_page_select_create_character_name, "page_prologue" : str_page_select_prologue, "page_in_game" : str_page_select_in_game}

def print_str_page_select_func(page_now):
    print(str_system_line + "\n" + dict_page_select_all[page_now] + "\n" + str_system_line)

def print_str_normal_func(string):
    print(str_system_line + "\n" + string + "\n" + str_system_line)

def print_str_seq_func(string):
    print(str_system_line)
    for i in string:
        print(i, end="", flush=True)
        sleep(delay)
    print("\n" + str_system_line)
        
def print_str_error_func():
    print(str_system_line + "\n" + str_system_error + "\n" + str_system_line)

def print_str_system_dummy_error_func():
    print(str_system_line + "\n" + str_system_dummy_error + "\n" + str_system_line)

def print_str_system_quit_func():
    print(str_system_line + "\n" + str_system_quit + "\n" + str_system_line)

def print_str_create_character_name_func(player_name):
    print(str_system_line + "\n" + "\n앞으로 모험을 진행할 에이전트의 이름은 '%s'입니다.\n" % player_name + "\n" + str_system_line)

def print_str_story_prologue():
    print_str_seq_func(str_story_prologue)
