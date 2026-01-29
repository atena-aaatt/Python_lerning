## Listelerde for döngüsü kullanımı:
sehirler = [
    "ankara",
    "istanbul",
    "ordu",
    "niğde",
    "adana"]
# sehirler listesinin her sehri kadar dön.
for sehir in sehirler:
    print(sehir, end=" ")

print()
print("Döngü Bitti")    

## ---------- FOR DÖNGÜSÜ İKİNCİ KULLANIMI LİSTE DIŞI ----------

for sayi in range(5,1,-1): #  [1,2,3,4]
    print(sayi)
# range(baslangic,bitis,artis_miktari)
# baslangıc > bitiş olduğunda artış miktarı negatif olmalı
