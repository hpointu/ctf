
void fun_80483c0();

void fun_8048360();

void fun_80482f4() {
    int32_t ebx1;

    fun_80483c0();
    if (*reinterpret_cast<int32_t*>(ebx1 + 0x18e3 - 4)) {
        fun_8048360();
    }
    return;
}

void fun_80483c0() {
    return;
}

int32_t __gmon_start__ = 0x8048366;

void fun_8048360() {
    goto __gmon_start__;
}

int32_t __libc_start_main(int32_t a1, int32_t a2);

int32_t fun_80483d0() {
    int32_t eax1;
    int32_t v2;

    eax1 = 3;
    if (!1 && (eax1 = 0, !1)) {
        eax1 = __libc_start_main(0x8049c10, v2);
    }
    return eax1;
}

struct s0 {
    struct s0* f0;
    struct s0* f4;
    unsigned char f8;
};

uint32_t fun_8048539(struct s0* a1, unsigned char* a2, int32_t a3);

uint32_t fun_804848b(struct s0* a1, unsigned char* a2, unsigned char* a3) {
    uint32_t eax4;
    uint32_t v5;
    unsigned char* v6;
    unsigned char* v7;
    uint32_t eax8;
    uint32_t eax9;
    uint32_t eax10;
    uint32_t eax11;
    uint32_t eax12;
    uint32_t eax13;
    uint32_t eax14;
    uint32_t edx15;
    uint32_t eax16;
    uint32_t eax17;

    if (!a1 || (!a2 || !a3)) {
        eax4 = 0;
    } else {
        v5 = 1;
        v6 = a2;
        v7 = a3;
        while ((eax8 = *v6, !!*reinterpret_cast<signed char*>(&eax8)) && (eax9 = *v7, !!*reinterpret_cast<signed char*>(&eax9))) {
            eax10 = *v7;
            eax11 = fun_8048539(a1, v6, static_cast<int32_t>(*reinterpret_cast<signed char*>(&eax10)));
            v5 = v5 & eax11;
            ++v7;
            while ((eax12 = *v6, *reinterpret_cast<signed char*>(&eax12) == 76) || (eax13 = *v6, *reinterpret_cast<signed char*>(&eax13) == 82)) {
                ++v6;
            }
            ++v6;
        }
        eax14 = *v6;
        *reinterpret_cast<unsigned char*>(&edx15) = reinterpret_cast<uint1_t>(*reinterpret_cast<signed char*>(&eax14) == 0);
        eax16 = *v7;
        *reinterpret_cast<unsigned char*>(&eax16) = reinterpret_cast<uint1_t>(*reinterpret_cast<unsigned char*>(&eax16) == 0);
        eax17 = eax16 & edx15;
        eax4 = v5 & static_cast<uint32_t>(*reinterpret_cast<unsigned char*>(&eax17));
    }
    return eax4;
}

uint32_t fun_8048539(struct s0* a1, unsigned char* a2, int32_t a3) {
    int32_t eax4;
    uint32_t eax5;
    uint32_t eax6;
    uint32_t eax7;
    uint32_t eax8;
    uint32_t eax9;
    struct s0* eax10;
    uint32_t eax11;
    struct s0* eax12;
    uint32_t eax13;
    uint32_t eax14;

    eax4 = a3;
    if (!a1 || (eax5 = *a2, !*reinterpret_cast<signed char*>(&eax5))) {
        eax6 = 0;
    } else {
        eax7 = a1->f8;
        if (*reinterpret_cast<signed char*>(&eax7) != *reinterpret_cast<signed char*>(&eax4)) {
            eax8 = a1->f8;
            if (*reinterpret_cast<signed char*>(&eax8) <= *reinterpret_cast<signed char*>(&eax4)) {
                eax9 = *a2;
                if (*reinterpret_cast<signed char*>(&eax9) != 82) {
                    eax6 = 0;
                } else {
                    eax10 = a1->f4;
                    eax6 = fun_8048539(eax10, a2 + 1, static_cast<int32_t>(*reinterpret_cast<signed char*>(&eax4)));
                }
            } else {
                eax11 = *a2;
                if (*reinterpret_cast<signed char*>(&eax11) != 76) {
                    eax6 = 0;
                } else {
                    eax12 = a1->f0;
                    eax6 = fun_8048539(eax12, a2 + 1, static_cast<int32_t>(*reinterpret_cast<signed char*>(&eax4)));
                }
            }
        } else {
            eax13 = *a2;
            if (*reinterpret_cast<signed char*>(&eax13) != 68) {
                eax6 = 0;
            } else {
                eax14 = a1->f8;
                if (*reinterpret_cast<signed char*>(&eax14) != *reinterpret_cast<signed char*>(&eax4)) {
                    eax6 = 0;
                } else {
                    eax6 = 1;
                }
            }
        }
    }
    return eax6;
}

