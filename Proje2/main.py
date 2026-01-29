from PyQt6.QtWidgets import QApplication
from _foto import Form_Anasayfa

uygulama = QApplication([])
baslangic_penceresi = Form_Anasayfa()
baslangic_penceresi.show()
uygulama.exec()