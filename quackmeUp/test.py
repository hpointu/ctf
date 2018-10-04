import sys


def ROR(x, n, bits=32):
    mask = (2**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))


def ROL(x, n, bits=32):
    return ROR(x, bits - n, bits)


def ror4(c):
    return ROR(c, 4, 8)


def ror8(c):
    return ROR(c, 8, 8)


def rol4(c):
    return ROL(c, 4, 8)


def rol8(c):
    return ROL(c, 8, 8)


def encrypt(s):
    for c in s:
        k = rol4(ord(c))
        l = rol8(k ^ 22)
        yield l


def decrypt(s):
    for c in s:
        c = ror8(c ^ 22)
        yield ror4(c)


# e = list(encrypt(sys.argv[1]))
# d = list(decrypt(e))
# print(' '.join(format(l, '02x') for l in e))
# print(''.join(format(c, 'x') for c in d).decode('hex'))

s = sys.argv[1]
d = list(decrypt(int(c, 16) for c in s.split()))
print(''.join(format(c, 'x') for c in d).decode('hex'))
