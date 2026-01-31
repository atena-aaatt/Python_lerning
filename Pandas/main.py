## exele çevirme işlemi  >  pip install openpyxl

import pandas as pd
veri = pd.read_csv("./olimpiyatlar.csv") 
# print(veri.head(6))
## tablonun türü ve özellikleri, dosya boyutu
# print(veri.info())
## Veri Setinin Sütun Başlığı Bilgisi
print(veri.columns) ## colums değişken tipinde olduğu için parantez yoktur
## veri.rename Veri Seti Sütun Başlıklarını Değiştir (TR olarak değiştir)

veri.rename(
    columns={
        "ID":"ID", "Name":"adi","Sex":"Cinsiyet","Age":"yas",
        "Height":"boy","Weight":"kilo","Team":"takim","NOC":"noc",
        "Games":"oyun","Year":"yil","Season":"sezon","City":"sehir",
        "Sport":"spor","Event":"olay","Medal":"madalya"
    }, inplace=True
)
# inplace=True  : varolan başlık ile yeni başlıkları değiştir
print(veri.head(5))

## 16 ARALIK DERS BAŞLANGICI
## Yararsız Veriyi Çıkarma İşlemi: Drop işlemi
print(" YENI TABLO ".center(25,"-"))
## id ve oyun sütununu tablodan çıkarma işlemi
veri = veri.drop(labels=["ID","oyun"],axis=1)
print(veri.head(3)) 

## Boş veya Nan yazan değerleri ortalama değerler ile değiştir
benzersiz = pd.unique(veri.olay)
print("Etkinlik:",len(benzersiz))
print(benzersiz[:5])

## boy ve kilo boş değerlerini düzeltme
veri_gecici = veri.copy()  # varolan tabloyu geçici değişkene atadık
boy_kilo = ["boy","kilo"]
print(boy_kilo)

import numpy as np # numpy modülünü dahil ettik

# 760 tane kayıt içinde dolaş
for e in benzersiz:
    # aranılan kayıt bulunduysa filtre içine gönder
    etkinlik_filtre = veri_gecici.olay == e
    veri_filtre = veri_gecici[etkinlik_filtre]
    
    # ortalama değişkeni olarak ayarla
    for boyvekilo in boy_kilo:
        ortalama = np.round(np.mean(veri_filtre[boyvekilo]), 2)
        if ~np.isnan(ortalama):
            veri_filtre[boyvekilo] = veri_filtre[boyvekilo].fillna(ortalama)
        else:
            tumVeriOrtalamasi = np.round(np.mean(veri[boyvekilo]), 2)
            veri_filtre[boyvekilo] = veri_filtre[boyvekilo].fillna(tumVeriOrtalamasi)
    
    veri_gecici[etkinlik_filtre] = veri_filtre

veri = veri_gecici.copy()


## YAŞ SÜTUNU İÇİN KAYIP VERİYİ DÜZELTME > nan veya null değerlerini yasort ile değiştir
yasort = np.round(np.mean(veri.yas), 2)
veri["yas"] = veri["yas"].fillna(yasort)

print(veri.info())  # non-null boş değer olup olmadığını gösterir

## MADALYA ALAMAYAN SPORCULARI TEMİZLEME
madalya = veri["madalya"] # madalya sütununu bul
print("Madalya Alamayan Sayısı:", pd.isnull(madalya).sum()) # toplam : 231333 adet

madalya_filtre = ~pd.isnull(madalya)
veri = veri[madalya_filtre]
print(veri.head(4))

veri.to_csv("duzenlenmis_olimpiyatlar.csv")