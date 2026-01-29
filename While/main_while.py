## while ile main dosyasını çalıştırma.

# Rasgele oluşturulan listeye eleman ekleyen python programı:

from random import randint as rnd
tekler , ciftler = [] , []
# 20 adet rasgele sayı üret ve bunun çift-tek
# olma durumuna göre listelere ata.
sayac = 0
while (sayac < 20):
    rasgele = rnd(20,200)
    if (rasgele % 2 == 0):
        ciftler.append(rasgele)
        sayac = sayac + 1
    else:
        tekler.append(rasgele)
        sayac += 1  # sayacı 1 artır demektir.

if (len(ciftler) > len(tekler)):
    print(f"Çiftler Listesi: {len(ciftler)}\n{ciftler}")
else:
    print(f"Çiftler Listesi: {len(tekler)}\n{tekler}")

## sum(liste)  > metodu kullanımı : 
#   Verilen listedeki sayılar toplamını verir.
print(f""" Listedeki Değerler Toplamı: 
    1- Çiftler Toplamı: {sum(ciftler)}
    2- Tekler Toplamı.: {sum(tekler)}""")