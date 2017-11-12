	int double_a = 0, tripple_a = 0;
%%

aaa			tripple_a++;
aa			double_a++;
%%

main() {
	yylex();
	printf("# of tripple as = %d, # of double as = %d\n", tripple_a, double_a);
}
