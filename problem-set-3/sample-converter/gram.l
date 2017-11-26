%{
#include "gram.tab.h"

extern int yylval;
%}
COMMENT ^#.*(\\\n)+.*\n
MULTILINE (\\\n)

%%
{COMMENT}   ;
{MULTILINE} ;
[0-9]+ {yylval=atoi(yytext); return NUM;}

\n      return EOF;
.       return *yytext;
%%

int yywrap(){
    return 1;
}