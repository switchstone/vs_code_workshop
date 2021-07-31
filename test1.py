fib_sum = 0
FIB_MAX = 4000000
fpos_a, fpos_b, fpos_c = 1, 2, 0 # fpos = position in the fibonacci sequence

while (fpos_a < FIB_MAX) and (fpos_b < FIB_MAX) and (fpos_c < FIB_MAX):
    fpos_c = fpos_a + fpos_b
    if fpos_a % 2 == 0:
        fib_sum += fpos_a
    fpos_a = fpos_b + fpos_c
    if fpos_b % 2 == 0:
        fib_sum += fpos_b
    fpos_b = fpos_c + fpos_a
    if fpos_c % 2 == 0:
        fib_sum += fpos_c

print('The sum of all the even-valued numbers in a Fibonacci sequence: {}'.format(fib_sum)) # 4613732
