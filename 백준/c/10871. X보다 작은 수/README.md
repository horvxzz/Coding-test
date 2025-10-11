#include<stdio.h>
int main()
{
	int x = 0, n = 0;
	scanf("%d %d", &x, &n);
	int a[10000];
	for (int i = 0; i < x; i++) {
		scanf("%d", &a[i]);
		if (a[i] < n) {
			printf("%d ", a[i]);
	}
	}
	return 0;
}