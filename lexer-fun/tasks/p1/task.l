%{
#include<stdio.h>

int yylex();
int yywrap();
int NL=0;
int NW=0;
%}
%%
^\n                 ;
^[ \f\r\t\v]+\n     ;
[ \f\r\t\v]+$       ;
^[ \f\r\t\v]+       ;
[ \t]+        printf(" ");
\n                  { NL++; printf("\n"); }

%%

int yywrap() {
    printf("---\n\%d\n", NL);
    return 1;
}

int main() {
    return yylex();
}
