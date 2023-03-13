class Mahasiswa:
    # Atribut kelas (static)
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, jurusan):
        # Atribut instance (public)
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

        # Atribut instance (private)
        self.__ipk = 0.0

        # Atribut instance (protected)
        self._sks = 0

        Mahasiswa.jumlah_mahasiswa += 1

    # Fungsi instance (public)
    def hitung_ipk(self, total_nilai, total_sks):
        self.__ipk = total_nilai / total_sks

    # Fungsi instance (public)
    def tambah_sks(self, sks):
        self._sks += sks

    # Fungsi instance (protected)
    def _fungsi_protected(self):
        print("Ini adalah fungsi protected")

    # Fungsi instance (private)
    def __fungsi_private(self):
        print("Ini adalah fungsi private")

    # Fungsi instance (public)
    def tampilkan_informasi(self):
        print(f"Nama        : {self.nama}")
        print(f"NIM         : {self.nim}")
        print(f"Jurusan     : {self.jurusan}")
        print(f"IPK         : {self.__ipk}")
        print(f"Total SKS   : {self._sks}")

mahasiswa1 = Mahasiswa("Rio Aditya", "121140140", "Teknik Informatika")

# Akses atribut instance public
print(mahasiswa1.nama)

# Akses atribut instance private (akan error)
#print(mahasiswa1.__ipk)

# Akses atribut instance protected (akan error)
#print(mahasiswa1._sks)

# Akses fungsi instance public
mahasiswa1.hitung_ipk(3.3, 22)
mahasiswa1.tambah_sks(22)
mahasiswa1.tampilkan_informasi()

# Akses fungsi instance protected (akan error)
#mahasiswa1._fungsi_protected()

# Akses fungsi instance private (akan error)
#mahasiswa1.__fungsi_private()

