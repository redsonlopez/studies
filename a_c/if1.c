#include <stdio.h>

int main() {
	int n1;
	printf("Digite um número ímpar: ");
	scanf("%d", &n1);
	if (n1 % 2 == 0) {
		printf("%d não é um número ímpar!\n", n1);
	}
	else {
		printf("Parabéns, %d é ímpar!\n", n1);
	}
	return 0;
}

