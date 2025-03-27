#! /usr/bin/env python3

# anonzerg@proton.me
# https://projecteuler.net/problem=1
# solution 233168

def main():
    lst = []
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            lst.append(i)

    print(sum(lst))
    return

if __name__ == "__main__":
    main()

