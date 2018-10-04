from __future__ import print_function
import string
from pwn import *


PAD = "X"*11  # to pad until next block
flag = 'FFFFFFFFFFFFFFFFFFFFFFFFF'

PLAIN = """Agent,
Greetings. My situation report is as follows:
{}
My agent identifying code is: {}.
Down with the Soviets,
006
"""


def oracle(prefix):
    p = remote('2018shell1.picoctf.com', 33893)

    print(p.readuntil("report:"))
    p.sendline(prefix)
    ciphertext = p.readall().strip()
    return bytearray.fromhex(ciphertext)


def dump_blocks(text, ascii=False, cols=3):
    for i in range(len(text)):
        if (i) % 16 == 0:
            print('|', end='')
        if ascii:
            print(text.replace('\n', '.')[i], end='')
        else:
            print("{:02x}".format(text[i]), end='')
        if (i+1) % (16 * cols) == 0:
            print('|')
    print()


# messages = reversed([
#     oracle('X'*i)
#     for i in range(16)
# ])

# for m, c in messages:
#     print("%s: " % m)
#     dump(c)
#

# 1: find prefix so first byte of flag is last of a block
# 2: get cipher for that
# 3: extend prefix to have same blocks as in 1 but last byte bruteforced
PREFIX_OFFSET = 53
FLAG_OFFSET = 31  # from end of prefix

symbols = '{}[]+-'
alphabet = string.digits + string.punctuation + string.ascii_lowercase \
    + string.ascii_uppercase + symbols


def get_7th_block(ciphertext):
    return ciphertext[7*16:8*16]


guess = 'picoCTF{@g3nt6_1$_th3_c00l3$'
for i in range(25):
    m1 = 'X' * (43 - len(guess))
    c1 = oracle(m1)
    for c in alphabet:
        tmp_guess = guess + c
        print(tmp_guess)
        m2 = m1 + '.My agent identifying code is: ' + tmp_guess
        c2 = oracle(m2)
        if get_7th_block(c1) == get_7th_block(c2):
            guess = tmp_guess
            break

#
guess = ''
m1 = 'X'* (43 - len(guess))
# guess = 'p'
# guess2 = 'i'
m2 = m1 + '.My agent identifying code is: ' + guess
c1 = oracle(m1)
c2 = oracle(m2)
dump_blocks(PLAIN.format(m1, flag), True)
dump_blocks(PLAIN.format(m2, flag), True)
dump_blocks(c1, False)
dump_blocks(c2, False)
