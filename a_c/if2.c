#include <stdio.h>

int main() {
	double n1= 6.0, n2= -4.5, n3= 2.5;
	if (n1 >= n2 && n1 >= n3) {
		printf("%.2lf é o maior número.", n1);
		}
	else if (n2 >= n1 && n2 >= n3) {
		printf("%2.lf é o maior número.", n2);
		}
	else {
		printf("%.2lf é o maior.", n3);
		}
	printf("\n");
	return 0;
}

