#include <stdio.h>

int addNumbers(int, int);

int main() {
	int a= 6, b= 8, result;

	result= addNumbers(a, b);
	printf("sum = %d", result);
	printf("\n");

	return 0;
}

int addNumbers(int n1, int n2) {
	int sum;
	sum= n1 + n2;
	return sum;
}

