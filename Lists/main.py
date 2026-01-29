## Liste İşlemleri
liste = []  # boş liste
liste2 = list() # boş liste

renkler = ["sarı","yeşil","mavi","beyaz"]
print(renkler)

## Liste Metotları (Ekleme)
renk = input("Renk Girin: ")
# renkler.append(renk) # sona eleman ekler
# renkler.insert(0,renk) # belirtilen indexe göre eleman ekler
sayilar = [1,2,3]
renkler.extend(sayilar)
print(renkler)