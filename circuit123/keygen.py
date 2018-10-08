import sys
import z3


def solve(chalbox):
    solver = z3.Solver()
    length, gates, check = chalbox

    size = length + len(gates) + 1
    v = z3.BitVec('v', size)

    def nth(n):
        return (v >> (size - n - 1)) & 1

    i = 0
    for name, args in gates:
        if name == 'true':
            solver.add(nth(length+i) == 1)
        else:
            a = nth(args[0][0]) ^ args[0][1]
            b = nth(args[1][0]) ^ args[1][1]
            if name == 'or':
                solver.add(nth(length+i) == (a | b))
            elif name == 'xor':
                solver.add(nth(length+i) == (a ^ b))
        i += 1

    solver.add(nth(check[0]) ^ check[1] == 1)

    if solver.check() == z3.sat:
        i = solver.model()[v]
        print(int(''.join(reversed(format(i.as_long(), 'b')[:length])), 2))
    return



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        cipher, chalbox = eval(f.read())
    solve(chalbox)