int32_t malloc = 0x8048346;

struct s0* fun_8048340(int32_t a1) {
    goto malloc;
}

struct s0* fun_8048607(struct s0* a1, int32_t a2) {
    int32_t eax3;
    uint32_t eax4;
    uint32_t eax5;
    struct s0* eax6;
    struct s0* eax7;
    struct s0* eax8;
    struct s0* eax9;
    struct s0* eax10;
    struct s0* eax11;
    uint32_t edx12;

    eax3 = a2;
    if (a1) {
        eax4 = a1->f8;
        eax5 = *reinterpret_cast<unsigned char*>(&eax4);
        if (*reinterpret_cast<signed char*>(&eax5) >= *reinterpret_cast<signed char*>(&eax3)) {
            eax6 = a1->f0;
            eax7 = fun_8048607(eax6, static_cast<int32_t>(*reinterpret_cast<signed char*>(&eax3)));
            a1->f0 = eax7;
            eax8 = a1;
        } else {
            eax9 = a1->f4;
            eax10 = fun_8048607(eax9, static_cast<int32_t>(*reinterpret_cast<signed char*>(&eax3)));
            a1->f4 = eax10;
            eax8 = a1;
        }
    } else {
        eax11 = fun_8048340(12);
        eax11->f0 = reinterpret_cast<struct s0*>(0);
        eax11->f4 = reinterpret_cast<struct s0*>(0);
        edx12 = *reinterpret_cast<unsigned char*>(&eax3);
        eax11->f8 = *reinterpret_cast<unsigned char*>(&edx12);
        eax8 = eax11;
    }
    return eax8;
}

struct s1 {
    struct s1* f0;
    struct s1* f4;
    unsigned char f8;
};

void fun_8048330(int32_t a1, int32_t a2);

void fun_80486a4(struct s1* a1, int32_t a2) {
    struct s1* v3;
    int32_t v4;
    uint32_t eax5;
    int32_t v6;
    struct s1* v7;

    if (a1) {
        v3 = a1->f0;
        fun_80486a4(v3, v4);
        eax5 = a1->f8;
        v6 = *reinterpret_cast<signed char*>(&eax5);
        fun_8048330("%c ", v6);
        v7 = a1->f4;
        fun_80486a4(v7, v6);
    }
    return;
}

int32_t printf = 0x8048336;

void fun_8048330(int32_t a1, int32_t a2) {
    goto printf;
}

struct s0* fun_80486f0(int32_t a1) {
    struct s0* v2;
    int32_t v3;
    uint32_t eax4;
    uint32_t eax5;
    struct s0* eax6;

    v2 = reinterpret_cast<struct s0*>(0);
    v3 = 0;
    while (eax4 = *reinterpret_cast<unsigned char*>(v3 + a1), !!*reinterpret_cast<signed char*>(&eax4)) {
        eax5 = *reinterpret_cast<unsigned char*>(v3 + a1);
        eax6 = fun_8048607(v2, static_cast<int32_t>(*reinterpret_cast<signed char*>(&eax5)));
        v2 = eax6;
        ++v3;
    }
    return v2;
}

int32_t puts = 0x8048356;

void fun_8048350(int32_t a1, unsigned char* a2, unsigned char* a3) {
    goto puts;
}

int32_t exit = 0x8048376;

void fun_8048370(int32_t a1, int32_t a2) {
    goto exit;
}

