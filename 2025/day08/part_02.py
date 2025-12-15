#!/usr/bin/env python3

import math
from itertools import combinations
from operator import mul
from functools import reduce

from colors import green


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
    '''Day 8, part 2'''
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
                    print(green('Both in some circuit, ignore this pair'))
                i += 1
            else:
                new_circuit = circuit0 | circuit1
                print(f'Borramos el circuito {green(max([i0, i1]))}')
                del circuits[max([i0, i1])]
                print(f'Borramos el circuito {green(min([i0, i1]))}')
                del circuits[min([i0, i1])]
                circuits.append(new_circuit)
                i += 1
        elif circuit0 and not circuit1:
            print(f'El punto {p0} estaba ya en el circuito {i0}, le añadimos {p1}')
            circuit0.add(p1)
            i += 1
        elif not circuit0 and circuit1:
            print(f'El punto {p1} estaba ya en el circuito {i1}, le añadimos {p0}')
            circuit1.add(p0)
            i += 1
        else:
            print('Nuevo circuito')
            new_circuit = set([p0, p1])
            circuits.append(new_circuit)
            i += 1
        if verbose:
            not_in_circuit = len(points_not_in_circuits(points, circuits))
            print(f'circuits: {len(circuits)}  not in circuit: {not_in_circuit}')
            for index, circuit in enumerate(circuits):
                print(index, circuit, len(circuit))
            input()
        not_in_circuit = len(points_not_in_circuits(points, circuits))
        if len(circuits) == 1 and not_in_circuit == 0:
            break
    print(green('Encontrado'))
    print(i)
    print(p0, p1)
    acc = p0.x * p1.x
    print(f'{p0.x} * {p1.x} = {acc}')
    print(f'Solution for {main.__doc__}: {acc}')



if __name__ == '__main__':
    main(get_options())
