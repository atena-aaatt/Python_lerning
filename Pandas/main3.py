## iloc (index location) ve loc (location) metotları: 

import pandas as pd

data = pd.read_csv("./ikv.csv")
# içinde veri olmadığı için diger_adlari sütununu sildik
data = data.drop(labels="diger_adlari", axis=1)
# anıt adı ve yapım tarihi listelensin (ilk 5 tane)
# print(data[["anit_adi" , "yapim_tarihi"]].head(7))

# adalarda ahşap ev kayıtlarını getir
print(data[(data["ilce_adi"] == "ADALAR") & (data["anit_adi"] == "AHŞAP EV") ])



