#include <stdio.h>

int main() {
	int S, M, L;
	scanf("%d", &S);
	scanf("%d", &M);
	scanf("%d", &L);

	puts(S + 2*M + 3*L > 9 ? "happy" : "sad");
}
