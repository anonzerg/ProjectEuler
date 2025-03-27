#! /usr/bin/env python3

# anonzerg@proton.me
# https://projecteuler.net/problem=2
# solution 4613732

def main():
    a, b = 1, 2
    sum = 0
    while (b < 4_000_000):
        if (b % 2 == 0):
            sum += b
        a, b = b, a+b

    print(sum)
    return

if __name__ == "__main__":
    main()

