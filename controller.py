from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal

from UI import Ui_MainWindow

from zapv2 import ZAPv2

import time
#pyuic5 -x pyqt.ui -o UI.py

URL = ""

#http://example.com
apikey = 'changeme'

zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8180', 'https': 'http://127.0.0.1:8180'})

zap.core.delete_all_alerts()

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Setup_Control()

    def Setup_Control(self):
        self.ui.URL_Line_Edit.setText("http://example.com")
        self.ui.URL_Submit_Button.clicked.connect(self.URL_Submit)
        self.ui.URL_Clear_Button.clicked.connect(self.URL_Clear)
        self.ui.Delete_All_Alert_Button.clicked.connect(self.Alter_Delete)
        self.ui.Report_Alert_Button.clicked.connect(self.Alter_Report)

    def URL_Submit(self):
        global URL
        URL = self.ui.URL_Line_Edit.text()
            
        self.Search_Work = WorkerThread()
        self.Search_Work.start()

    def URL_Clear(self):
        self.ui.URL_Line_Edit.setText("")
        self.ui.Search_Progress_Bar.setValue(0)      

    def Alter_Delete(self):
        zap.core.delete_all_alerts()

        self.ui.High_Alert_Number.setText("0")
        self.ui.Medium_Alert_Number.setText("0")
        self.ui.Low_Alert_Number.setText("0")
        self.ui.Info_Alert_Number.setText("0")
        self.ui.show.clear()

    def Alter_Report(self):
        reportPath = QFileDialog.getSaveFileName(self, "選擇保存路徑", "./Alert_Report.txt", "Text Files (*.txt)")
        reportFile = open(reportPath[0], "w") #"a"

        allAlert = zap.core.alerts()
        a = 1
        for alert in allAlert:
            reportFile.write("{}\n".format(a))
            reportFile.write("cweid : {}\n".format(alert.get("cweid")))
            reportFile.write("confidence : {}\n".format(alert.get("confidence")))
            reportFile.write("wascid : {}\n".format(alert.get("wascid")))
            reportFile.write("description : {}\n".format(alert.get("description")))
            reportFile.write("alert : {}\n".format(alert.get("alert")))
            reportFile.write("risk : {}\n".format(alert.get("risk")))
            reportFile.write("--------------------\n")
            a += 1   
        reportFile.close()

        reportText = open(reportPath[0]).read()
        self.ui.show.setText(reportText) 
class WorkerThread(QThread):
    progressChanged = QtCore.pyqtSignal(int)
    highAlertNumber = QtCore.pyqtSignal(str)
    mediumAlertNumber = QtCore.pyqtSignal(str)
    lowAlertNumber = QtCore.pyqtSignal(str)
    infoAlertNumber = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.progressChanged.connect(window.ui.Search_Progress_Bar.setValue)
        self.highAlertNumber.connect(window.ui.High_Alert_Number.setText)
        self.mediumAlertNumber.connect(window.ui.Medium_Alert_Number.setText)
        self.lowAlertNumber.connect(window.ui.Low_Alert_Number.setText)
        self.infoAlertNumber.connect(window.ui.Info_Alert_Number.setText)

    def run(self):
        zap.urlopen(URL)
        zap.spider.scan(URL)
        scanid = zap.ascan.scan(URL)

        #reference : https://www.iamdu.com/archives/11253 
        while (int(zap.ascan.status(scanid)) < 100):
            self.progressChanged.emit(int(zap.ascan.status(scanid)))
            time.sleep(1.0)
        self.progressChanged.emit(100)

        summary =  zap.core.alerts_summary()
        self.highAlertNumber.emit(str(summary.get("High")))
        self.mediumAlertNumber.emit(str(summary.get("Medium")))
        self.lowAlertNumber.emit(str(summary.get("Low")))
        self.infoAlertNumber.emit(str(summary.get("Informational")))
    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())


# TODO list 
# V UI show alert summary
# V detail alert report to text file
# V     >> select create/report file path
#       >> check alert exist
#       >> setting default file path
# V show alert report
# X search CWE & WASC website
# X OWASP ZAP setting tutorial(or in GitHub README)
# X setting ZAP apikey & proxy port

### coding style : UI item/function 開頭大寫 用_分隔 _後大寫
###                controller       開頭小寫 不分隔 第二字後開頭大寫
