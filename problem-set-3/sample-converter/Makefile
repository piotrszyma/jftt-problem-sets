CC = cc
all:
	make flex && make bison && make cc

flex:
	flex gram.l

bison:
	bison -d gram.y

cc:
	cc lex.yy.c gram.tab.c -lm

clean:
	rm *.out && rm *.tab.* && rm yy.c
