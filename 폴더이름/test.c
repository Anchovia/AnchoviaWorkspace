#include <stdio.h>
#include <string.h>



//���� ���������� ���� �ϱ����� 100�̶� ���ڸ�
//MAX_NUM���� ����, 100�� 200���� �ٲٸ�
//MAX_NUM�� 200�� ��
#define MAX_NUM 100



//������� ������ �����ϴ� ����ü
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
    User user[MAX_NUM]; //����� ������ ������ ����ü �迭
    int person = 0; //����� user��



    openFile(user, &person);//����� �����͸� �ҷ����� �Լ�



    //�޴� ����
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



//�����͸� ���Ͽ� �����ϴ� �Լ�
int saveFile(User* ptr, int* num) {

    if (*num > 0) {
        int i, state;
        FILE* fp = fopen("data.txt", "wt");



        /* fopen�Լ��� �����߻��� NULL�� �����ϹǷ�
        ���� ���� �� �����߻��� ���α׷��� ���� */
        if (fp == NULL) {
            printf("File Open Error!\n");
            return 1;
        }



        //����ü �迭�� ����� �����͸� ���Ͽ� ����
        //�ٹٲ����� �����Ͽ� ����
        for (i = 0; i < *num; i++) {
            fprintf(fp, "%s %s %s", ptr[i].name, ptr[i].phone, ptr[i].memo);
            fputc('\n', fp);
        }



        /* fclose�Լ��� ����� ������ �߻��ϸ�
        0�� �ƴ� �ٸ����� �����ϹǷ� ������ ����� �ǴܵǸ�
        �ȳ��� ���α׷��� ���� */
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


    //���Ͽ� ����� �����͸� ����ü �迭�� ����
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



//������� ������ �����ϴ� �Լ�
void insert(User* ptr, int* num) {

    //���������� �� ���� ������
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
    //���� ������ �� ����
    else
        printf("  Data Full \n\n");
}



//������� ������ �����ϴ� �Լ�
int deleted(User* ptr, int* num) {
    char name[30];
    int i, j;



    //���� ������ �Ѱ��� ����������
    if (*num > 0) {
        printf("Input Name: ");
        scanf("%s", name);



        for (i = 0; i < MAX_NUM; i++) {
            //���ڿ��̹Ƿ� ���ϱ����� strcmp���
            if (strcmp(name, ptr[i].name) == 0) {

                (*num)--;
                printf("  Data Deleted \n\n");

                //�����Ͱ� ���� ���� �ʾҴٸ�
                if (i != MAX_NUM - 1) {
                    for (j = i; j < MAX_NUM; j++) {
                        //���ڿ��̹Ƿ� strcpy�� ����Ͽ� ������ ����
                        strcpy(ptr[j].name, ptr[j + 1].name);
                        strcpy(ptr[j].phone, ptr[j + 1].phone);
                        strcpy(ptr[j].memo, ptr[j + 1].memo);
                    }
                    //����ü �迭�� �������� NULL�� �ٲ�
                    *ptr[MAX_NUM - 1].name = NULL;
                    *ptr[MAX_NUM - 1].phone = NULL;
                    *ptr[MAX_NUM - 1].memo = NULL;
                }


                //�����Ͱ� ���� á�ٸ�
                else {
                    //����ü �迭�� �������� NULL�� �ٲ�
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


    //����� ���� ������ ���ٸ�
    else {
        printf("  No Data \n\n");
        return 0;
    }
}



//������� ������ �˻��ϴ� �Լ�
int search(User* ptr, int* num) {
    char name[30];
    int i;



    //����� �����Ͱ� �ִٸ�
    if (*num > 0) {
        printf("Input Name: ");
        scanf("%s", name);



        for (i = 0; i < MAX_NUM; i++) {
            //strcmp�� ���ڿ��� ��ġ�Ҷ� 0�� ��ȯ
            //0�� C���� ������ �ǹ�
            //�׷��Ƿ� ! �� �ٿ� ������ �����Ͽ� ����
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



//����� ��� �̸��� ��ȭ��ȣ ������ ����ϴ� �Լ�
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


    //���Ͽ� ����� �����͸� ����ü �迭�� ����
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



//���� ���������� ���� �ϱ����� 100�̶� ���ڸ�
//MAX_NUM���� ����, 100�� 200���� �ٲٸ�
//MAX_NUM�� 200�� ��
#define MAX_NUM 100



//������� ������ �����ϴ� ����ü
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