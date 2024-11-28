import os
import time
'''F00: Program Random Number Generator
{ Spesifikasi : Mengeluarkan angka "random" menggunakan sistem Random Number Generator dengan algoritma Linear Congruential Generator.
Import os dan time disini berguna sebagai variabel "seed" yang akan membantu program mengeluarkan bilangan acak yang lebih "natural".
Keterangan, Formula LCG : X = (a * x0 + c) % m }'''

def formula(a:int, c:int, m:int, seed:int)->int:        # Fungsi yang berisikan formula dari pencarian bilangan random sebagai variabel x_prev
    x0 = seed

    if seed is None:
        x0 = int(os.getpid() + time.time())
    else:
        x0 = seed

    x_prev = (a * x0 + c) % m

    return x_prev

def randomNumberGenerator(x_prev:int, numRange=None)->int:   # Fungsi rekursif dari x_prev yang akan menghasilkan bilangan secara random
    a = 4871
    c = 0
    m = 2**31-1

    x_prev = (a * x_prev + c) % m

    if numRange is None:
        return x_prev
    else:
        return int((x_prev / m) * (numRange[1] - numRange[0]) + numRange[0])

# Contoh penggunaan:
#print(randomNumberGenerator(formula(a = 4871, c = 0, m = 2**31-1, seed=None), [1,11]))