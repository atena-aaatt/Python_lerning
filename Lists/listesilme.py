## Listede eleman silme işlemleri

renkler = ["sarı","yeşil","mavi","beyaz"]
silinenrenk = renkler.pop(1)
print(silinenrenk, "Rengi Silindi \n Yeni Liste",renkler)
## pop ile sildiğiniz elemanı bir değişkene atayabilirsiniz.
## Eleman sondan siler veya bir index nosuna göre de silinebilir.
renkler.remove("sarı")
print(renkler)
## Remove ile silinen eleman değişkene atanamaz
## Remove eleman ismiyle siler, pop > indexe göre siler

renkler.clear() ## Listenin tüm elemanlarını siler. Boş liste
print("Boş Liste",renkler)
del renkler
renkler = ["ali","can"]
print(renkler)
