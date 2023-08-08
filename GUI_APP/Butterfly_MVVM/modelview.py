import numpy as np
import cv2
from PyQt5.QtWidgets import (QMainWindow, 
                             QFileDialog,
                             )

from PyQt5.QtGui     import QIcon, QPixmap
from butterfly_application_ui import Ui_MainWindow
from model import  ButterflySpecies, load_model
from recource_utils import resource_path, os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Nav.setChecked(True)
        self.setWindowTitle("Identification of polish butterflies")
        self.ui.Load.clicked.connect(self.load_an_butterfly_image)
        self._flag = 0
        self.ui.Predict.setEnabled(False)
        self.ui.Predict.clicked.connect(self.predict_an_butterfly)
        self.ui.Load.setToolTip("Click to load an butterfly image")
        self.ui.Reset.setToolTip("Click to restore the initial state")
        self.ui.Predict.setToolTip("Click to Predict a butterfly\nWARRING! the button will be available after the image is loaded")
        
    # functions for changing pages
    def on_Nav_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Model_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_About_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_Tech_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def on_Links_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    # load an image
   
            
    def load_an_butterfly_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Choose a picture of a butterfly from the available species',
            '',
            'Image files (*.jpg *.jpeg *.png *.bmp)')

        
        if file_path:
            pixmap = QPixmap(resource_path(file_path))
            self.ui.label_4.setPixmap(pixmap)
            self._flag=1
            self.ui.Predict.setEnabled(True)
            image = cv2.imread(file_path,cv2.IMREAD_COLOR)
            cv2.imwrite(resource_path("images\\temp.png"), image)
             
    
    def on_Reset_clicked(self):
        self._flag = 0
        self.ui.Predict.setEnabled(False)
        pixmap = QPixmap(resource_path("images\\butterflies.png"))
        self.ui.label_4.setPixmap(pixmap)
        if os.path.exists(resource_path("images\\temp.png")):
            os.remove(resource_path("images\\temp.png"))
        self.ui.Prediction_label.setText("")
        self.ui.Aglais_bar.setValue(0)
        self.ui.Argynnis_bar.setValue(0)
        self.ui.Nymphalis_bar.setValue(0)
        self.ui.Papilio_bar.setValue(0)
        self.ui.Vanessa_bar.setValue(0)
        
    def predict_an_butterfly(self):
        
        
        cnn = load_model()
        if self._flag == 1:
            
            image = cv2.imread(resource_path("images\\temp.png"), cv2.IMREAD_COLOR)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            array = cv2.resize(image, (110, 110))
            array = array / 255.0 #normalization
            array_prediction =  np.round(cnn.predict(array.reshape((1,) + array.shape),verbose = 0),2)
            self.ui.Aglais_bar.setValue(int(array_prediction[0][0]*100))
            self.ui.Argynnis_bar.setValue(int(array_prediction[0][1]*100))
            self.ui.Nymphalis_bar.setValue(int(array_prediction[0][2]*100))
            self.ui.Papilio_bar.setValue(int(array_prediction[0][3]*100))
            self.ui.Vanessa_bar.setValue(int(array_prediction[0][4]*100))
        

            index = np.argmax(array_prediction)
            if index == 0:
                self.ui.Prediction_label.setText(f"Most likely in the picture is {ButterflySpecies.Peacock_butterfly.value}")
            elif index == 1:
                self.ui.Prediction_label.setText(f"Most likely in the picture is {ButterflySpecies.Silver_washed_fritillary.value}")
            elif index == 2:
                self.ui.Prediction_label.setText(f"Most likely in the picture is {ButterflySpecies.Mourning_cloak.value}")
            elif index == 3:
                self.ui.Prediction_label.setText(f"Most likely in the picture is {ButterflySpecies.Swallowtail_butterfly.value}")
            else:
                self.ui.Prediction_label.setText(f"Most likely in the picture is {ButterflySpecies.Red_admiral.value}")

        