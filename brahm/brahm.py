from __future__ import print_function
from pwn import *
import string
import time


def get_p():
    return remote('2018shell1.picoctf.com', 37440)

def dump_blocks(text, ascii=True, cols=3):
    print()
    for i in range(len(text)):
        if (i) % 16 == 0:
            print('|', end='')
        if ascii:
            c = text[i]
            if 0x20 < ord(c) < 0x7e:
                pass
            else:
                c = '.'

            print(c, end='')
        else:
            print("{:02x}".format(text[i]), end='')
        if (i+1) % (16 * cols) == 0:
            print('|')
    print()


def encrypt(report, additional=''):
    encrypted = ''
    found = False
    while not found:
        try:
            p = get_p()
            p.readuntil('S)\n')
            p.sendline('E')
            p.readuntil(': ')
            p.sendline(report)
            p.readuntil('? ')
            p.sendline(additional)
            p.readuntil(': ')
            encrypted = p.readline().strip()
            found = True
        except KeyboardInterrupt:
            p.close()
            return
        except:
            pass
        finally:
            p.close()
    return encrypted


def submit(message):
    result = ''
    found = False
    while not found:
        try:
            p = get_p()
            p.readuntil('S)\n')
            p.sendline('S')
            p.readuntil(': ')
            p.sendline(message)
            result = p.readline()
            if result.startswith('Traceback'):
                while True:
                    line = p.readline()
                    result += line
                    if not line.startswith(' '):
                        break
            result = result.strip()
            found = True
        except KeyboardInterrupt:
            p.close()
            return
        except:
            pass
        print(result)
        p.close()
    return result


def get_full_padding_message_encrypted(empty_message_encrypted):
    base_length = len(empty_message_encrypted)
    with log.progress('Finding length for full padding...') as progress:
        for i in range(1, 17):  # TODO replace 14 with 1
            progress.status(str(i))
            encrypt_message = encrypt('a' * i)
            current_length = len(encrypt_message)
            if current_length != base_length:
                progress.success(str(i))
                return encrypt_message
        progress.success('0')
        return empty_message_encrypted


def bytes_from_hex(hex_string):
    return ''.join(chr(b) for b in bytearray.fromhex(hex_string))


def get_nth_block(ciphertext, n):
    return ciphertext[n*16:(n+1)*16]


PLAIN = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
{2}""" + 10*"M="


PLAIN_NOFLAG = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: .
Down with the Soviets,
006
{1}""" + 10*"M="

guess = "picoCTF{g0_@g3nt006!_4936528}"
guess = [ord(c) for c in guess]
for i in range(len(guess), 45):
    flag = 'picoCTF{%s}' % ((29-9)*'x')
    tot = 11 + 16*3
    a = 'X'*(tot - i)
    b = 'Y'*(3 + tot - len(a))
    fake_msg = PLAIN.format(a, flag, b)
    while True:
        dump_blocks(8*'IV' + fake_msg, True)
        print(guess)
        print(''.join(chr(k) for k in guess))
        e = bytes_from_hex(encrypt(a, b))
        bi = get_nth_block(e, 9)
        bp = get_nth_block(e, 8)
        bl = get_nth_block(e, 14)
        # dump_blocks(e, True)
        # dump_blocks(bi, True)
        # dump_blocks(bp, True)
        # dump_blocks(bl, True)

        tampered = e[:-16] + bi
        # dump_blocks(tampered)

        res = submit(tampered.encode('hex'))
        if 'Ooops!' not in res:
            # print("found")
            c = 16 ^ ord(bp[-1]) ^ ord(bl[-1])
            guess.append(c)
            print(guess)
            print(''.join(chr(k) for k in guess))
            break


# first step: find out the length of the flag
#for i in range(17):
#    a = 'X'*i
#    b = 'BBBBBBBBBB'
#    e = encrypt(a, b)
#    print(i)
#    dump_blocks()
