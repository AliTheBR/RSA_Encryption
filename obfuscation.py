import random as R

def x0():
    def x1(y, z=5):
        if y <= 1: return False
        if y <= 3: return True
        if y % 2 == 0: return False
        a, b = 0, y - 1
        while b % 2 == 0:
            a += 1
            b //= 2
        for _ in range(z):
            c = R.randint(2, y - 2)
            d = pow(c, b, y)
            if d == 1 or d == y - 1: continue
            for _ in range(a - 1):
                d = pow(d, 2, y)
                if d == y - 1: break
            else: return False
        return True
    def x2(f=512):
        while True:
            g = R.getrandbits(f)
            if x1(g): return g
    def x3(h, i):
        def x4(j, k):
            if j == 0: return k, 0, 1
            l, m, n = x4(k % j, j)
            return l, n - (k // j) * m, m
        l, o, _ = x4(h, i)
        if l != 1: raise ValueError("Error")
        return o % i
    def x5(p=512):
        q, r = x2(p), x2(p)
        s, t = q * r, (q - 1) * (r - 1)
        u = 65537
        v = x3(u, t)
        return (s, u, v)
    def x6(w, x, y):
        z = int.from_bytes(w.encode(), 'big')
        return pow(z, y, x)
    print("X...")
    A, B, C = x5(512)
    D = input("M: ")
    E = x6(D, A, B)
    print("\nPK:", (A, B))
    print("SK:", (A, C))
    print("\nE:", E)
def x7():
    def x8(F, G, H):
        I = pow(F, H, G)
        return I.to_bytes((I.bit_length() + 7) // 8, 'big').decode()
    J = input("SK: ").split(',')
    K, L = int(J[0]), int(J[1])
    M = int(input("C: "))
    N = x8(M, K, L)
    print("\nD:", N)
O = input("E(e) or D(d): ")
if O in ["e", "encrypt"]:
    x0()
    print("Complete")
elif O in ["d", "decrypt"]:
    x7()
    print("Complete")
else:
    print("Error")