import assult_judgment as a_judgment
import assult_input as a_input
import assult_page as a_page

# 메인 함수
def main():
    class_page = a_page.Page()

    while True:
        a_judgment.print_judgment_func(class_page)
        now_page = a_input.input_func(class_page)
        class_page.page_transform(now_page)

# 프로그램 실행
if __name__== "__main__":
    main()
