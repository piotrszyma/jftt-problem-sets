/*
 * C99 comments remover
 */

%{
int lines, words = 0;
int yylex();
int yywrap();
int DOCS = 0 ;

%}

STRING_START        "\""
MUL_DOC_COM_START   [ \t]*"/**"
ONE_DOC_COM_START   ([ \t]*"///")

ONE_COM_START       ([ \t]*"//")
MUL_COM_START       [ \t]*"/*"

%x STRING
%x MUL_DOC_COM
%x ONE_DOC_COM
%x ONE_COM
%x MUL_COM
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
    if(DOCS) { printf("%s", yytext); }
}

<MUL_DOC_COM>{
    "*/"[ \t]*$  {
                    BEGIN(0);
                    if(DOCS) { printf("%s", yytext); }
                 };
    "*/"         {
                    BEGIN(0);
                    if(DOCS) { printf("%s", yytext); }
                 };
    .           { if(DOCS) { printf("%s", yytext); } };
    \n          { if(DOCS) { printf("%s", yytext); } };
}

{ONE_DOC_COM_START} {
    BEGIN(ONE_DOC_COM);
    if(DOCS) { printf("%s", yytext); }
}

<ONE_DOC_COM>{
    "\\"[ \t]*\n        { if(DOCS) { printf("%s", yytext); } } ;
    .                 { if(DOCS) { printf("%s", yytext); } };
    \n              { ECHO; BEGIN(0); }
}

{ONE_COM_START} {
    BEGIN(ONE_COM);
}

<ONE_COM>{
    "\\"[ \t]*\n         ;
    .                    ;
    \n              { ECHO; BEGIN(0); }
}
{MUL_COM_START} {
    BEGIN(MUL_COM);
}

<MUL_COM>{
    "*/"[ \t]*$  BEGIN(0);
    "*/"         BEGIN(0);
    .   ;
    \n  ;
}

. ECHO;
\n printf("\n");
%%

int yywrap() {
    return 1;
}

main(int argc, char* argv[])
{
    if (argc != 2 ) {
        return yylex();
    }
    if( strcmp(argv[1], "--docs") == 0 )  {
        DOCS = 1;
    }
    return yylex();
}

