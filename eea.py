import sys

#author tolgabuyuktanir
#Python program for Extended Euclidean algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b/a) * x, x)

def main():
    if(len(sys.argv)!=3):
        print("Usage: python3 eea.py a m")
        print("\tax+by=1\n\tgdc(a,m)=1")
    else:
        a=int(sys.argv[1])
        m=int(sys.argv[2])
        gcd, x, y = egcd(a,m)
        print("gdc:"+str(gcd)+" x:"+str(x)+" y:"+str(y))

if __name__ == "__main__":
    main()
