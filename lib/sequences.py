#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fib_seq = []
    a, b = 0, 1
    for _ in range(length):
        fib_seq.append(a)
        a, b = b, a + b

    print(fib_seq)
    pass