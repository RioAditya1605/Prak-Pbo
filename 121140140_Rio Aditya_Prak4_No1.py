class komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

class processor(komputer):
    def __init__(self, merk, nama, harga, jumlah_core, kecepatan_processor):
        super().__init__(nama, "processor", harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

class RAM(komputer):
    def __init__(self, merk, nama, harga, capacity_ram):
        super().__init__(nama, "RAM", harga, merk)
        self.capacity_ram = capacity_ram

class HDD(komputer):
    def __init__(self, merk, nama, harga, capacity_hdd,rpm_hdd):
        super().__init__(nama, "HDD", harga, merk)
        self.capacity_hdd = capacity_hdd
        self.rpm_hdd = rpm_hdd

class VGA(komputer):
    def __init__(self, merk, nama, harga, capacity_vga):
        super().__init__(nama, "VGA", harga, merk)
        self.capacity_vga = capacity_vga

class PSU(komputer):
    def __init__(self, merk, nama, harga, daya_psu):
        super().__init__(nama, "PSU", harga, merk)
        self.daya_psu = daya_psu

rakit = [[processor('Intel','Core i7 7740X',4350000,4,'4.3GHz'),
        RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB'),
        HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200),
        VGA('Asus','VGA GTX 1050',250000,'2GB'),
        PSU('Corsair','Corsair V550',250000,'500W')],
         
        [processor('AMD','Ryzen 5 3600',250000,4,'4.3GHz'),
        RAM('G.SKILL','DDR4 2400MHz',328000,'4GB'),
        HDD('Seagate','HDD 2.5 inch',295000,'1000GB',7200),
        VGA('Asus','1060Ti',250000,'8GB'),
        PSU('Corsair','Corsair V550',250000,'500W')]]

for i, Komputer in enumerate(rakit):
    print("Komputer", i+1)
    for part in Komputer:
        print(part.jenis, part.nama," produksi", part.merk)
    print()