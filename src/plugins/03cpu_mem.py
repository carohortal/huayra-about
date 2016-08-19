#! /usr/bin/python
# -*- coding: utf-8 -*-
# Copyleft 2015 - Diego Accorinti (mejoras memoria y modelo de cpu)
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)
import markup
import info_table
from subprocess import Popen, PIPE


# Memoria
memo = (Popen(['free', '-m'], stdout=PIPE).stdout.read()).split()
mem_label = markup.label_set_markup('Memoria')
mem_texto = markup.text_set_markup(memo[7] + " Mb")

# CPU
s = ""
micro = Popen(['lscpu'], stdout=PIPE).stdout.read()
micro = (s.join(micro)).split()
micro_label = markup.label_set_markup('Microprocesador')

x = 0
while micro[x] != "name:":
    x += 1
micro_texto = ""
while micro[x + 1] != "Stepping:":
    micro_texto = micro_texto + micro[x + 1] + " "
    x += 1
micro_texto = markup.text_set_markup(micro_texto)

info_table.add_row_to_table(mem_label, mem_texto, 3, "Memoria disponible")
info_table.add_row_to_table(micro_label, micro_texto, 4, "Modelo de microprocesador")
