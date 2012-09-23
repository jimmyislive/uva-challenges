
"""
problem description @ http://acm.uva.es/p/v1/100.html
"""

def cycle_length(n, count):
    if (n == 1):
        return count
    if (n % 2):
        n = 3*n + 1
    else:
        n = n/2

    return cycle_length(n, count + 1)

def main(start,end):
    cycles = []
    for i in range(start, end + 1):
        cycles.append(cycle_length(i, 1))

    return max(cycles)

if __name__ == '__main__':
    assert main(22,23) == 16
    assert main(1,10) == 20
    assert main(100,200) == 125
    assert main(201,210) == 89
    assert main(900,1000) == 174