int32_t __libc_start_main = 0x8048386;

void fun_8048380(int32_t a1, int32_t a2, void* a3, int32_t a4, int32_t a5, int32_t a6, void** a7, int32_t a8) {
    goto __libc_start_main;
}

void fun_8048874() {
    fun_80483c0();
    return;
}

void fun_804832c() {
    signed char* eax1;
    signed char* eax2;
    signed char al3;
    signed char* eax4;
    signed char* eax5;
    signed char al6;

    *eax1 = reinterpret_cast<signed char>(*eax2 + al3);
    *eax4 = reinterpret_cast<signed char>(*eax5 + al6);
}

int32_t g8049af0 = 0;

int32_t fun_8048460() {
    int32_t edx1;
    int32_t v2;
    int32_t eax3;

    edx1 = g8049af0;
    if (!(!edx1 || 1)) {
        __libc_start_main(0x8049af0, v2);
    }
    eax3 = 0;
    if (!1 && !1) {
        eax3 = __libc_start_main(0x8049c10, 0);
    }
    return eax3;
}

void fun_804846d() {
}

struct s2 {
    int32_t f0;
    unsigned char* f4;
    unsigned char* f8;
};

int32_t g8049c0c = 0x8048890;

int32_t fun_804873e(int32_t a1, struct s2* a2) {
    int32_t eax3;
    struct s0* eax4;
    unsigned char* v5;
    unsigned char* v6;
    int32_t v7;
    unsigned char* eax8;
    unsigned char* v9;
    uint32_t eax10;

    eax3 = g8049c0c;
    eax4 = fun_80486f0(eax3);
    if (a1 != 3) {
        fun_8048350("You have the wrong number of arguments for this forest.", v5, v6);
        v7 = a2->f0;
        fun_8048330("%s [password] [string]\n", v7);
        fun_8048370(1, v7);
    }
    eax8 = a2->f8;
    v9 = a2->f4;
    eax10 = fun_804848b(eax4, eax8, v9);
    if (!eax10) {
        fun_8048350("Nope.", eax8, v9);
    } else {
        fun_8048350("You did it! Submit the input as the flag", eax8, v9);
    }
    return 0;
}

void fun_8048861() {
    return;
}

int32_t g8049be8 = 0;

void fun_8048366() {
    goto g8049be8;
}

void fun_80483fc() {
}

signed char g8049c10 = 0;

int32_t fun_8048435() {
    int1_t zf1;
    int32_t eax2;

    zf1 = g8049c10 == 0;
    if (zf1) {
        eax2 = fun_80483d0();
        g8049c10 = 1;
    }
    return eax2;
}

void fun_8048346() {
    goto 0x8048320;
}

void fun_8048336() {
    goto 0x8048320;
}

void fun_8048356() {
    goto 0x8048320;
}

void fun_8048376() {
    goto 0x8048320;
}

void fun_8048800(int32_t a1, int32_t a2, int32_t a3) {
    int32_t edi4;
    int32_t ebx5;
    int32_t ebx6;
    int32_t ebp7;
    int32_t esi8;
    int32_t esi9;

    edi4 = 0;
    fun_80483c0();
    ebx5 = ebx6 + 0x13d5;
    ebp7 = a1;
    fun_80482f4();
    esi8 = ebx5 - 0xf4 - (ebx5 - 0xf8) >> 2;
    if (esi8) {
        esi9 = esi8;
        do {
            *reinterpret_cast<int32_t*>(ebx5 + edi4 * 4 - 0xf8)(ebp7, a2, a3);
            ++edi4;
        } while (edi4 != esi9);
    }
    return;
}

void fun_8048386() {
    goto 0x8048320;
}

void fun_8048390() {
    void* esp1;
    int32_t edx2;
    int32_t eax3;

    esp1 = reinterpret_cast<void*>(reinterpret_cast<int32_t>(__zero_stack_offset()) + 4);
    fun_8048380(fun_804873e, __return_address(), esp1, fun_8048800, 0x8048870, edx2, (reinterpret_cast<uint32_t>(esp1) & 0xfffffff0) - 4 - 4, eax3);
    __asm__("hlt ");
}
