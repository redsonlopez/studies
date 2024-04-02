#include <stdio.h>

int main() {
	double number, sum = 0.0;
	printf("Digite os números para soma e 0 para finalizar!\n");
	do {
		printf("Digite um número: ");
		scanf("%lf", &number);
		sum += number;
	}
	while (number != 0.0);
	printf("Soma = %.2lf", sum);
	printf("\n");
	return 0;
}

