from PyQt6.QtWidgets import *
from kamera import Ui_Kamera_Formu

import cv2
from PyQt6.QtGui import QImage, QPixmap

class Kamera_Formu(QMainWindow):
    def __init__(self):
        super().__init__()
        ## giris formu için g2 değişkenini tanımladık
        self.cam = Ui_Kamera_Formu()
        self.cam.setupUi(self)

        ## Fotoğraf ID tanımlama İşlemi 
        self.logic, self.value = 0 , 1
        
        
        self.cam.btn_fotoCekimi.clicked.connect(self.fotoCekimi)
        self.cam.btn_open.clicked.connect(self.kamerayiAc)
    
    def kamerayiAc(self):
        kamera = cv2.VideoCapture(0)
        while kamera.isOpened():
            roi, frame = kamera.read()
            if roi == True:
                self.displayImage(frame, 1)
                cv2.waitKey()
                
                if self.logic == 2:
                    self.value += 1
                    cv2.imwrite(f"./photos/{self.value}.png", frame)
                    self.logic = 1
                    QMessageBox.information(self, "Foto Kayıt", "Fotoğraf Kaydedildi")
                    
            else:
                QMessageBox.warning(self, "Foto Uyarı", "Fotoğraf Çekilemedi")
        kamera.release()
        cv2.destroyAllWindows()
    
    def fotoCekimi(self):
        self.logic = 2
    
    def displayImage(self, img, window=1):
        qFormat = QImage.Format.Format_Indexed8
        if (len(img.shape) == 3):
            if (img.shape[2] == 4):
                qFormat = QImage.Format.Format_RGBA8888
            else:
                qFormat = QImage.Format.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qFormat)
        img = img.rgbSwapped()
        self.cam.label_image.setPixmap(QPixmap.fromImage(img))
        
    