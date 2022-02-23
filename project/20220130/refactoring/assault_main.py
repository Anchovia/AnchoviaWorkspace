import assault_judgment as a_judgment
import assault_input as a_input
import assault_page as a_page

# 메인 함수
def main():
    class_page = a_page.Page() # 페이지 객체 생성

    while True:
        print(class_page.now_page_output()) # 테스트용 현재 장면 프린트

        a_judgment.print_judgment_func(class_page) # 페이지 객체를 출력 판단 함수 인자로 전달
        now_page = a_input.input_func(class_page) # 입력 함수 실행 및 현재 페이지를 받아옴
        class_page.page_update(now_page) # 현재 페이지 업데이트

# 프로그램 실행
if __name__== "__main__":
    main()
