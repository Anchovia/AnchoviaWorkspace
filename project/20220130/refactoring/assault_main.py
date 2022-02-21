import assult_judgment as judg

# 기본 변수
page = "main"
determination = 0

str_error = '''
다시 입력해주세요.
'''

# 입력 함수
def input_func(page):
    cmd_input = input("입력: ") # 입력받음
    # 입력이 숫자일 때
    if judg.input_succeed_judgment_func(cmd_input) == True:
        page = judg.input_judgment_func(page, cmd_input) # 입력 판단 함수 실행
    # 입력이 숫자가 아닐때
    else:
        judg.str_print_func(str_error) # 오류문 출력
        return page # 장면 리턴

# 프로그램 작동부
while True:
    judg.print_judgment_func(page)
    page = input_func(page)
