# Kinanthi P (71210745)
# UG02 - deret ajaib

import timeit

# recursive

def ajaib_re(n):
    if (n <= 5):
        return n
    else:
        return ajaib_re(n-2) + ajaib_re(n//2)

for i in range(1, 101):
    start = timeit.default_timer()
    suku = ajaib_re(n)
    end = timeit.default_timer()
    waktu = end-start
    print("suku ke",n,"adalah",suku,"waktu",waktu,"detik")
