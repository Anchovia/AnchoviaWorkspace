#include <stdio.h>
#include <string.h>



//추후 유지보수를 편히 하기위해 100이란 숫자를
//MAX_NUM으로 설정, 100을 200으로 바꾸면
//MAX_NUM은 200이 됨
#define MAX_NUM 100



//사용자의 정보를 저장하는 구조체
typedef struct {
    char name[30];
    char phone[20];
    char memo[40];
}User;



int saveFile(User* ptr, int* num);
int openFile(User* ptr, int* num);
void insert(User* ptr, int* num);
int deleted(User* ptr, int* num);
int search(User* ptr, int* num);
void printAll(User* ptr, int* num);



int main(void) {
    int input;
    User user[MAX_NUM]; //사용자 정보를 저장할 구조체 배열
    int person = 0; //저장된 user수



    openFile(user, &person);//저장된 데이터를 불러오는 함수



    //메뉴 선택
    while (1) {
        printf("***** Menu ***** \n");
        printf("1. Insert \n");
        printf("2. Delete \n");
        printf("3. Search \n");
        printf("4. Print All \n");
        printf("5. Save and Exit \n");

        printf("Choose the item: ");
        scanf("%d", &input);



        if (input == 1) {
            printf("\n[INSERT] \n");
            insert(user, &person);
        }
        else if (input == 2) {
            printf("\n[Delete] \n");
            deleted(user, &person);
        }
        else if (input == 3) {
            printf("\n[Search] \n");
            search(user, &person);
        }
        else if (input == 4) {
            printf("\n[Print All] \n");
            printAll(user, &person);
        }
        else if (input == 5) {
            saveFile(user, &person);
            return 0;
        }
        else
            printf("\nError! ReTry! \n\n");
    }

    return 0;

}



//데이터를 파일에 저장하는 함수
int saveFile(User* ptr, int* num) {

    if (*num > 0) {
        int i, state;
        FILE* fp = fopen("data.txt", "wt");



        /* fopen함수는 오류발생시 NULL을 리턴하므로
        파일 개방 중 오류발생시 프로그램을 종료 */
        if (fp == NULL) {
            printf("File Open Error!\n");
            return 1;
        }



        //구조체 배열에 저장된 데이터를 파일에 저장
        //줄바꿈으로 구분하여 저장
        for (i = 0; i < *num; i++) {
            fprintf(fp, "%s %s %s", ptr[i].name, ptr[i].phone, ptr[i].memo);
            fputc('\n', fp);
        }



        /* fclose함수는 종료시 오류가 발생하면
        0이 아닌 다른값을 리턴하므로 비정상 종료로 판단되면
        안내후 프로그램을 종료 */
        state = fclose(fp);
        if (state != 0) {
            printf("File Close Error!\n");
            return 1;
        }
        printf("\n  Data Save \n");
        return 0;
    }

    else {
        printf("\n  Exit \n");
        return 0;
    }
}



int openFile(User* ptr, int* num) {
    int state;
    FILE* fp = fopen("data.txt", "rt");

    if (fp == NULL) {
        printf("File Open Error!\n");
        return 1;
    }


    //파일에 저장된 데이터를 구조체 배열에 저장
    while (1) {
        char temp[512];
        int count = 0, incount = 0;
        fscanf(fp, "%s", &temp);

        int i;
        for (i = 0; temp[i] != '\0'; incount++, i++)
        {
            if (temp[i] == ':')
            {
                if (count == 0)
                    ptr[*num].name[incount] = '\0';

                else if (count == 1)
                    ptr[*num].phone[incount] = '\0';

                incount = 0;
                count++;
            }
            else
            {
                if (count == 0)
                    ptr[*num].name[incount] = temp[i];

                else if (count == 1)
                    ptr[*num].phone[incount] = temp[i];

                else if (count == 2) {
                    ptr[*num].memo[incount] = temp[i];
                }
            }
        }
        ptr[*num].memo[incount] = '\0';

        if (feof(fp) != 0)
            break;
        (*num)++;
    }




    state = fclose(fp);
    if (state != 0) {
        printf("File Close Error!\n");
        return 1;
    }

    return 0;
}



//사용자의 정보를 삽입하는 함수
void insert(User* ptr, int* num) {

    //유저정보가 꽉 차지 않으면
    if (*num < MAX_NUM) {
        printf("Input Name: ");
        scanf("%s", ptr[*num].name);
        printf("Input Tel Number: ");
        scanf("%s", ptr[*num].phone);
        printf("Input Memo");
        scanf("%s", ptr[*num].memo);

        (*num)++;
        printf("  Data Inserted \n\n");
    }
    //유저 정보가 꽉 차면
    else
        printf("  Data Full \n\n");
}



