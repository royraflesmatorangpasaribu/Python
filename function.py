nama = input("Masukkan Nama : ")
npm = eval(input("Masukkan NPM  : "))
nilai = eval(input("Masukkan Nilai : "))

def convertToHurufMutu():
    if nilai <= 100 and nilai >= 76:
        hurufMutu = "A"
    elif nilai < 76 and nilai >= 71:
        hurufMutu = "B+"
    elif nilai < 71 and nilai >= 66:
        hurufMutu = "B"
    elif nilai < 66 and nilai >= 61: 
        hurufMutu = "C+"
    elif nilai < 61 and nilai >= 56:
        hurufMutu = "C"
    elif nilai < 56 and nilai >= 50:
        hurufMutu = "D"
    elif nilai < 50 and nilai >= 0:
        hurufMutu = "E"
    else : 
        hurufMutu = "Huruf Mutu Tidak Tersedia"
    return hurufMutu

print("")
print("Nama : ", nama)
print("NPM  : ",npm)
print("Huruf Mutu :" ,convertToHurufMutu())
