%{
#define PRIME 1234577
#define TRUE 1
#define FALSE 0

#include <stdio.h>

int modPow(int a, int b) {
    if(a == 0) {
        return 0;
    }
    if(b == 0) {
        return 1;
    }
    int solution = 1;
    while(b--) {
        solution = (solution * a) % PRIME;
    }
    return solution;
}

int mod(int a) {
    while(a < 0) {
        a += PRIME;
    }
    return a % PRIME;
}

// C function for extended Euclidean Algorithm
int gcdExtended(int a, int b, int *x, int *y)
{
    // Base Case
    if (a == 0)
    {
        *x = 0;
        *y = 1;
        return b;
    }
    int x1, y1; // To store results of recursive call
    int gcd = gcdExtended(b%a, a, &x1, &y1);
 
    // Update x and y using results of recursive
    // call
    *x = y1 - (b/a) * x1;
    *y = x1;
 
    return gcd;
}

int modDiv(int a, int b) {
    int x, y;
    gcdExtended(b, PRIME, &x, &y);
    return (int)(((unsigned long int)a * (unsigned long int)mod(x)) % (unsigned long int)PRIME);
}

%}
%token NUM
%left '+' '-'
%left '*' '/'
%precedence NEGATIVE
%right '^'

%%
S:  E {printf("\nWynik: %d\n", mod($1));}
    | {printf("\n");}
    ;
E:  E '+' E { printf("+ ");  $$ = ($1 + $3); }
    |   E '*' E {printf("* "); $$ = ($1 * $3); }
    |   E '-' E {printf("- "); $$ = ($1 - $3); }
    |   E '^' E {printf("^ "); $$ = modPow($1, $3); }
    |   E '/' E {printf("/ "); $$ = modDiv($1, $3); }    
    |   '-' NE %prec NEGATIVE { $$ = -$2; }
    |   NUM     { printf("%d ",  yylval); $$ = $1; }
    |   '(' E ')' { $$ = $2; }
    ;

NE: NUM { printf("%d ", mod((-1) * yylval));  $$ = $1; }
%%

int main(){
    while(TRUE) {
        yyparse();
    }
}

int yyerror (char *msg) {
    printf ("Error");
    return 0;
}