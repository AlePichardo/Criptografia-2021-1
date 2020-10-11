#Prueba Inicial

#! /bin/sh
python3 prueba.py

import fileinput

lines = []
isFloat = False
result = 0.0

for line in fileinput.input()
	if line.find(".") != -1:
		isFloat = True
	x = line.split("\n")
	lines.append(float(x[0]))

if not isFloat:
	result = int(result)

for i in n:
	result = result + i

print(result)