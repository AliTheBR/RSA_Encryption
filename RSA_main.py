import random
def encryption():
    def is_prime(n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    def generate_large_prime(bits=512):
        while True:
            num = random.getrandbits(bits)
            if is_prime(num):
                return num
    def mod_inverse(e, phi):
        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            g, x, y = egcd(b % a, a)
            return g, y - (b // a) * x, x

        g, x, _ = egcd(e, phi)
        if g != 1:
            raise ValueError("No modular inverse found!")
        return x % phi
    def generate_rsa_keys(bits=512):
        p = generate_large_prime(bits)
        q = generate_large_prime(bits)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537
        d = mod_inverse(e, phi)
        return (n, e, d)
    def encrypt(message, n, e):
        m = int.from_bytes(message.encode(), 'big')
        c = pow(m, e, n)
        return c
    print("Generating RSA keys...")
    n, e, d = generate_rsa_keys(bits=512)
    plaintext = input("Enter message to encrypt: ")
    ciphertext = encrypt(plaintext, n, e)
    print("\n Public Key (n, e):", (n, e))
    print(" Private Key (n, d):", (n, d))
    print("\n Encrypted:", ciphertext)
def decryption():
    def decrypt(ciphertext, n, d):
        m = pow(ciphertext, d, n)
        message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
        return message
    private_key = (input("Enter Private Key (n,d): ")).split(',')
    n,d = int(private_key[0]), int(private_key[1])
    ciphertext = int(input("Enter ciphertext: "))
    decrypted_text = decrypt(ciphertext, n, d)
    print("\n Decrypted Message:", decrypted_text)
what = input("enter Encrypt (e) or Decrypt (d): ")
if what == "encrypt" or what == "e":
    encryption()
    print("Encryption Complete")
elif what == "decrypt" or what == "d":
    decryption()
    print("Decryption Complete")

else :
    print("error")

