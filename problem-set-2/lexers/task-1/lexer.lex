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
#define TRUE    1
#define FALSE   0

int lines, words = 0;
int isEmpty = TRUE;
int yylex();
int yywrap();

%}

WORD [a-zA-Z0-9]+
TABSPACES [ \t]+
WHITESYMBOLS [ \f\r\t\v]+
%%
{WORD}              {
                        isEmpty = FALSE;
                        printf("%s", yytext);
                        words++;
                    };
^{WHITESYMBOLS}                            {isEmpty = FALSE; }
{WHITESYMBOLS}$                            {isEmpty = FALSE; }
{TABSPACES}                   {isEmpty = FALSE; printf(" "); }
\n                                {isEmpty = FALSE; lines++; }
%%

int yywrap() {
    if(lines == 0 & isEmpty == FALSE) lines = 1;
    printf("\n%d %d", lines, words);
    return 1;
}

main()
{
    return yylex();
}

