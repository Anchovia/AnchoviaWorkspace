import assault_page as a_page
import assault_player_data as a_player_data
from assault_judgment import judgment_system_func

# 메인 함수
def main():
    class_Page = a_page.Page()
    class_Player_Data = a_player_data.Player_Data()

    while True:
        #print("현재 페이지: %s" % class_Page.output_page_now())
        page_new = judgment_system_func(class_Page, class_Player_Data)
        class_Page.update_page_now(page_new)

# 프로그램 실행
if __name__== "__main__":
    main()
