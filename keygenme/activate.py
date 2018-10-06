import random

ORD = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ord_(c):
    return ORD.find(c)  # simplified version of real ord substraction


def _valid_sum(cref, s):
    v1 = s
    t = v1
    t *= 0x38e38e39
    # print("0x080487e0\tedx/eax: %x"%t)
    t >>= 32
    t >>= 3
    # print("0x080487e5\tebx: %x"%t)
    v2 = t << 3
    # print("0x080487ea\teax: %x"%v2)
    t += v2
    t <<= 2
    t &= 0xFFFFFFFF
    # print("0x080487ef\teax: %x"%t)
    v1 -= t

    return v1 == cref

def validate_key(s):
    # EBX pushed in prologue?
    size = len(s)
    v1 = 0
    index = 0

    # 0x80487c9
    while index < size-1:
        # 0x8048799
        c = s[index] # with sign extension? from byte
        o = ord_(c)   # again with sign extension? from byte
        v1 += (index + 1) * (o + 1)
        index += 1

    sum_ = v1

    # 0x80487d4
    t = v1
    t *= 0x38e38e39
    # print("0x080487e0\tedx/eax: %x"%t)
    t >>= 32
    t >>= 3
    # print("0x080487e5\tebx: %x"%t)
    v2 = t << 3
    # print("0x080487ea\teax: %x"%v2)
    t += v2
    t <<= 2
    t &= 0xFFFFFFFF
    # print("0x080487ef\teax: %x"%t)
    v1 -= t
    # print("0x080487f1\tecx: %x"%v1)

    return sum_, v1 == ord_(s[-1])


def generate_key():
    # pick a random last char
    lc = random.choice(ORD)
    # get valid sums
    valid_sums = [
        s for s in range(120, 16*16*36)
        if _valid_sum(ord_(lc), s)
    ]

    s = valid_sums[0]
    count = 0
    res = [lc]
    for i in range(15, 0, -1):
        # get multiples of i
        max_ = s - sum(range(i)) - count
        multiples = [m*i for m in range(1, 37) if m*i <= max_]
        # take the biggest
        m = max(multiples)
        count += m
        res = [ORD[(m//i)-1]] + res

    key = ''.join(res)
    return key

key = generate_key()
print(key)
