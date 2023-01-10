from Kendaraan import Kendaraan
class Mobil(Kendaraan):
    def __init__(self, merek, namaMobil, kapasitasPenumpang, roda):
        super().__init__()
        self.__merek = merek
        self.__namaMobil = namaMobil
        self.__kapasitasPenumpang = kapasitasPenumpang
        self.__roda = roda
    
    def getMerek(self):
        return self.__merek
    
    def setMerek(self, merek):
        self.__merek = merek
        
    def getNamaMobil(self):
        return self.__namaMobil
    
    def setNamaMobil(self, namaMobil):
        self.__namaMobil = namaMobil
    
    def getKapasitasPenumpang(self):
        return self.__kapasitasPenumpang
    
    def setKapasitasPenumpang(self, kapasitasPenumpang):
        self.__kapasitasPenumpang = kapasitasPenumpang
    
    def getRoda(self):
        return self.__roda
        
    def setRoda(self, roda):
        self.__roda = roda