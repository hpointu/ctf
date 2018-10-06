unsigned char validate_key(unsigned char* a1) {
    int size;
    int v7;
    int i;
    unsigned int c;
    signed char al10;
    unsigned int ebx11;
    unsigned int eax12;
    signed char al13;

    size = strlen(a1);
    v7 = 0;
    i = 0;
    while (i < size - 1 ) {
        c = a1[i];
        al10 = ord(c);
        v7 = v7 + (i + 1) * (al10 + 1);
        ++i;
    }
    ebx11 = __intrinsic() >> 3;
    eax12 = *reinterpret_cast<unsigned char*>(reinterpret_cast<int>(a1) + (size - 1));
    al13 = ord(static_cast<int>(*reinterpret_cast<signed char*>(&eax12)));
    return static_cast<unsigned char>(reinterpret_cast<uint1_t>(v7 - ((ebx11 << 3) + ebx11 << 2) == static_cast<int>(al13)));
}
