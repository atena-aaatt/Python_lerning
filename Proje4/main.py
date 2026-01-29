from PyQt6.QtWidgets import QApplication
from _giris import Giris_Formu
from _kamera import Kamera_Formu
uygulama = QApplication([])
pencere = Kamera_Formu()
pencere.show()
uygulama.exec()