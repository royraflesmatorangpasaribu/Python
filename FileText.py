import os
def main():
    pilihan = 0
    while pilihan !=5:
        while(True):
            try:
                print("\t\tMenu File \nProgram By Roy Rafles Matorang Pasaribu (2117051058) ")
                print("\n1 : Membuat File \n2 : Membaca File \n3 : Menambah File \n4 : Hapus File \n5 : Keluar Program")
                pilihan = int(input("Pilihan : "))
                if pilihan<=0 or pilihan>5 :
                    raise ValueError
                print("")
                break
            except :
                print("Masukkan Pilihan 1, 2, 3, 4, 5! BUKAN HURUF ATAU KATA!!!\n")
    
        if pilihan == 1:
            nama_file = input("Masukkan nama file (.txt) :")
            try:
                outfile = open(nama_file, "x")
            except FileExistsError:
                print("Nama File Sudah Ada!!")
            else:
                outfile.write(input("Masukkan teks : "))
                outfile.close()
                print("NOTIFIKASI : File", nama_file, "Berhasil Dibuat \n")
           
        elif pilihan == 2:
            nama_file = input("Masukkan nama file (.txt) :")
            try:
                infile = open(nama_file, "r")
                print(infile.read())
                infile.close()
            except FileNotFoundError:
                print("Nama File", nama_file , "Tidak ada")
            
        elif pilihan == 3:
            nama_file = input("Masukkan nama file (.txt) : ")
            try:
                with open(nama_file, 'r') as nf:
                    print("\nisi dari file yang dipilih : ")
                    print(nf.read())
                isi = input('\nTambahkan teks ke file yang dipilih : ')
                outfile = open(nama_file, 'a')
                outfile.write("\n")
                outfile.write(isi)
                outfile = open(nama_file, 'r')
                print("NOTIFIKASI : Teks", isi, "Berhasil ditambahkan pada File", nama_file,"\n") 
                print(outfile.read())
                outfile.close()            
            except FileNotFoundError:
                print("Nama File", nama_file , "Tidak ada")
           
        elif pilihan == 4:
            nama_file = input("Masukkan nama file (.txt) : ")
            try:
                os.remove(nama_file)
                print("NOTIFIKASI : File", nama_file, "Berhasil Dihapus \n")
            except FileNotFoundError:
                print("Nama File", nama_file , "Tidak ditemukan")
main()
