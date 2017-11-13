/*
 * C99 comments remover
 */

%{
int lines, words = 0;
int yylex();
int yywrap();

%}

INLINE_COMMENT_START "//"
MULTILINE_COMMENT_START "/*"
%x INLINE_COMMENT
%x MULTILINE_COMMENT
%%

{INLINE_COMMENT_START}             BEGIN(INLINE_COMMENT);
<INLINE_COMMENT>{
                .                                       ;
                \\\n                                    ;
                \n                              BEGIN(0);
}
{MULTILINE_COMMENT_START}       BEGIN(MULTILINE_COMMENT);
<MULTILINE_COMMENT>{
                .                                    ;
                \n                                   ;
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

