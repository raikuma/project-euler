#include <stdio.h>
#include <string.h>
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

int isDoublePD(char *s) {
    int l = strlen(s);
    if (isPanDigital(s) && isPanDigital(s+l-9)) {
        return 1;
    }
    return 0;
}

int main() {
    mpz_t n1, n2;
    mpz_t *f1 = &n1, *f2 = &n2, *t;
    char *str;
    int i;
    int k;

    mpz_init(n1);
    mpz_init(n2);
    mpz_set_ui(n1, 1);
    mpz_set_ui(n2, 1);
    k = 2;

    while (1) {
        mpz_add(*f1, *f1, *f2);
        k += 1;
        str = mpz_get_str(NULL, 10, *f1);
        if (isDoublePD(str)) {
            printf("%s %d\n", str, k);
            break;
        }
        t = f1;
        f1 = f2;
        f2 = t;
    }

    mpz_clear(n1);
    mpz_clear(n2);
    return 0;
}