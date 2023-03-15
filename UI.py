# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 587)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.URL_Line_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.URL_Line_Edit.setGeometry(QtCore.QRect(100, 10, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.URL_Line_Edit.setFont(font)
        self.URL_Line_Edit.setObjectName("URL_Line_Edit")
        self.URL_Label = QtWidgets.QLabel(self.centralwidget)
        self.URL_Label.setGeometry(QtCore.QRect(5, 10, 91, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.URL_Label.setFont(font)
        self.URL_Label.setObjectName("URL_Label")
        self.URL_Submit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.URL_Submit_Button.setGeometry(QtCore.QRect(700, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.URL_Submit_Button.setFont(font)
        self.URL_Submit_Button.setObjectName("URL_Submit_Button")
        self.URL_Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.URL_Clear_Button.setGeometry(QtCore.QRect(610, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.URL_Clear_Button.setFont(font)
        self.URL_Clear_Button.setObjectName("URL_Clear_Button")
        self.Search_Progress_Bar = QtWidgets.QProgressBar(self.centralwidget)
        self.Search_Progress_Bar.setGeometry(QtCore.QRect(610, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Search_Progress_Bar.setFont(font)
        self.Search_Progress_Bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Search_Progress_Bar.setProperty("value", 0)
        self.Search_Progress_Bar.setObjectName("Search_Progress_Bar")
        self.Alert_Summary_Label = QtWidgets.QLabel(self.centralwidget)
        self.Alert_Summary_Label.setEnabled(True)
        self.Alert_Summary_Label.setGeometry(QtCore.QRect(610, 160, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Alert_Summary_Label.setFont(font)
        self.Alert_Summary_Label.setObjectName("Alert_Summary_Label")
        self.High_Alert_Label = QtWidgets.QLabel(self.centralwidget)
        self.High_Alert_Label.setGeometry(QtCore.QRect(610, 210, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.High_Alert_Label.setFont(font)
        self.High_Alert_Label.setObjectName("High_Alert_Label")
        self.Medium_Alert_Label = QtWidgets.QLabel(self.centralwidget)
        self.Medium_Alert_Label.setGeometry(QtCore.QRect(610, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Medium_Alert_Label.setFont(font)
        self.Medium_Alert_Label.setObjectName("Medium_Alert_Label")
        self.Low_Alert_Label = QtWidgets.QLabel(self.centralwidget)
        self.Low_Alert_Label.setGeometry(QtCore.QRect(610, 290, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Low_Alert_Label.setFont(font)
        self.Low_Alert_Label.setObjectName("Low_Alert_Label")
        self.Info_Alert_Label = QtWidgets.QLabel(self.centralwidget)
        self.Info_Alert_Label.setGeometry(QtCore.QRect(610, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.Info_Alert_Label.setFont(font)
        self.Info_Alert_Label.setObjectName("Info_Alert_Label")
        self.High_Alert_Number = QtWidgets.QLabel(self.centralwidget)
        self.High_Alert_Number.setGeometry(QtCore.QRect(740, 210, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.High_Alert_Number.setFont(font)
        self.High_Alert_Number.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.High_Alert_Number.setObjectName("High_Alert_Number")
        self.Medium_Alert_Number = QtWidgets.QLabel(self.centralwidget)
        self.Medium_Alert_Number.setGeometry(QtCore.QRect(740, 250, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Medium_Alert_Number.setFont(font)
        self.Medium_Alert_Number.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Medium_Alert_Number.setObjectName("Medium_Alert_Number")
        self.Info_Alert_Number = QtWidgets.QLabel(self.centralwidget)
        self.Info_Alert_Number.setGeometry(QtCore.QRect(740, 330, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Info_Alert_Number.setFont(font)
        self.Info_Alert_Number.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Info_Alert_Number.setObjectName("Info_Alert_Number")
        self.Low_Alert_Number = QtWidgets.QLabel(self.centralwidget)
        self.Low_Alert_Number.setGeometry(QtCore.QRect(740, 290, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Low_Alert_Number.setFont(font)
        self.Low_Alert_Number.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Low_Alert_Number.setObjectName("Low_Alert_Number")
        self.Delete_All_Alert_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_All_Alert_Button.setGeometry(QtCore.QRect(700, 380, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Delete_All_Alert_Button.setFont(font)
        self.Delete_All_Alert_Button.setObjectName("Delete_All_Alert_Button")
        self.Report_Alert_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Report_Alert_Button.setGeometry(QtCore.QRect(610, 380, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.Report_Alert_Button.setFont(font)
        self.Report_Alert_Button.setAutoFillBackground(False)
        self.Report_Alert_Button.setObjectName("Report_Alert_Button")
        self.Report_Text = QtWidgets.QTextEdit(self.centralwidget)
        self.Report_Text.setGeometry(QtCore.QRect(10, 50, 591, 371))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Report_Text.setFont(font)
        self.Report_Text.setObjectName("Report_Text")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(610, 140, 171, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OWASP_ZAP_Controller"))
        self.URL_Label.setText(_translate("MainWindow", "Target URL"))
        self.URL_Submit_Button.setText(_translate("MainWindow", "Scan"))
        self.URL_Clear_Button.setText(_translate("MainWindow", "Clear"))
        self.Alert_Summary_Label.setText(_translate("MainWindow", "Alerts  Summary"))
        self.High_Alert_Label.setText(_translate("MainWindow", "High"))
        self.Medium_Alert_Label.setText(_translate("MainWindow", "Medium"))
        self.Low_Alert_Label.setText(_translate("MainWindow", "Low"))
        self.Info_Alert_Label.setText(_translate("MainWindow", "Informational"))
        self.High_Alert_Number.setText(_translate("MainWindow", "0"))
        self.Medium_Alert_Number.setText(_translate("MainWindow", "0"))
        self.Info_Alert_Number.setText(_translate("MainWindow", "0"))
        self.Low_Alert_Number.setText(_translate("MainWindow", "0"))
        self.Delete_All_Alert_Button.setText(_translate("MainWindow", "Delete"))
        self.Report_Alert_Button.setText(_translate("MainWindow", "Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
