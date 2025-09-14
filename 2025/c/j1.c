#include <stdio.h>

int main() {
	int N, C, P;

	scanf("%d", &N);
	scanf("%d", &C);
	scanf("%d", &P);

	puts(N <= C * P ? "yes" : "no");
}
