from itertools import permutations

# size 0x24, 36
ORD = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ord_(c):
    return ORD.find(c)  # simplified version of real ord substraction


def mod(a, b):
    return a % b


def constraint_01(a):
    v1 = ord(a[0])
    v2 = ord(a[1])
    return mod(v1+v2, 0x24) == 14


def constraint_02(a):
    v1 = ord(a[2])
    v2 = ord(a[3])
    return mod(v1+v2, 0x24) == 24


def constraint_03(a):
    v1 = ord(a[2])
    v2 = ord(a[0])
    return mod(v1-v2, 0x24) == 6


def constraint_04(a):
    v1 = ord(a[1])
    v2 = ord(a[3])
    v3 = ord(a[5])
    return mod(v1+v2+v3, 0x24) == 4


def constraint_05(a):
    v1 = ord(a[2])
    v2 = ord(a[4])
    v3 = ord(a[6])
    return mod(v1+v2+v3, 0x24) == 13


def constraint_06(a):
    v1 = ord(a[3])
    v2 = ord(a[4])
    v3 = ord(a[5])
    return mod(v1+v2+v3, 0x24) == 22


def constraint_07(a):
    v1 = ord(a[6])
    v2 = ord(a[8])
    v3 = ord(a[10])
    return mod(v1+v2+v3, 0x24) == 31


def constraint_08(a):
    v1 = ord(a[1])
    v2 = ord(a[4])
    v3 = ord(a[7])
    return mod(v1+v2+v3, 0x24) == 7


def constraint_09(a):
    v1 = ord(a[9])
    v2 = ord(a[12])
    v3 = ord(a[15])
    return mod(v1+v2+v3, 0x24) == 20


def constraint_10(a):
    v1 = ord(a[13])
    v2 = ord(a[14])
    v3 = ord(a[15])
    return mod(v1+v2+v3, 0x24) == 12


def constraint_11(a):
    v1 = ord(a[8])
    v2 = ord(a[9])
    v3 = ord(a[10])
    return mod(v1+v2+v3, 0x24) == 27


def constraint_12(a):
    v1 = ord(a[7])
    v2 = ord(a[12])
    v3 = ord(a[13])
    return mod(v1+v2+v3, 0x24) == 23


"""
0:  [01, 03,],
1:  [01, 04, 08],
2:  [02, 03, 05],
3:  [02, 04, 06],
4:  [05, 06, 08],
5:  [04, 06],
6:  [05, 07],
7:  [08, 12],
8:  [07, 11],
9:  [09, 11],
10: [07, 11],
11: [],
12: [09, 12],
13: [10, 12],
14: [10],
15: [09, 10],

01: (a + b) % 36 = 14
02: (c + d) % 36 = 24
03: (a + c) % 36 = 6
04: (b + d + f) % 36 = 4
05: (c + e + g) % 36 = 13
06: (d + e + f) % 36 = 22
07: (g + i + k) % 36 = 31
08: (b + e + h) % 36 = 7
09: (j + m + p) % 36 = 20
10: (n + o + p) % 36 = 12
11: (i + j + k) % 36 = 27
12: (h + m + n) % 36 = 23
"""

from z3 import Int, Solver
s = Solver()
a = Int('a')
b = Int('b')
c = Int('c')
d = Int('d')
e = Int('e')
f = Int('f')
g = Int('g')
h = Int('h')
i = Int('i')
j = Int('j')
k = Int('k')
m = Int('m')
n = Int('n')
o = Int('o')
p = Int('p')

# s.add(36 > a)
# s.add(36 > b)
# s.add(36 > c)
# s.add(36 > d)
# s.add(36 > e)
# s.add(36 > f)
# s.add(36 > g)
# s.add(36 > h)
# s.add(36 > i)
# s.add(36 > j)
# s.add(36 > k)
# s.add(36 > m)
# s.add(36 > n)
# s.add(36 > o)
# s.add(36 > p)

s.add(a >= 0)
s.add(b >= 0)
s.add(c >= 0)
s.add(d >= 0)
s.add(e >= 0)
s.add(f >= 0)
s.add(g >= 0)
s.add(h >= 0)
s.add(i >= 0)
s.add(j >= 0)
s.add(k >= 0)
s.add(m >= 0)
s.add(n >= 0)
s.add(o >= 0)
s.add(p >= 0)


def cons(sum_, mod_):
    s.add(sum_ % 36 == mod_)

cons(a + b, 14)
cons(c + d, 24)
cons(c - a, 6)
cons(b + d + f, 4)
cons(c + e + g, 13)
cons(d + e + f, 22)
cons(g + i + k, 31)
cons(b + e + h, 7)
cons(j + m + p, 20)
cons(n + o + p, 12)
cons(i + j + k, 27)
cons(h + m + n, 23)

if s.check():
    mo = s.model()
    print(mo)
    tpl = '{}'*16
    print(tpl.format(
        ORD[mo[a].as_long() % 36],
        ORD[mo[b].as_long() % 36],
        ORD[mo[c].as_long() % 36],
        ORD[mo[d].as_long() % 36],
        ORD[mo[e].as_long() % 36],
        ORD[mo[f].as_long() % 36],
        ORD[mo[g].as_long() % 36],
        ORD[mo[h].as_long() % 36],
        ORD[mo[i].as_long() % 36],
        ORD[mo[j].as_long() % 36],
        ORD[mo[k].as_long() % 36],
        'X',
        ORD[mo[m].as_long() % 36],
        ORD[mo[n].as_long() % 36],
        ORD[mo[o].as_long() % 36],
        ORD[mo[p].as_long() % 36],
    ))
