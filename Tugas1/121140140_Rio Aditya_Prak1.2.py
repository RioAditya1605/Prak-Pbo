"""
Nama : Rio Aditya
NIM : 121140140
Kelas : RB
"""

## Soal no 2
username = ("informatika")
password = ("12345678")

i=int(1)
while(i<=3):
    user=input("Masukkan username: ")
    pw=input("Masukkkan password: ")
    if (user == username and pw == password):
        print("Berhasil login")
        break
    elif(i==3):
        print("Akun anda diblokir")
        break
    else:
        print("username atau password salah coba lagi!")
    i += 1
