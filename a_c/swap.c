#include <stdio.h>

int main() {
	int n1= 5, n2= 4, temp;

	//Increases and decreases '1'
	++n1;
	--n2;
	printf("Increases and decreases\n");
	printf("n1 = %d\n", n1);
	printf("n2 = %d", n2);
	printf("\n");

	//Swapping
	temp= n1;
	n1= n2;
	n2= temp;
	printf("Swapping\n");
	printf("n1 = %d\n", n1);
	printf("n2 = %d", n2);
	printf("\n");

	//Size in bytes
	printf("int size: %zu", sizeof (n1));
	printf("\n");
	return 0;
}

