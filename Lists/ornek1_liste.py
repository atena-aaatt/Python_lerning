# dışarıdan girilen adet kadar listeye eleman ekleyen python programı 

isimler = list() ## boş liste tanımladık

adet = int(input("Kaç isim girilecek: ")) ## tamsayı
for sayi in range(1,adet+1):
    girilenisim = input(str(sayi) + ". İsim Gir: ")
    isimler.append(girilenisim) ## listeye isim ekledik
    
## enumerate(liste)
print("Sıra No\tİsim")  # \t --> 4 krktr boşluk bırakır
for no,isim in enumerate(isimler, start=1):
    print(f"{no}\t{isim}".upper())
    