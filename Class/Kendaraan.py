class Kendaraan:
    def __init__(self, warna = "Hitam", tahun = "2020", noPlat = "BE 0505 ROY"):
        self.__warna = warna
        self.__tahun = tahun
        self.__noPlat = noPlat

    def getWarna(self):
        return self.__warna
    
    def setWarna(self, warna):
        self.__warna = warna
        
    def getTahun(self):
        return self.__tahun
    
    def setTahun(self, tahun):
        self.__tahun = tahun
        
    def getNoplat(self):
        return self.__noPlat
    
    def setNoplat(self, noPlat):
        self.__noPlat = noPlat
    
    def __str__(self):
        return "Warna Kendaraan\t\t: " + self.__warna  + "\nTahun Kendaraan\t\t: "+ self.__tahun  + "\nNo Plat Kendaraan\t: "+ self.__noPlat