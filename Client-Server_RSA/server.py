# Import library yang dibutuhkan
import socket  # Untuk meng-handle komunikasi socket
import pickle  # Untuk serialisasi/pickle objek
import sys
from key_generation import *  # key_generation berisi fungsi generate_keypair() dan decrypt()

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mendapatkan nama mesin lokal dan port
host = socket.gethostname()
port = 8080

# Binding ke port
server_socket.bind((host, port))

# Listen untuk koneksi masuk
server_socket.listen(5)

print('Menghubungkan Koneksi....')

# Membangun koneksi dengan klien
client_socket, addr = server_socket.accept()
print('Menerima Koneksi dari ip : ', addr)

# Generate pasangan kunci RSA
public_key, private_key = generate_keypair()

# Mengirim kunci publik ke klien
client_socket.send(pickle.dumps(public_key))

while True:
    # Menerima pesan terenkripsi dari klien
    encrypted_message = client_socket.recv(4096)
    encrypted_message = pickle.loads(encrypted_message)

    # Mendekripsi pesan yang diterima
    decrypted_message = decrypt(private_key, encrypted_message)
    print('Menerima Pesan Terenkripsi:', encrypted_message)
    print('Mendeskripsi Pesan:', decrypted_message)
    print("\n")

    # Memeriksa apakah pesan yang diterima adalah 'q'
    if decrypted_message == 'q':
        print('Sampai jumpa lagi!!!!!')
        client_socket.close()
        break

# Exit program
sys.exit(0)
