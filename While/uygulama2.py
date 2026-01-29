## şehir oyunu 
## Girilen şehrin son karakteri ile diğer şehrin ilk karakteri eşleşiyorsa
# sürekli şehir girmesini sağlayan python programı:
## eskişehir > rize > edirne > erzincan > nevşehir > muğla

sehirler = list()
sayac = 1
while True:
    sehir = input(f"{str(sayac)}. Sehir: ")
    sayac += 1
    sehir2 = input(f"{str(sayac)}. Şehir: ")
    sayac += 1
    # continue > döngüyü başa sarar
    if (sehir[-1] == sehir2[0]):
        sehirler.append(sehir)
        sehirler.append(sehir2)
        continue 
    else:
        sehirler.append(sehir)
        print("Program Sonlandı")
        break

print(sehirler)