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
int yylex();
int yywrap();

%}
START_COMMENT ^%.*\n
COMMENT %.*\n
ESCAPED \\%

%%
{ESCAPED}                     ECHO;
{START_COMMENT}                   ;
{COMMENT}             printf("\n");
.                             ECHO;

%%

int yywrap() {
    return 1;
}

main()
{
    return yylex();
}

