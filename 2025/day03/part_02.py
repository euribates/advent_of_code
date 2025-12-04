#!/usr/bin/env python3


from core import get_options, load_input

SIZE = 12

def get_max_jolts(line: str, verbose=False) -> int:
    digits = list(line)
    freedom = len(digits) - SIZE
    stack = []
    while freedom > 0:
        a = digits[0]
        b = digits[1]
        c = digits[2]
        ab = f'{a}{b}'
        ac = f'{a}{c}'
        bc = f'{b}{b}'
        if verbose:
            print(f'freedom: {freedom} Stack: {stack} digits: {digits}')
        if bc >= ac and bc >= ab:  # Drop a
            print(f'- Remove a: {a} {digits[0]}')
            digits.pop(0)
            freedom -= 1
        elif ac >= ab and ac >= bc: # Drop B, prom A
            print(f'- Remove b: {b} {digits[1]}')
            stack.append(digits.pop(0))
            del digits[0]
            freedom -= 1
        elif ab >= ac and ab >= bc:  # Drop C, prom A
            print(f'- Remove c: {c} {digits[2]}')
            stack.append(digits.pop(0))
            del digits[1]
            freedom -= 1
        else:
            raise ValueError(f'Queseto ab:{ab} bc:{bc} ac:{ac}' )
    buff = stack + digits[0:SIZE-len(stack)]
    result = ''.join(buff)
    if verbose:
        print(line, result)
        input()
    return result



def main(options):
    '''Day 3, part 2'''
    verbose = options.verbose
    acc = 0
    for line in load_input(options.filename):
        acc += int(get_max_jolts(line, verbose=verbose))
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
