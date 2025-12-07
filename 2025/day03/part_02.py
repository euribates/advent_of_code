#!/usr/bin/env python3


from tqdm import tqdm

from core import get_options, load_input

SIZE = 12


def find_seq(items, verbose=False):
    result = []
    size = SIZE
    while len(result) < SIZE:
        max_char = max(items)
        index = items.index(max_char)
        if index > len(items) - size: # No sirve
            for num in range(ord(max_char)-1, ord('0'), -1):
                char = chr(num)
                try:
                    index = items.index(char)
                except ValueError:
                    continue
                if index <= len(items) - size:
                    max_char = char
                    break
            else:
                print('No encuentra ndad?')
                break
        if verbose:
            print(f'Encontrado {max_char} en items[{index}]')
            from icecream import ic; ic(items)
        result.append(max_char)
        items = items[index+1:]
        size = size - 1
        if len(items) < size:
            break
        
    delta = SIZE - len(result)
    result.extend(items[0:delta])
    return result


def get_max_jolts(line, size=SIZE, verbose=False):
    items = tuple(list(line))
    values = find_seq(items, verbose=verbose)
    result = ''.join(values)
    if verbose:
        print(result)
    return result


def main(options):
    '''Day 3, part 2'''
    verbose = options.verbose
    acc = 0
    lines = list(load_input(options.filename))
    for line in tqdm(lines):
        result = int(get_max_jolts(line, size=SIZE, verbose=verbose))
        acc += result
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
