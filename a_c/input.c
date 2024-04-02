#include <stdio.h>

int main() {
	int n1;
	double n2;
	float n3, n4;

	printf("Digite dois números, para soma e quadrado: ");
	scanf("%d%lf", &n1, &n2);
	n3= n1 + n2;
	n4= n1 * n2;
	
	printf("n3 = %.2f\nn4 = %.2f", n3, n4);
	printf("\n");
	return 0;
}

