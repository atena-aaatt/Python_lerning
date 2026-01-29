## Veritabanı işlemleri
import sqlite3


def baglan():
    ## connect veritabanı başlantısı için kullanılan metot
    with sqlite3.connect("./database.db") as baglanti:
        # kayıtları gezen ve işlem yapan bir komut satırı
        sql_komut = baglanti.cursor() 
        # her satır için çalışacak sql komutu yazılır
        sql_komut.execute("""   create table if not exists bilgiler 
                                (no INT, adi TEXT, soyadi TEXT,
                                tel TEXT, adres TEXT) """)
        return baglanti


def ekle():
    from random import randint, choice
    ilceler = ["Bahçelievler","Avcılar","Küçükçekmece","Bakırköy"]
    ## Veri Giriş İşlemleri > Terminalden Giriş
    adi = input("Adınız: ")
    soyadi = input("Soyadınız: ")
    telefon = input("Telefon No: ")
    
    ## Veritabanına Başlantı Bölümü
    baglanti = baglan()
    sql_komut = baglanti.cursor() 
    ## tabloya yeni kayıt ekle
    sql_komut.execute(f"""   insert into bilgiler values   
                            ({randint(100,200)}, "{adi}", "{soyadi}", 
                             "{telefon}", "{choice(ilceler)}" ) """)
    baglanti.commit() # tabloda kayıt değiştiği/yeni kayıt için commit() kullandık
    print("\n Bilgiler Kaydedilmiştir")
    
# ekle()



def listele():
    baglanti = baglan()
    sql_komut = baglanti.cursor()
    sql_komut.execute(""" select * from bilgiler """)
    print("NO     ADI   SOYADI   TELEFON   ADRES") ## Sütun Oluştur
    # for döngüsü ile alt alta kayıtları yazdır
    for kayit in sql_komut.fetchall():
        ## 123 nolu öğrencinin bilgilerini getir
        if kayit[0] == 123:
            print( kayit[1], kayit[2], kayit[3], kayit[4])

def kararlistele():
    baglanti = baglan()
    sql_komut = baglanti.cursor()
    sql_komut.execute(""" select * from bilgiler where no=123 """)
    for kayit in sql_komut.fetchall():
        print( kayit[1], kayit[2], kayit[3], kayit[4])


def adsoyadlistele():
    baglanti = baglan()
    sql_komut = baglanti.cursor()
    sql_komut.execute(""" select adi,soyadi from bilgiler """)
    for kayit in sql_komut.fetchall():
        print(kayit)
    
kararlistele()