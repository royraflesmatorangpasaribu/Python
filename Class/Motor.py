from Kendaraan import Kendaraan
class Motor(Kendaraan):
    def __init__(self, merek, roda = 2):
        super().__init__()
        self.__merek = merek
        self.__roda = roda
    
    def getMerek(self):
        return self.__merek
    
    def setMerek(self, merek):
        self.__merek = merek
        
    def getRoda(self):
        return self.__roda
        
    def setRoda(self, roda):
        self.__roda = roda
        
    