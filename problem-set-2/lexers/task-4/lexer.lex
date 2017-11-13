/*
 * Sample Scanner1:
 * Usage: (1) $ flex sample1.lex
 *        (2) $ gcc lex.yy.c -lfl
 *        (3) $ ./a.out
 *            stdin> username
 *	          stdin> Ctrl-D
 * Question: What is the purpose of '%{' and '%}'?
 *           What else could be included in this section?
 */

%{
#include <math.h>

#define STACK_SIZE  100
#define TRUE          1
#define FALSE         0


// Stack implementation



int stack[STACK_SIZE];
int stackPtr = -1;

int isEmpty() {
    if(stackPtr == -1) {
        return TRUE;
    } else {
        return FALSE;
    }
}

int isFull() {
    if(stackPtr == STACK_SIZE - 1) {
        return TRUE;
    } else {
        return FALSE;
    }
}

int push(int number) {
    if(!isFull()) {
        stack[++stackPtr] = number;
    } else {
        return -1;
    }
}

int pop() {
    if(!isEmpty()) {
        return stack[stackPtr--];
    } else {
        return -1;
    }
}

// LEX initializer
// a - b = -b + a
int yylex();
int yywrap();

int UNKNOWN = FALSE;
int numberCtr = 0;
int operatorCtr = 0;

%}


digit (-){0,1}[0-9]+

%%
{digit}     {
                 push(atoi(yytext));
                 numberCtr++;
            }
"+"         {
                push(pop() + pop());
                operatorCtr++;
            }
"-"         {
                //TODO: make it work better
                int fNumber = pop();
                push(pop() - fNumber);
                operatorCtr++;
            }
"*"         {
                operatorCtr++;
                push(pop() * pop());
            }
"%"         {

                int fNumber = pop();
                push(pop() % fNumber);
                operatorCtr++;
            }
"/"         {
                operatorCtr++;
                int fNumber = pop();
                push(pop() / fNumber);
            }
"^"         {
                operatorCtr++;
                int fNumber = pop();
                push(pow(pop(),  fNumber));
            }
" "        ;
.           {
                printf("\nError: unknown symbol \"%s\"", yytext);
                UNKNOWN = TRUE;
            }
%%

int yywrap() {
    if(UNKNOWN == TRUE) {
        return 1;
    } else if(operatorCtr < numberCtr - 1) {
        printf("Error: not enough operators\n");
    } else if(numberCtr <= operatorCtr) {
        printf("Error: not enough arguments\n");
    } else if(UNKNOWN == FALSE) {
        printf("= %d\n", pop());
    }
    return 1;
}

main()
{
    return yylex();
}

