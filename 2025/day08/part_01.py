
#!/usr/bin/env python3

import math
from itertools import combinations
from operator import mul
from functools import reduce

def multiply(values):
    return reduce(mul, values, 1)


from core import get_options, load_input

def get_candidates(points):
    options = []
    for p0, p1 in combinations(points, 2):
        d = p0.distance(p1)
        t = (d, p0, p1)
        options.append(t)
    for t in sorted(options, key=lambda row: row[0]):
        yield t


def find_in_circuits(circuits, p):
    for i, circuit in enumerate(circuits):
        if p in circuit:
            return i, circuit
    return -1, None


def points_not_in_circuits(points, circuits):
    result = []
    for point in points:
        for circuit in circuits:
            if point in circuit:
                break
        else:
            result.append(point)
    return result


def main(options):
    '''Day 8, part 1'''
    verbose = options.verbose
    limit = options.limit
    acc = 0
    points = list(load_input(options.filename))
    circuits = []
    i = 0
    for d, p0, p1 in get_candidates(points):
        if verbose:
            print(f'step {i}')
            print(f'Candidates {p0} <--| {d} |--> {p1}')
        i0, circuit0 = find_in_circuits(circuits, p0)
        i1, circuit1 = find_in_circuits(circuits, p1)
        if circuit0 and circuit1:
            if circuit0 == circuit1:
                if verbose:
                    print('Both in some circuit, ignore this pair')
                continue
            else:
                new_circuit = circuit0 | circuit1
                del circuits[max([i0, i1])]
                del circuits[min([i0, i1])]
                circuits.append(new_circuit)
        elif circuit0 and not circuit1:
            circuit0.add(p1)
        elif not circuit0 and circuit1:
            circuit1.add(p0)
        else:
            new_circuit = set([p0, p1])
            circuits.append(new_circuit)
        size = sum([len(_c) for _c in circuits])
        i += 1
        if verbose:
            not_in_circuit = len(points_not_in_circuits(points, circuits))
            print(f'circuits: {len(circuits)}  not in circuit: {not_in_circuit}')
            for circuit in circuits:
                print(circuit, len(circuit))
            input()
        if i >= limit:
            break
    sorted_sizes = sorted([len(c) for c in circuits], reverse=True)
    print(sorted_sizes[0:3])
    print(sum(sorted_sizes))
    print(sorted_sizes, sep='+')
    acc = multiply(sorted_sizes[0:3])
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
