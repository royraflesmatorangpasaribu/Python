import math

class PersegiPanjang:
  # construct a Persegi Panjang object
    def __init__(self, panjang = 1, lebar = 1):
      self.panjang = panjang
      self.lebar = lebar

    def getKeliling(self):
      return 2 *(self.panjang + self.lebar)

    def getLuas(self):
      return self.panjang * self.lebar

    def getPanjang(self):
      return self.panjang
    
    def getLebar(self):
      return self.lebar

    def setPanjang(self, panjang):
      self.panjang = panjang

    def setLebar(self, lebar):
      self.lebar = lebar

print("Persegi Panjang")
obj1=PersegiPanjang(5, 5)
print("Keliling : " ,obj1.getKeliling())
print("Luas : " ,obj1.getLuas())
print("Panjang : ",obj1.getPanjang())
print("Lebar : ", obj1.getLebar())

print("")
obj1.setPanjang(12)
obj1.setLebar(16)
print("Panjang Setelah di set : ", obj1.getPanjang())
print("Lebar Setelah di set : ", obj1.getLebar())
print("Keliling : ", obj1.getKeliling())
print("Luas : ", obj1.getLuas())
