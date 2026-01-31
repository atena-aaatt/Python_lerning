## SIFIRLARDAN VE BİRLERDEN OLUŞAN NUMPY
import numpy as np
## sıfırlardan oluşan 2 boyutlu dizi oluştur
sifirlar_dizisi = np.zeros((4,3))
print(sifirlar_dizisi)
## birlerden oluşan 2 boyutlu dizi oluştur
birler_dizisi = np.ones((3,4))
print(birler_dizisi)

# aralıklı sayısal işlemleri gösteren linspace kullanımı
# başlangıç ve bitiş sabit, diğer sayılar eşit bir şekilde dağılmış
## np.linspace(başla,bitiş,sayı_adeti)
aralikli_dizi = np.linspace(1,10,7)
print("Aralıklı Dizi:", aralikli_dizi )

## RASGELE SAYILAR OLUŞTURAN NUMPY METODU
rasgele1 = np.random.randint(low=4, high=10)
print("Rasgele Bir Sayı Üretir:",rasgele1)

## RASGELE SAYILARDAN OLUŞAN DİZİ İŞLEMİ
rasgele_dizi = np.array([
    np.random.randint(5,10,3),
    np.random.randint(5,10,3),
    np.random.randint(5,10,3)
])
print("Rasgele Dizi Elemanları:", rasgele_dizi)
print("Rasgele Dizi Toplamı:\n",sum(rasgele_dizi))

## RASGELE DEĞERDE İÇ İÇE KULLANIM > 4-10 arasında 5x5 lik tablo oluştur
print()
rasgele_dizi2 = np.random.randint(4,10,(5,5))
print(rasgele_dizi2)

## RASGELE ONDALIKLI SAYILAR
print() ## boş satır olması için
rasgele_ondalik = np.random.randn()
print(rasgele_ondalik)

rasgele_ondalik_dizi = np.random.uniform(2,10,(6,6))
print("2-10 arasında 6x6 lık rasgele ondalık sayı tablosu\n".upper(),
      rasgele_ondalik_dizi)

print(round(rasgele_ondalik_dizi.max(),4)) ## enb
print(round(rasgele_ondalik_dizi.min(),4)) ## enk
print(rasgele_ondalik_dizi.argmax()) ## enb sayının index nosu
print(rasgele_ondalik_dizi.argmin()) ## enk sayının index nosu

## İKİ DİZİYİ BİRLEŞTİRME
dizi1 = np.random.randint(5,15,(5,5))
dizi2 = np.random.randint(5,15,(5,5))
## iki diziyi bir dizide birleştirmek için köşeli parantez kullandık
## dtype (veri tipi) olarak : float, int, str tiplerine dönüşüm olabilir
birlesim_dizisi = np.concatenate([dizi1,dizi2],axis=1, dtype=float)
print(dizi1)
print(dizi2)
print(" BİRLEŞTİRİLMİŞ DİZİ ".center(35,"▒"))  # alt+177
print(birlesim_dizisi)
## axis=1 : her dizinin satırlarını yanyana gelecek şekilde birleştirir 