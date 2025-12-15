#!/usr/bin/env python3

LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
END = "\033[0m"


def green(text: str) -> str:
    '''Devuelve el texto en verde.
    '''
    return f'{LIGHT_GREEN}{text}{END}'


def red(text: str) -> str:
    '''Devuelve el texto en rojo.
    '''
    return f'{LIGHT_RED}{text}{END}'


def yellow(text: str) -> str:
    '''Devuelve el texto en amarillo.
    '''
    return f'{YELLOW}{text}{END}'
