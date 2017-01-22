from PyQt5 import QtWidgetsfrom src.controller.camera import Camerafrom src.ui.commons.layout import set_hboxclass ContinuousShooterWindow(QtWidgets.QMainWindow):    def __init__(self, parent=None):        super(ContinuousShooterWindow, self).__init__(parent)        self.cam = Camera()        self.button_start_shoot = QPushButton("Start", self)        self.button_stop_shoot = QPushButton("Stop", self)        self.button_start_shoot.clicked.connect(self.cam.start_taking_photo)        self.button_stop_shoot.clicked.connect(self.cam.stop_taking_photo)        l = set_hbox(self.button_start_shoot, self.button_stop_shoot)        self.setLayout(l)