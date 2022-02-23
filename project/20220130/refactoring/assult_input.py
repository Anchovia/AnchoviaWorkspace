import assult_print as a_print
import assult_judgment as a_judgment

# 입력 함수
def input_func(class_page):
    cmd_input = input("입력: ") # 입력받음

    page_now = class_page.now_page_output() # 현재 페이지 변수
    page_create_character = class_page.page_create_character_output # 캐릭터 생성 페이지 변수

    page_error = class_page.page_error_output() # 에러 페이지 변수

    # 닉네임 생성창 한정
    if page_now == page_create_character:
        page_now = a_judgment.input_judgment_func(class_page, cmd_input) # 페이지 판단 함수로 페이지 객체와 입력받은 값 전달 및 현재 페이지 반환
        class_page.page_update(page_now) # 현재 페이지 업데이트
        return class_page # 페이지 객체 반환

    # 입력이 숫자일 때
    if a_judgment.input_succeed_judgment_func(cmd_input) == True:
        page_now = a_judgment.input_judgment_func(class_page, cmd_input) # 페이지 판단 함수로 페이지 객체와 입력받은 값 전달 및 현재 페이지 반환
        class_page.page_update(page_now) # 현재 페이지 업데이트
        return class_page # 페이지 객체 반환

    # 입력이 숫자가 아닐때
    else:
        a_print.str_print_func(page_error) # 오류문 출력
        return class_page # 페이지 객체 반환
