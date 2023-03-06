class Biodata:
    def __init__(self, nama, NIM, Kelas_PBO_Siakad, Jumlah_SKS):
        self.nama = nama
        self.NIM = NIM
        self.Kelas_PBO_Siakad = Kelas_PBO_Siakad
        self.Jumlah_SKS = Jumlah_SKS

    def Bio(self):
        print("Nama         : ", self.nama)
        print("NIM          : ", self.NIM)
        print("Kelas        : ", self.Kelas_PBO_Siakad)
        print("Jumlah SKS   : ", self.Jumlah_SKS)

biodata = Biodata("Rio Aditya", "121140140", "RB", 3)
biodata.Bio()