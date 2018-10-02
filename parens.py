from pwn import *


p = remote('2018shell1.picoctf.com', 22973)


def add(t1, t2):
    return t1[:-1] + t2 + ')'


while 1:
    line = p.readline()
    print(line.strip())
    if '???' in line:
        eq = line.split(' = ')[0]
        info("eq: %s" % eq)
        tokens = eq.split(' + ')
        re = add(*tokens)
        info("re: %s" % re)
        p.sendline(re)

