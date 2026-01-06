#!/usr/bin/env python

from copy import deepcopy

class Machine:

    def __init__(self, line, mode=1):
        close_brackets = line.index(']')
        self.target = [
            char == '#'
            for char in line[1:close_brackets]
            ]
        self.num_leds = len(self.target)
        self.leds = [False] * self.num_leds
        open_braces = line.index('{')
        self.joltages = [
            int(_)
            for _ in line[open_braces + 1: -1].split(',')
            ]
        self.counters = [0] * len(self.joltages)
        self.buttons = []
        for action in line[close_brackets + 2: open_braces - 1].split(' '):
            assert action[0] == '('
            assert action[-1] == ')'
            signals = [int(_) for _ in action[1:-1].split(',')]
            self.buttons.append(signals)
        self.mode = mode

    def reset(self):
        self.leds = [False] * self.num_leds
        self.counters = [0] * len(self.joltages)



    @property
    def label(self):
        return ''.join([
            '#' if _ else '.'
            for _ in self.leds
            ])

    def copy(self):
        return deepcopy(self)

    def press_button(self, index: int):
        result = self.copy()
        signals = result.buttons[index]
        if self.mode == 1:
            for _ in signals:
                result.leds[_] = not result.leds[_]
        elif self.mode == 2:
            for _ in signals:
                result.counters[_] += 1
        return result

    def is_ready(self) -> bool:
        return self.leds == self.target

    def is_working(self):
        return self.counters == self.joltages

    def is_overly(self):
        return any([
            _c > _j
            for _j, _c in zip(self.joltages, self.counters)
            ])

    def __str__(self):
        s_target = ''.join([
            '#' if _ else '.'
            for _ in self.target
            ])
        l_buttons = []
        for signals in self.buttons:
            buff = ['(']
            buff.append(','.join([str(_) for _ in signals]))
            buff.append(')')
            l_buttons.append(''.join(buff))
        s_buttons = ' '.join(l_buttons)
        s_joltages = ','.join([
            str(j) for j in self.joltages
            ])
        return f'[{s_target}] {s_buttons} {{{s_joltages}}}'

    def __repr__(self):
        return f'Machine({self})'

    def apply_command(self, cmd):
        for index, value in enumerate(cmd):
            self.counters[index] += value
            
    def is_over_joltage(self, cmd) -> bool:
        return any([
            cmd[_] > self.joltages[_]
            for _ in range(self.num_leds)
            ])

    def get_commands(self):
        for button in self.buttons:
            cmd = tuple([
                1 if index in button else 0
                for index in range(self.num_leds)
                ])
            while not self.is_over_joltage(cmd):
                yield button, cmd
                cmd = tuple([
                    _ + 1 if _ > 0 else 0
                    for _ in cmd
                    ])

