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
int lines, words = 0;
int yylex();
int yywrap();

%}

WORD [a-zA-Z0-9]+
TABSPACES [ \t]+
WHITESYMBOLS [ \f\r\t\v]+
%%
{WORD}              {
                        printf("%s", yytext);
                        words++;
                    };
^{WHITESYMBOLS}                             ;
{WHITESYMBOLS}$                             ;
{TABSPACES}                      printf(" ");
\n                                   lines++;
%%

int yywrap() {
    printf("\n%d %d", lines, words);
    return 1;
}

main()
{
    return yylex();
}

