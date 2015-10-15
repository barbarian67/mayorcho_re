#!/usr/bin/env python
#-*- coding: utf-8 -*-
mayor = 0
num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
while num>=0:
	if num > mayor:
		mayor = num
	num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
print "El mayor del chorro números es " + str(mayor)
		


