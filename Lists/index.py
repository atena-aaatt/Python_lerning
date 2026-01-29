## Liste içindeki elemanlara erişim metotları: index, count

renkler = ["sarı","yeşil","MAVI","beyaz","mavi"]
arananEleman = input("Hangi Renk: ")  # mavi
print(renkler.index(arananEleman))  
print(renkler.count(arananEleman))   
print("Renkler Listesi Eleman Sayısı:",len(renkler))

## Girilen Rengi Listeden Silen Python Programı:
sil = renkler.pop(renkler.index(arananEleman))
print(f"{sil} rengi silindi Yeni Liste: {renkler}")

