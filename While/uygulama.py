# Sayı Tahmin oyunu 
# kullanıcının 3 hakkı var. 
# Bilgisayarın tuttuğu sayıya göre tahmini düşür veya yükselt uyarısı veriyor
from random import randint as rnd # randint yerine rnd kısaltması yaptık
hak = 1
tutulan_sayi = rnd(0,10)
# print(tutulan_sayi)
while (hak <= 3):
    tahmin = int(input("0-10 arası sayı girin: "))
    if (tutulan_sayi == tahmin):
        print(f"Tebrikler {hak} hakta bildiniz. Tutulan Sayı: {tutulan_sayi}")
        break  ## döngüyü bitirir.
    elif (tutulan_sayi > tahmin):
        print("Yükseltin")
        hak += 1
    elif (tutulan_sayi < tahmin):  # sadece else yazılabilir. 
        print("Düşürün")
        hak += 1
    
print("Tutulan Sayı:", tutulan_sayi)