def depth(t):
    d, md = 0, 0
    for c in t:
        d += 1 if c == '(' else -1
        if d > md:
            md = d
    return md


def add(t1, t2):
    s1, s2 = depth(t1), depth(t2)
    if s1 == s2:
        return t1 + t2
    if s1 > s2:
        return t1[:-1] + t2 + ')'
    else:
        return '(' + t1 + t2[1:]


if __name__ == "__main__":
    from pwn import *
    p = remote('2018shell1.picoctf.com', 22973)
    while 1:
        line = p.readline()
        print(line.strip())
        if '???' in line:
            eq = line.split(' = ')[0]
            info("eq: %s" % eq)
            tokens = eq.split(' + ')
            # re = add(*tokens)
            re = reduce(add, tokens)
            info("re: %s" % re)
            p.sendline(re)

# (()()()()()) + (()(())) = ((()()()()())()(())) GOOD
# (()()()()()) + (()(())) = (()()()()())(()(())) BAD

 # (()()()()()()()()) + (()) + (()(((()()())()())()())) + (()(())) + (()())
 # ((()()()()()()()())(())()(((()()())()())()())(()(()))(()()))
 #
 # (()()()()()()()())(())(()(((()()())()())()()))(()(()))(()())
