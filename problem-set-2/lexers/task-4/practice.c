#include <math.h>
#include <stdio.h>
#include <stdlib.h>

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
    if(stackPtr == STACK_SIZE) {
        return TRUE;
    } else {
        return FALSE;
    }
}

int push(const int number) {
    if(!isFull()) {
        stack[stackPtr] = number;
        stackPtr++;
    } else {
        return -1;
    }
}

int pop() {
    if(!isEmpty()) {
        stackPtr--;
        return stack[stackPtr + 1];
    } else {
        return -1;
    }
}


int main() {
//    char* word = "abc";
//    printf("%d\n", calculate(1, 2, '+'));
    printf("%d", 4/3);
    printf("%d", 3/4);
    return 0;
}