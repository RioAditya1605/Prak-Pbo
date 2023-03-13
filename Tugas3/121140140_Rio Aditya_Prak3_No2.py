class AkunBank:
    list_pelanggan = []
    
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.append(self)
        
    def lihat_menu(self):
        print("Selamat datang di Bank Awenk Sejahtera Selamanya")
        print("Halo", self.__nama_pelanggan, "ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        
    def lihat_saldo(self):
        print(self.__nama_pelanggan," memiliki saldo Rp ", self.__jumlah_saldo)
        
    def tarik_tunai(self):
        nominal = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if nominal > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= nominal
            print("Saldo berhasil ditarik!")
        
    def transfer(self):
        nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
        no_rekening_tujuan = int(input("Masukkan no rekening tujuan: "))
        tujuan = None
        for pelanggan in AkunBank.list_pelanggan:
            if pelanggan.__no_pelanggan == no_rekening_tujuan:
                tujuan = pelanggan
                break
        if tujuan is None:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama.")
        else:
            if nominal > self.__jumlah_saldo:
                print("Nominal saldo yang Anda punya tidak cukup!")
            else:
                self.__jumlah_saldo -= nominal
                tujuan.__jumlah_saldo += nominal
                print("Transfer Rp ", nominal, " ke ", tujuan.__nama_pelanggan, " sukses!")

# membuat objek AkunBank
Akun1 = AkunBank(1234, "Rio Aditya", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

# simulasi penggunaan fungsi-fungsi AkunBank pada Akun1
Akun1.lihat_menu()
nomor_input = int(input("Masukkan nomor input: "))
while nomor_input != 4:
    if nomor_input == 1:
        Akun1.lihat_saldo()
    elif nomor_input == 2:
        Akun1.tarik_tunai()
    elif nomor_input == 3:
        Akun1.transfer()
    else:
        print("Nomor input tidak valid!")
    Akun1.lihat_menu()
    nomor_input = int(input("Masukkan nomor input: "))
print("Terima kasih telah menggunakan layanan Bank Awenk Sejahtera Selamanya!")