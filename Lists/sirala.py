renkler = ["sarı","Yeşil","MAVI","beyaz","mAvi", ".","!","5" ]
sehirler = ["ankara","istanbul","ordu","niğde","adana"]
# ['!', '.', '5', 'MAVI', 'Yeşil', 'beyaz', 'mAvi', 'sarı']
siralisehir = sorted(sehirler, reverse=1)
print(siralisehir)
renkler.sort(reverse=False)
## reverse=True > Tersten Sıralar (Azalan - DESC)
## reverse=False > Alfabetik Sıralar (Artan - ASC)
print(renkler)
# print(renkler[::-1])
print(sehirler)

## sorted(liste) > anlık olarak listeyi sıralar orijinal liste aynı kalır
## sorted(liste) > bir değişkene atanıp sonradan tekrar kullanılabilir.