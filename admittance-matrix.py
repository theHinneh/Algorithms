"""Admittance matrix assignment
Emmanuel Opoku Hinneh - 5924016
Buboafor Quist Micheal - 5922416
Otu Mark Ampomah - 5927916
Agyarko Kwadwo Adu - 5917916
Obuadey Obed Borley - 5927016
"""

import numpy as np

num_of_buses = input('How many Buses? ')
num_of_lines = input('How many lines are available? ')

num_of_buses = int(num_of_buses)
num_of_lines = int(num_of_lines)

dt = np.dtype(np.complex)
Y = np.zeros((num_of_buses, num_of_buses), dtype=dt)

print('\n')

for i in range(num_of_lines):
    sending_bus = input('input the sending bus number ')
    ending_bus = input('what is the ending bus number? ')
    z = input('what is the impedance in complex numbers? ')

    sending_bus = int(sending_bus) - 1
    ending_bus = int(ending_bus) - 1
    z = complex(z)

    y = 1 / z

    if sending_bus != ending_bus:
        Y[sending_bus][ending_bus] = -y
        Y[ending_bus][sending_bus] = Y[sending_bus][ending_bus]

for a in range(num_of_buses):
    for b in range(num_of_buses):
        if a != b:
            Y[a, a] = np.add(Y[a, a], Y[a, b])
    Y[a, a] = -Y[a, a]

print('\n Admittance matrix = ')
print(Y)
