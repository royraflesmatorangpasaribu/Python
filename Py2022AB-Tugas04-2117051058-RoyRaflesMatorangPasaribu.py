sum = 0
for i in range(1,101):
    sum = sum + i
    rataRata = sum / 100
print("Rata-rata = ", rataRata)

s=0
for i in range(1, 101):
  x =(i-rataRata)**2
  s = s + x
varians = s/(100-1)
print("s^2 = ", varians)