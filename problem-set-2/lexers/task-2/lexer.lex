/*
 * C99 comments remover
 */

%{
int lines, words = 0;
int yylex();
int yywrap();

%}

INLINE_COMMENT_START [ \t]*"//"
INLINE_COMMENT_START_AT_BEGINNING ^[ \t]*("//")
MULTILINE_COMMENT_START [ \t]*"/*"
MULTILINE_COMMENT_START_AT_BEGINNING ^[ \t]*("/*")

STRING_START "\""

%x INLINE_COMMENT_FROM_BEGINNING
%x INLINE_COMMENT
%x MULTILINE_COMMENT
%x MULTILINE_COMMENT_FROM_BEGINNING
%x STRING
%%

{STRING_START}                  {
    printf("%s", yytext);
    BEGIN(STRING);
}
<STRING>{
    "\\\""                                  ECHO;
    .                                       ECHO;
    \n                                      ECHO;
    "\""                                    {
                                                printf("%s", yytext);
                                                BEGIN(0);
                                            }
}

{INLINE_COMMENT_START_AT_BEGINNING}             BEGIN(INLINE_COMMENT_FROM_BEGINNING);
<INLINE_COMMENT_FROM_BEGINNING>{
                .                                      ;
                \\n                                    ;
                \n                              {
                                                BEGIN(0);
                                                }
}

{INLINE_COMMENT_START}             BEGIN(INLINE_COMMENT);
<INLINE_COMMENT>{
                .                                       ;
                \\n                                    ;
                \n                              {
                                                printf("\n");
                                                BEGIN(0);
                                                }
}

{MULTILINE_COMMENT_START_AT_BEGINNING}      BEGIN(MULTILINE_COMMENT_FROM_BEGINNING);
<MULTILINE_COMMENT_FROM_BEGINNING>{

                .                                    ;
                \n                                   ;
                \".*\"                               ;
                ("*/\n"|"*/")                BEGIN(0);

}

{MULTILINE_COMMENT_START}       BEGIN(MULTILINE_COMMENT);
<MULTILINE_COMMENT>{
                .                                    ;
                \n                                   ;
                \".*\"                               ;
                ("*/\n"|"*/")                BEGIN(0);
}
%%

int yywrap() {
    return 1;
}

main()
{
    return yylex();
}

