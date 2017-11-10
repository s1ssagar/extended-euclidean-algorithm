def mmi(a,power,m):
    m0 = m
    x0 = 0
    x1 = 1
    if m == 0:
        return 0
    while a > 1:
        # quotient
        q = a/m
        t = m
        # euclids theorem
        m= a%m
        a = t
        # back subs
        t = x0
        x0 = x1-(q*x0)
        x1 = t
    if x1 < 0:
        x1 += m0
    return x1
    
def main():
    base, power, mod = map(int, raw_input().strip().split(' '))
    print mmi(base, power, mod)

if __name__ == "__main__":
    main()