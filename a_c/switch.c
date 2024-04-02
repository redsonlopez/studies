#include <stdio.h>

int main() {
	char operator;
	int n1= 14, n2= 5, result;
	printf("Escolha um operador (+, -, *, /): ");
	scanf("%c", &operator);
	switch (operator) {
	case '+':
		printf("Resultado = %d", n1 + n2);
		break;
	case '-':
		printf("Resultado = %d", n1 - n2);
		break;
	case '*':
		printf("Resultado = %d", n1 * n2);
		break;
	case '/':
		printf("Resultado = %d", n1 / n2);
		break;
	default:
		printf("Erro! Operador incorreto");
	}
	printf("\n");
	return 0;
}

