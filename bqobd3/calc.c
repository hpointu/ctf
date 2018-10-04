#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

uint32_t calc(uint32_t edi, uint32_t *cache) {
    uint32_t eax2;
    uint32_t eax3;
    uint32_t eax4;
    uint32_t eax5;
    uint32_t eax6;
    uint32_t v7;

    if(cache[edi] != 0) {
      return cache[edi];
    }

    if (edi > 4) {
        eax2 = calc(edi - 1, cache);
        eax3 = calc(edi - 2, cache);
        eax4 = calc(edi - 3, cache);
        eax5 = calc(edi - 4, cache);
        eax6 = calc(edi - 5, cache);
        v7 = eax6 * 0x1234 + (eax2 - eax3 + (eax4 - eax5));
    } else {
        v7 = edi * edi + 0x2345;
    }

    cache[edi] = v7;

    return v7;
}

int main(int argc, char **argv) {
    uint32_t cache[150000] = {0};
    uint32_t result;
    result = calc(0x18f4b, cache);
    printf("%d\n", result);
}
