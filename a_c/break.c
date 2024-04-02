#include <stdio.h>

int main() {
	int number, sum = 0;
	while (1) {
		printf("Enter a number: ");
		scanf("%d", &number);
		if (number < 0) {
			break;
		}
		sum += number;
	}
	printf("sum = %d", sum);
	printf("\n");
	return 0;
}

