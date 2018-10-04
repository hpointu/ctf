import sys
from functools32 import lru_cache

sys.setrecursionlimit(20000000)


@lru_cache(maxsize=100000000)
def calc(edi):
    if edi > 4:
        eax2 = calc(edi - 1);
        eax3 = calc(edi - 2);
        eax4 = calc(edi - 3);
        eax5 = calc(edi - 4);
        eax6 = calc(edi - 5);
        v7 = eax6 * 0x1234 + (eax2 - eax3 + (eax4 - eax5));
    else:
        v7 = edi * edi + 0x2345;
    return v7;


if __name__ == "__main__":
    print(calc(int(sys.argv[1])))
