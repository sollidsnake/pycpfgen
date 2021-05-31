#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
from random import randint

import random

def gerar_cpf(formatacao=False):
    def calcula_digito(digs):
       s = 0
       qtd = len(digs)
       for i in range(qtd):
          s += n[i] * (1+qtd-i)
       res = 11 - s % 11
       if res >= 10: return 0
       return res
    n = [random.randrange(10) for i in range(9)]
    n.append(calcula_digito(n))
    n.append(calcula_digito(n))

    if formatacao:
        return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)
    else:
        return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)


if __name__ == '__main__':
    print(gerar_cpf(True))
