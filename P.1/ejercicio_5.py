#!/usr/bin/env python3
import random

# Piedra, Papel o Tijera - versión simple y legible
OPTS = ['PIEDRA', 'PAPEL', 'TIJERA']

v = d = e = 0

print('Piedra, Papel o Tijera — escribe EXIT para salir')

try:
    while True:
        jug = input('Tu jugada: ').strip().upper()
        if jug == 'EXIT':
            break
        if jug not in OPTS:
            print('Entrada no válida. Usa PIEDRA, PAPEL o TIJERA.')
            continue

        pc = random.choice(OPTS)

        if jug == pc:
            e += 1
            resultado = 'EMPATE'
        elif (jug == 'PIEDRA' and pc == 'TIJERA') or \
             (jug == 'TIJERA' and pc == 'PAPEL') or \
             (jug == 'PAPEL' and pc == 'PIEDRA'):
            v += 1
            resultado = 'GANASTE'
        else:
            d += 1
            resultado = 'PERDISTE'

        print(f'Tú: {jug}  PC: {pc}  -> {resultado}')
        print(f'Marcador: V={v}  D={d}  E={e}\n')

except (KeyboardInterrupt, EOFError):
    print('\nInterrumpido por el usuario.')

print('\nMarcador final:')
print(f'Victorias: {v}  Derrotas: {d}  Empates: {e}')
