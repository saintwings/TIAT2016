########################################################
#
#	STANDARD IMPORTS
#

from PyQt4 import QtCore, QtGui
from CameraSetting_UI import Ui_MainWindow
from configobj import ConfigObj
import sys

########################################################
#
#	Standard globals
#

DEFAULT_VIDEO_DEV = "/dev/video0"
DEFAULT_COLOR_CONFIG_FILENAME = "colorfile.ini"


class CameraSettingMainWindow(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self, parent=None):
        super(CameraSettingMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.colorName = ["black","blue","brown","cyan","gray","green",
                                              "magenta","orange","pink","red","white","yellow",
                                              "color1","color2","color3","color4","color5"]

        self.configObj = ConfigObj(DEFAULT_COLOR_CONFIG_FILENAME)
        self.configObj['CameraParameters'] = {}







if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = CameraSettingMainWindow()


    MainWindow.show()
    sys.exit(app.exec_())