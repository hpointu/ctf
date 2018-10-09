magic = [0xbd, 0x0e, 0x50, 0x1b, 0xef, 0x9e, 0x16, 0xd1, 0x7d, 0xe5, 0xc1, 0x55, 0xc9, 0x7f, 0xcf, 0x21, 0xc5, 0x99, 0x51, 0xd5, 0x7d, 0xc9, 0xc5, 0x9d, 0x21, 0xd3, 0x7d, 0xc1, 0xcd, 0xd9, 0x95, 0x8f, 0x91, 0x99, 0x97, 0xc5, 0xf5, 0xd1, 0x2d, 0xd5]


def ror(x, n, bits=32):
    mask = (2**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))


def rol(x, n, bits=32):
    return ror(x, bits - n, bits)


def dword(c):
    return [c >> (i*8) & 0xff
            for i in range(4)]


def word(c):
    return [c >> (i*8) & 0xff
            for i in range(2)]


def tata():
    guess = []
    s = magic
    for i in range(len(s) - 4, -1, -1):
        k = int(''.join(format(n,'02x') for n in reversed(s[i:i+4])), 16)
        k = ror(k, 0xa, 32)
        magic[i:i+4] = dword(k)

        k = rol(k & 0xffff, 0xf, 16)
        magic[i:i+2] = word(k)

        k = (k & 0xff) ^ 0x66
        magic[i] = k

    return magic

if __name__ == "__main__":
    r = tata()
    print(map(hex,r))
    print(''.join(chr(i) for i in r))
