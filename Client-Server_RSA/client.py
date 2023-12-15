# Import library yang dibutuhkan
import socket  # Untuk meng-handle komunikasi socket
import pickle  # Untuk serialisasi/pickle objek
import sys
from key_generation import *  # key_generation berisi fungsi-fungsi is_prime, gcd, mod_inverse, generate_keypair, encrypt, dan decrypt

# Inisialisasi socket klien
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mendapatkan nama mesin server dan port
host = socket.gethostname()
port = 8080

# Menghubungkan dengan server
client_socket.connect((host, port))

# Menerima kunci publik dari server
public_key = pickle.loads(client_socket.recv(4096))

while True:
    # Pesan yang akan dikirim
    # message = "Hello, RSA Encryption!"
    message = input('Masukkan pesan Anda: ')

    # menutup jika mengetik q 
    if message == 'q':
        # Menutup socket
        print("\n")
        print('Pesan Berahir')
        encrypted_message = encrypt(public_key, message)
        client_socket.send(pickle.dumps(encrypted_message))
        break

    # Mengenkripsi pesan menggunakan kunci publik yang diterima
    encrypted_message = encrypt(public_key, message)
    print('Pesan Asli:', message)
    print('Pesan Terenkripsi:', encrypted_message)
    print("\n")

    # Mengirim pesan terenkripsi ke server
    client_socket.send(pickle.dumps(encrypted_message))

# Menutup socket klien
client_socket.close()
sys.exit(0)
