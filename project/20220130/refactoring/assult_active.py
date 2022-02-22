import os
import assult_print as a_print
list_page = ["main", "create_name", "load_save", "exit"]

def active_func(page):
    if page == "create_name":
        123
        
    elif page == "load_save":
        page = "main"
        return page

    elif page == "exit":
        a_print.str_print_func(page)
        os.exit()
