from __future__ import print_function
from pwn import *


PAD = "X"*11  # to pad until next block


def oracle(prefix):
    p = remote('2018shell1.picoctf.com', 33893)

    print(p.readuntil("report:"))
    p.sendline(PAD+prefix)
    ciphertext = p.readall().strip()
    return prefix, bytearray.fromhex(ciphertext)


def dump(ciphertext):
    for i in range(len(ciphertext)):
        print("{:02x}".format(ciphertext[i]), end='')
        if (i+1) % 16 == 0:
            print(' ', end='' if (i+1) % 32 != 0 else '\n')
    print()


messages = reversed([
    oracle('X'*i)
    for i in range(16)
])

# for m, c in messages:
#     print("%s: " % m)
#     dump(c)
#

# 1: find prefix so first byte of flag is last of a block
# 2: get cipher for that
# 3: extend prefix to have same blocks as in 1 but last byte bruteforced

message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
"""
PREFIX_OFFSET = 53
FLAG_OFFSET = 31  # from end of prefix
