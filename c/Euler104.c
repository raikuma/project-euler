#include <stdio.h>
#include <gmp.h>

int isPanDigital(char *s) {
    char d[10] = {0};
    int i;
    for (i = 0; i < 9; i++) {
        d[s[i]-'0']++;
    }
    for (i = 1; i <= 9; i++) {
        if (d[i] != 1) {
            return 0;
        }
    }
    return 1;
}

int main() {
    return 0;
}