tahun = eval(input("Masukkan Tahun : "))
chineseZodiac = tahun % 12
if chineseZodiac == 0:
    print("monkey")
elif chineseZodiac == 1:
    print("rooster")
elif chineseZodiac == 2:
    print("dog")
elif chineseZodiac == 3:
    print("pig")
elif chineseZodiac == 4:
    print("rat")
elif chineseZodiac == 5:
    print("ox")
elif chineseZodiac == 6:
    print("tiger")
elif chineseZodiac == 7:
    print("rabbit")
elif chineseZodiac == 8:
    print("dragon")
elif chineseZodiac == 9:
    print("snake")
elif chineseZodiac == 10:
    print("horse")
else:
    print("sheep")
