# Rasgele oluşturulan listeye eleman ekleyen python programı:

from random import randint as rnd
tekler , ciftler = [] , []
# 20 adet rasgele sayı üret ve bunun çift-tek
# olma durumuna göre listelere ata.
for i in range(20):
    rasgele = rnd(20,200)
    if (rasgele % 2 == 0):
        ciftler.append(rasgele)
    else:
        tekler.append(rasgele)

if (len(ciftler) > len(tekler)):
    print(f"Çiftler Listesi: {len(ciftler)}\n{ciftler}")
else:
    print(f"Çiftler Listesi: {len(tekler)}\n{tekler}")

## sum(liste)  > metodu kullanımı : 
#   Verilen listedeki sayılar toplamını verir.
print(f""" Listedeki Değerler Toplamı: 
    1- Çiftler Toplamı: {sum(ciftler)}
    2- Tekler Toplamı.: {sum(tekler)}""")