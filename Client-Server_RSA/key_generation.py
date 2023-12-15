import random
import math
import sys

# Fungsi untuk menghitung Faktor Persekutuan Terbesar (FPB) atau GCD
def gcd(a, b):
    if b == 0:
        result = a
    else:
        result = gcd(b, a % b)
    return result

# Fungsi untuk menemukan invers perkalian modulo
def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2 + phi

    return d

# Fungsi untuk mengecek apakah suatu bilangan prima
def is_prime(num):
    # Memeriksa apakah bilangan kurang dari atau sama dengan 1
    if num <= 1:
        return False

    # Iterasi melalui rentang dari 2 hingga akar kuadrat dari bilangan
    for i in range(2, int(pow(num, 0.5)) + 1):
        # Memeriksa apakah bilangan dapat dibagi oleh i
        if num % i == 0:
            # Jika i dapat membagi bilangan, maka bukan bilangan prima
            return False

    # Jika tidak ada i yang membagi bilangan, maka bilangan adalah prima
    return True


# Fungsi untuk menghasilkan bilangan prima besar 'p' dan 'q'
def generate_large_primes():
    # Membuat daftar (list) dari bilangan prima di antara 100 hingga 999
    primes = [i for i in range(1, 100) if is_prime(i)]
    
    # Memilih bilangan prima acak untuk p dan q
    p = random.choice(primes)
    q = random.choice(primes)
    
    # Memastikan bahwa p dan q tidak sama
    while p == q:
        q = random.choice(primes)
    
    # Mengembalikan pasangan bilangan prima (p, q)
    return p, q


# Fungsi untuk menghasilkan pasangan kunci RSA (public key, private key)
def generate_keypair():
    p, q = generate_large_primes()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    gcd_value = gcd(e, phi)
    while gcd_value != 1:
        e = random.randrange(1, phi)
        gcd_value = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# Fungsi untuk mengenkripsi pesan
def encrypt(public_key, plain_text):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plain_text]
    return cipher

# Fungsi untuk mendekripsi pesan
def decrypt(private_key, cipher_text):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(plain)

# Program Utama
if __name__ == "__main__":
    # Membuat pasangan kunci RSA
    public_key, private_key = generate_keypair()
    
    # Pesan yang akan dienkripsi
    message = 'hi!!!!'
    print("Pesan Asli:", message)

    # Melakukan enkripsi menggunakan kunci publik
    encrypted_message = encrypt(public_key, message)
    print("Pesan Terenkripsi:", ''.join(str(el) for el in encrypted_message))
    print("Pesan Terenkripsi [versi list]:", encrypted_message)
    print("Kunci Publik:", public_key)

    # Melakukan dekripsi menggunakan kunci privat
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Pesan Terdekripsi:", decrypted_message)
    print("Kunci Privat:", private_key)
