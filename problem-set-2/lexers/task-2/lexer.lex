/*
 * C99 comments remover
 */

%{
int lines, words = 0;
int yylex();
int yywrap();

%}

STRING_START        "\""
MUL_DOC_COM_START   ([ \t]*"/**"|^[ \t]*"/**")
ONE_DOC_COM_START   ([ \t]*"///"|^[ \t]*"///")

ONE_COM_START       ([ \t]*"//"|^[ \t]*"//")

%x STRING
%x MUL_DOC_COM
%x ONE_DOC_COM
%x ONE_COM
%%

{STRING_START} {
    printf("%s", yytext);
    BEGIN(STRING);
}
<STRING>{
    "\\\""                                  ECHO;
    \n                                      ECHO;
    "\""                                    {
                                                printf("%s", yytext);
                                                BEGIN(0);
                                            }
    .                                       ECHO;
}

{MUL_DOC_COM_START} {
    BEGIN(MUL_DOC_COM);
}

<MUL_DOC_COM>{
    "*/"[ \t]*$  BEGIN(0);
    "*/"         BEGIN(0);
    .   ;
    \n  ;
}

{ONE_DOC_COM_START} {
    BEGIN(ONE_DOC_COM);
}

<ONE_DOC_COM>{
    "\\"[ \t]*\n         ;
    .                   ;
    \n              BEGIN(0);
}

{ONE_COM_START} {
    BEGIN(ONE_COM);
}

<ONE_COM>{
        "\\"[ \t]*\n         ;
    .                   ;
    \n              { ECHO; BEGIN(0); }
}

. ECHO;
\n printf("\n");
%%

int yywrap() {
    return 1;
}

main()
{
    return yylex();
}

