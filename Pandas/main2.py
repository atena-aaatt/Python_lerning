import pandas as pd

tablo, satirno = [] , []

for satir in range(1,6):
    kayit = input("Demirbaş Girin: ")
    satirno.append(satir)
    tablo.append(kayit)

data = pd.DataFrame(data=tablo, columns=["Demirbas"],  index=satirno)
print(data)

# data.to_html("data.html")

## Birden fazla Satır ve Sütun ile çalışma
import numpy as np
## rasgele 10-30 arasında 5x5 lik matris oluştur
rasgele = np.random.randint(10,30 , (5,5))

satir_listesi = []
for satir in range(1, len(rasgele) + 1):
    satir_listesi.append(str(satir) + ". Değer")

yeni_liste = pd.DataFrame(data=rasgele, 
            index=[1,2,3,4,5], columns=satir_listesi)
print(yeni_liste)
yeni_liste.to_html("ogrlist.html")
    