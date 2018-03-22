#include <stdio.h>
#include <math.h>

int is_squre(long n) {
    return sqrt(n) == (int)(sqrt(n));
}

int count(long a, long b, long c) {
    long s = pow(a, 2) + pow(b+c, 2);
    if (is_squre(s))
        return 1;
    return 0;
}

int main() {
    int m = 0;
    int cnt = 0;

    while (cnt < 1000000) {
        m++;
        int a = m;
        for (int b = 1; b < m+1; b++) {
            for (int c = b; c < m+1; c++) {
                cnt += count(a, b, c);
            }
        }
        printf("%d\n", cnt);
    }
    printf("%d %d\n", m, cnt);
}