//사용자의 정보를 삭제하는 함수
int deleted(User* ptr, int* num) {
    char name[30];
    int i, j;



    //유저 정보가 한개라도 남아있으면
    if (*num > 0) {
        printf("Input Name: ");
        scanf("%s", name);



        for (i = 0; i < MAX_NUM; i++) {
            //문자열이므로 비교하기위해 strcmp사용
            if (strcmp(name, ptr[i].name) == 0) {

                (*num)--;
                printf("  Data Deleted \n\n");

                //데이터가 가득 차지 않았다면
                if (i != MAX_NUM - 1) {
                    for (j = i; j < MAX_NUM; j++) {
                        //문자열이므로 strcpy를 사용하여 데이터 복사
                        strcpy(ptr[j].name, ptr[j + 1].name);
                        strcpy(ptr[j].phone, ptr[j + 1].phone);
                        strcpy(ptr[j].memo, ptr[j + 1].memo);
                    }
                    //구조체 배열의 마지막을 NULL로 바꿈
                    *ptr[MAX_NUM - 1].name = NULL;
                    *ptr[MAX_NUM - 1].phone = NULL;
                    *ptr[MAX_NUM - 1].memo = NULL;
                }


                //데이터가 가득 찼다면
                else {
                    //구조체 배열의 마지막을 NULL로 바꿈
                    *ptr[MAX_NUM - 1].name = NULL;
                    *ptr[MAX_NUM - 1].phone = NULL;
                    *ptr[MAX_NUM - 1].memo = NULL;
                }
                return 0;
            }
        }
        printf("Not Found \n\n");
        return 0;
    }


    //저장된 유저 정보가 없다면
    else {
        printf("  No Data \n\n");
        return 0;
    }
}



//사용자의 정보를 검색하는 함수
int search(User* ptr, int* num) {
    char name[30];
    int i;



    //저장된 데이터가 있다면
    if (*num > 0) {
        printf("Input Name: ");
        scanf("%s", name);



        for (i = 0; i < MAX_NUM; i++) {
            //strcmp는 문자열이 일치할때 0을 반환
            //0은 C언어에서 거짓을 의미
            //그러므로 ! 을 붙여 참으로 변경하여 실행
            if (!strcmp(name, ptr[i].name)) {

                printf("Name : %s ", ptr[i].name);
                printf("Phone : %s ", ptr[i].phone);
                printf("Memo : %s \n", ptr[i].memo);


                printf("  Data Found \n\n");
                return 0;
            }
        }
        printf("Not Found \n\n");
        return 0;
    }
    else {
        printf("  No Data \n\n");
        return 0;
    }
}



//저장된 모든 이름과 전화번호 정보를 출력하는 함수
void printAll(User* ptr, int* num) {
    int i = 0;

    if (*num > 0) {
        for (i = 0; i < *num; i++) {
            printf("Name : %s ", ptr[i].name);
            printf("Phone : %s ", ptr[i].phone);
            printf("Tel : %s \n", ptr[i].memo);
        }
        printf("  Data Print \n\n");
    }
    else
        printf("  No Data \n\n");
}


/*
int openFile(User* ptr, int* num) {
    int state;
    FILE* fp = fopen("data.txt", "rt");

    if (fp == NULL) {
        printf("File Open Error!\n");
        return 1;
    }


    //파일에 저장된 데이터를 구조체 배열에 저장
    while (1) {
        char temp[512];
        int count = 0, incount = 0;
        fscanf(fp, "%s", &temp);

        int i;
        for (i = 0; temp[i] != '\0'; i++)
        {
            if (temp[i] == ':')
            {
                if (count == 0)
                    ptr[*num].name[incount] = '\0';

                else if (count == 1)
                    ptr[*num].phone[incount] = '\0';

                incount = 0;
                count++;
            }
            else
            {
                if (count == 0)
                    ptr[*num].name[incount] = temp[i];

                else if (count == 1)
                    ptr[*num].phone[incount] = temp[i];

                else if (count == 2)
                    ptr[*num].memo[incount] = temp[i];
            }
            incount++;
        }
        ptr[*num].memo[++incount] = '\0';

        if (feof(fp) != 0)
            break;
        (*num)++;
    }



 
    state = fclose(fp);
    if (state != 0) {
        printf("File Close Error!\n");
        return 1;
    }

    return 0;
}


__________________________________________________
#include <stdio.h>
#include <string.h>



//추후 유지보수를 편히 하기위해 100이란 숫자를
//MAX_NUM으로 설정, 100을 200으로 바꾸면
//MAX_NUM은 200이 됨
#define MAX_NUM 100



//사용자의 정보를 저장하는 구조체
typedef struct {
    char name[30];
}User;

int main()
{
    char term[512];
    User user[MAX_NUM];
    int people = 0;
    FILE* fp = fopen("data.txt", "r");
    int end = 0;
    fscanf(fp, "%s", term);
    for (int i = 0, incount = 0; term[i] != '\0'; i++, incount++)
    {
        user[people].name[incount] = term[i];
        end = incount;
    }
    user[people].name[++end] = '\0';
    printf("%s", user[people].name);

    return 0;
}

*/