#include <stdio.h>

int phi(int n) {
	int r = n;
	int d = 2;
	int p = n;

	while (r > 1) {
		if (r % d == 0) {
			p -= p / d;
			while (r % d == 0) {
				r = r / d;
			}
		}
		d++;
	}

	return p;
}

int main() {
	double m = 0;
	int mn = 1;
	int i;

	for (i = 2; i < 1000000; i++) {
		int p = phi(i);
		if (m < (double)i / p) {
			m = (double)i / p;
			mn = i;
		}
		if (i % 10000 == 0) {
			printf("%d\n", i);
		}
	}

	printf("%lf %d", m, mn);
}