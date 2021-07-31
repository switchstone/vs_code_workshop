fib_sum = 0
FIB_MAX = 4000000
fpos_a, fpos_b, fpos_c = 1, 2, 0 # fpos = position in the fibonacci sequence

while (fpos_a + fpos_b < FIB_MAX):
    fpos_c = fpos_a + fpos_b
    fpos_a = fpos_b
    fpos_b = fpos_c
    if fpos_c % 2 == 0:
        fib_sum += fpos_c

print('The sum of all the even-valued numbers in a Fibonacci sequence: {}'.format(fib_sum)) # 4613732
