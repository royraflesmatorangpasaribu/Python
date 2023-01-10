from Mobil import Mobil
from Motor import Motor
def main() :
    
    Kendaraanmotor = Motor("Honda")
    print(Kendaraanmotor)
    print()
    print("Warna Kendaraan Motor\t: ", Kendaraanmotor.getWarna())
    print("Merek Motor\t\t: ", Kendaraanmotor.getMerek())
    print("No Kendaraan\t\t: ", Kendaraanmotor.getNoplat())
    print("Jumlah Roda\t\t: ", Kendaraanmotor.getRoda())
    print("Tahun Kendaraan\t\t: ", Kendaraanmotor.getTahun())
    
    print()
    kendaraanMobil = Mobil("Toyota", "Kijang Innova", 8, 4)
    kendaraanMobil.setWarna("Putih")
    print("Warna Kendaraan Mobil\t: ", kendaraanMobil.getWarna())
    print("Merek Mobil\t\t: ", kendaraanMobil.getMerek())
    print("Nama Mobil\t\t: ", kendaraanMobil.getNamaMobil())
    kendaraanMobil.setNoplat("BE 2345 TOR")
    print("No Kendaraan\t\t: ", kendaraanMobil.getNoplat())
    print("Kapasitas Tampung\t: ", kendaraanMobil.getKapasitasPenumpang())
    kendaraanMobil.setTahun("2012")
    print("Jumlah Roda\t\t: ", kendaraanMobil.getRoda())
    print("Tahun Kendaraan\t\t: ", kendaraanMobil.getTahun())
    
main()
