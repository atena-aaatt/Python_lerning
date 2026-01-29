from PyQt6.QtWidgets import *
from giris import Ui_Form_Giris
import sqlite3, random


class Giris_Formu(QMainWindow):
    def __init__(self):
        super().__init__()
        ## giris formu için g2 değişkenini tanımladık
        self.g2 = Ui_Form_Giris()
        self.g2.setupUi(self)
        self.kontrol()
        
        ## Buton Tıklama Olayları
        self.g2.btn_yenile.clicked.connect(self.kontrol)
        self.g2.btn_giris.clicked.connect(self.giris)
        self.g2.btn_uyeOl.clicked.connect(self.uyeol)
        self.g2.btn_goster.clicked.connect(self.goster) # parolayı normal göster
                
        ## Metin Kutusu Kısaltmaları > bütün metotlarda kullanılması için self yazdık 
        ## Global Kullanım
        self.uye_eposta = self.g2.txt_uyeEposta
        self.uye_username = self.g2.txt_uyeUsername
        self.uye_password = self.g2.txt_uyePassword
        self.uye_pass_tekrar = self.g2.txt_uyePasswordTekrar
        self.uye_rol = self.g2.combo_uyeRol

    def kontrol(self):
        from string import ascii_lowercase, ascii_uppercase, punctuation
        buyuk = random.choice(ascii_uppercase)
        kucuk = random.choice(ascii_lowercase)
        ozel  = random.choice(punctuation)
        rakam = str(random.randint(0, 9))
        self.birlestir = buyuk + kucuk + ozel + rakam
        ## Karakterleri Label İçinde Göster
        self.g2.label_yazilar.setText(self.birlestir) 
    
    def goster(self):
        ## Buton onaylı mı? > True
        if (self.g2.btn_goster.isChecked()):
            self.g2.txt_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.g2.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        
    def uyeol(self):
        try:
            if (self.uye_password.text() != self.uye_pass_tekrar.text()) or  (self.birlestir != self.g2.txt_yazilar.text()):
                QMessageBox.warning(self, "Uyarı", "Bilgiler Eşleşmiyor")
                
            else:
            
                IDNO = str(random.randint(100, 999)) ## IDNO text olduğu için str tür dönüşümü yaptık
                baglan = self.baglanti()
                komut = baglan.cursor()
                komut.execute(f""" insert into tbl_uyeler values 
                                ("{IDNO}", "{self.uye_eposta.text()}",
                                "{self.uye_username.text()}",   -- Yorum satırı DOĞRU 😊
                                "{self.uye_password.text()}", 
                                "{self.uye_rol.currentText()}")  """)
                baglan.commit()
                QMessageBox.information(self, "Kayıt Başarılı", 
                                        f"{IDNO} - Kullanıcısı Kaydedilmiştir.")
            
        except Exception as hata:
            QMessageBox.critical(self, "HATA", f"Bir Hata Oluştu \n {hata}")
                
    def baglanti(self):
        with sqlite3.connect("./kullanici.db") as baglan:
            komut = baglan.cursor()
            komut.execute(""" create table if not exists tbl_uyeler
                        (ID TEXT, eposta TEXT, 
                        username TEXT, password TEXT, rol TEXT) """)
            return baglan
    
    
    def giris(self):
        self.baglanti()