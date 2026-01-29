## main sayfasında bağlantiya erişip bilgileri sıralayan python programı
# order by > artan veya azalan sıralama

from main import baglan, ekle

def siralama():
    baglanti = baglan()
    sql_komut = baglanti.cursor()
    sql_komut.execute(" select * from bilgiler order by no DESC ")
    for kayit in sql_komut.fetchall():
        print(kayit)

def delete():
    ## bir noya göre kayıt silen python metodu
    ara = int(input("Hangi Kayıt Silinsin: "))
    baglanti = baglan()
    sql_komut = baglanti.cursor()
    sql_komut.execute(f" delete from bilgiler where no={ara} ")
    baglanti.commit() # veritabanını onayladık
    print(f"\n {ara} nolu kayıt silindi ")


# def kolonsil():
#     # sütunu silme işlemi
#     baglanti = baglan()
#     sql_komut = baglanti.cursor()
#     sql_komut.execute("""   alter table bilgiler
#                             drop column tel""")
#     baglanti.commit()
    
ekle()   
    
    
# kolonsil()    
siralama() # sıralama metodu
delete()   # silme metodu