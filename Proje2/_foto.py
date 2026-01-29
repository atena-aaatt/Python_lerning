from PyQt6.QtWidgets import *
from foto import Ui_Form_Anasayfa
from PyQt6.QtGui import QPixmap, QDesktopServices ## Fotoğrafı label içinde gösterme için kullandık
from PyQt6.QtCore import QUrl ## Web sitesine git
import sqlite3
## Eposta Gönderme Modülleri
from email.message import EmailMessage
import ssl, smtplib
## Klavye Dinleme Modülü > Qt
from PyQt6.QtCore import Qt


class Form_Anasayfa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = Ui_Form_Anasayfa()
        self.main.setupUi(self)
        
        ## Bilgiler Bölümü Başlangıçta Gizli olsun
        self.main.groupBox.hide()
        
        ## Menu Tıklama Olayları
        self.main.actionSiteye_Git.triggered.connect(self.siteyegit)
        self.main.mn_kapat.triggered.connect(self.kapat)
        self.main.btn_goster.clicked.connect(self.goster_gizle)
        self.main.btn_fotoekle.clicked.connect(self.fotoEkle)
        self.main.btn_kullanici_kayit.clicked.connect(self.kullanici_kayit)
        self.main.btn_oturumac.clicked.connect(self.oturumac)
        self.main.btn_guncelle.clicked.connect(self.guncelle)
        self.main.btn_eposta.clicked.connect(self.epostagonder) # eposta gönder
        
        ## Değişken tanımlamaları (Genel Tanımlamalar)
        self.eposta = self.main.txt_kullaniciadi
        self.parola = self.main.txt_parola
        self.rol = self.main.comboBox_rol
        self.kayit_kullaniciadi = self.main.txt_kayit_kullaniciadi
        self.kayit_eposta = self.main.txt_kayit_eposta
        self.kayit_parola = self.main.txt_kayit_parola
        self.kayit_rol = self.main.comboBox_kayit_rol
        self.eposta.setPlaceholderText("E-Posta Adresi")

        ## Güncelleme Tanımlamaları
        self.G_eposta = self.main.txt_guncelle_eposta
        self.G_PID = self.main.txt_guncelle_PID
        self.G_kullanici = self.main.txt_guncelle_kullaniciadi
        self.G_parola = self.main.txt_guncelle_parola
        self.G_eposta.setToolTip("Burası E-Posta Bilgisi İçermektedir")
        self.G_kullanici.setToolTip("Burası Kullanıcı Adı Bilgisi İçermektedir")
        ## Rol bölümünün bir işlevi olmadığı için tanımlamadım
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F1.value:
            QMessageBox.information(self, "Tuş Özelliği",
            " Bu uygulama İsmek Python eğitiminde yazılmıştır. Copyride © ")
        elif event.key() == Qt.Key.Key_Escape.value:
            print("ESC Tuşuna Basıldı Program Kapatılıyor")
            self.kapat()
            
    
    
    def epostagonder(self):
        try:
            gonderen = "sercantirmik@gmail.com"
            parola = "parola"  # gönderen kişinin 16 hanelik parolası
            kime = self.G_eposta.text()
            konu = "Parola Kurtarma ve Gönderi"
            mesaj = f" Kullanıcı:{self.G_kullanici.text()}\n Parola:{self.G_parola.text()}"
            ## mail değişkeni kullanarak yukarıdaki bilgileri gönder
            mail = EmailMessage()
            mail["From"]=gonderen
            mail["To"]=kime
            mail["Subject"]=konu
            mail.set_content(mesaj)
            ## ssl ve smtp bölümü
            icerik = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=icerik) as smtp:
                smtp.login(gonderen, parola)
                smtp.sendmail(gonderen, kime, mail.as_string())
        except Exception as hatakodu:
            QMessageBox.critical(self, "Mail Hatası", "HATA\n"+str(hatakodu))
        
        
    def guncelle(self):
        try:
            baglan = self.baglanti()
            komutsatiri = baglan.cursor()
            komutsatiri.execute(f""" update tbl_uyeler
            set EPOSTA="{self.G_eposta.text()}", KULLANICI_ADI="{self.G_kullanici.text()}",
            PAROLA="{self.G_parola.text()}", FOTO="{self.dosyayol[0]}"
            where PID={int(self.G_PID.text())}   """)
            baglan.commit()
            QMessageBox.information(self, "Güncelleme","Bilgiler Güncellenmiştir")
            self.temizle()
        except Exception as hatakodu:
            QMessageBox.critical(self, "HATA","Bir hata oluştu \n"+str(hatakodu))
    
    def temizle(self):
        self.eposta.setText(self.G_eposta.text()) # bilgisini kopyaladık oturum aç eposta bilgisine atadık
        self.parola.clear()  # Kullanıcı Yeni Parolasıyla giriş yapsın
        ## txtbox içeriğini temizleme metodu
        self.G_eposta.clear()
        self.G_kullanici.clear()        
        self.G_parola.clear()
        self.G_PID.clear()
        self.main.txt_guncelle_rol.clear()
        ## Oturum kapandığında varsayılan kullanıcı fotosu ekle
        self.main.label_fotoekle.setPixmap(QPixmap("./user.png"))
        self.main.groupBox.setVisible(False) ## Groupbox gizlensin (sağdaki)
        
    def baglanti(self):
        with sqlite3.connect("./kullanicilar.db") as baglan:
            komutsatiri = baglan.cursor()
            komutsatiri.execute(""" create table if not exists tbl_uyeler
            (PID INT, EPOSTA TEXT, KULLANICI_ADI TEXT, PAROLA TEXT, ROL TEXT, FOTO TEXT) """)
            return baglan
    
    def siteyegit(self):
        url = QUrl("https://enstitu.ibb.istanbul/portal/default.aspx")
        QDesktopServices.openUrl(url)
    
    def oturumac(self):
        try:
            ## bilgilerin dolu olmasını kontrol ediyoruz
            if (self.eposta.text() != "") or (self.parola.text() != ""):
                baglan = self.baglanti()
                komutsatiri = baglan.cursor()
                komutsatiri.execute(" select * from tbl_uyeler ")
                uyeler = komutsatiri.fetchall()
                # print(uyeler[0][1])
                for uye in uyeler:
                    # print(uye[1], uye[3]) # uye epostasını ve parolasını göster
                    if (self.eposta.text() == uye[1]) and (self.parola.text() == uye[3]):
                        
                        ## Bilgileri Göster Bölümünü Doldur
                        self.main.txt_guncelle_PID.setText(str(uye[0]))
                        self.main.txt_guncelle_eposta.setText(uye[1])
                        self.main.txt_guncelle_kullaniciadi.setText(uye[2])
                        self.main.txt_guncelle_parola.setText(uye[3])
                        self.main.txt_guncelle_rol.setText(uye[4])
                        self.main.label_fotoekle.setPixmap(QPixmap(uye[5]))
                        
                        self.main.groupBox.show() # Bilgileri göster
                        
            else:
                QMessageBox.critical(self, "Oturum Açma Hatası", "Hatalı Giriş")
        except Exception as hatakodu:
            QMessageBox.critical(self, "HATA", "Bir Hata Oluştu \n"+str(hatakodu))
    
    
        
    def kullanici_kayit(self):
        from random import randint as rnd # rasgele sayı üret
        if (self.kayit_eposta.text() == "") or (self.kayit_kullaniciadi.text() == "") or (self.kayit_parola.text() == ""):
            QMessageBox.critical(self, "Kayıt Hatası", "Yukarıdaki İlgili Alanları Doldurunuz.")
        else:
            # Fotoğraf seçili mi kontrol et
            try:
                # kayıt işlemini başlat (insert into çalışsın)
                self.PID = rnd(1000,9000) # Personel ID rasgele üret
                baglan = self.baglanti()
                komutsatiri = baglan.cursor()
                komutsatiri.execute(f""" insert into tbl_uyeler values
                ({self.PID}, "{self.kayit_eposta.text()}", 
                "{self.kayit_kullaniciadi.text()}", "{self.kayit_parola.text()}",
                "{self.kayit_rol.currentText()}", "{self.dosyayol[0]}")  """)
                baglan.commit()
                QMessageBox.information(self,"Kayıt İşlemi", 
                f"Kişi {self.PID} numarasıyla sisteme kayıt edilmiştir.")
                ## Kişi kayıt olduktan sonra oturum aç sayfasında bilgileri gelsin
                self.eposta.setText(self.kayit_eposta.text())
                self.main.tabWidget.setCurrentIndex(0)
            except Exception as hatakodu: 
                QMessageBox.warning(self,"Uyarı","Hata Oluştu \n" + str(hatakodu))
    
    def fotoEkle(self):
        ## Fotoğraf Seçmeyi Zorunlu Yaptık
        while True:
            self.dosyayol = QFileDialog.getOpenFileName(self, "Fotoğraf Seç", "",
                            " png (*.png) ;; jpg (*.jpg) ")
            # Fotoğraf seçili değilse veya Iptale basıldıysa
            if self.dosyayol[0] == "": 
                QMessageBox.warning(self,"Foto Uyarısı","Bir Fotoğraf Seçin")
            else:
                gorsel = self.main.label_fotoekle
                gorsel.setPixmap(QPixmap(self.dosyayol[0]))
                self.main.btn_fotoekle.setText("") ## Buton içindeki yazıyı sil
                break        
        

    def goster_gizle(self):
        # butonun tıklı mı kontrolünü yapıyoruz > True Değeri Döner
        if self.main.btn_goster.isChecked():
            self.parola.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.parola.setEchoMode(QLineEdit.EchoMode.Password)
            
    def kapat(self):
        QMessageBox.warning(self, "Program Kapatılıyor", "Program Sonlandırıldı.")
        quit()