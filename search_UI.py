# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search_Window(object):
    def setupUi(self, Search_Window):
        Search_Window.setObjectName("Search_Window")
        Search_Window.resize(530, 474)
        self.ID_Label = QtWidgets.QLabel(Search_Window)
        self.ID_Label.setGeometry(QtCore.QRect(10, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.ID_Label.setFont(font)
        self.ID_Label.setObjectName("ID_Label")
        self.ID_Serach_Line_Edit = QtWidgets.QLineEdit(Search_Window)
        self.ID_Serach_Line_Edit.setGeometry(QtCore.QRect(40, 10, 151, 41))
        self.ID_Serach_Line_Edit.setObjectName("ID_Serach_Line_Edit")
        self.Serach_Button = QtWidgets.QPushButton(Search_Window)
        self.Serach_Button.setGeometry(QtCore.QRect(200, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.Serach_Button.setFont(font)
        self.Serach_Button.setObjectName("Serach_Button")
        self.CWE_Radio_Button = QtWidgets.QRadioButton(Search_Window)
        self.CWE_Radio_Button.setGeometry(QtCore.QRect(300, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.CWE_Radio_Button.setFont(font)
        self.CWE_Radio_Button.setChecked(True)
        self.CWE_Radio_Button.setObjectName("CWE_Radio_Button")
        self.WASC_Radio_Button = QtWidgets.QRadioButton(Search_Window)
        self.WASC_Radio_Button.setGeometry(QtCore.QRect(370, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.WASC_Radio_Button.setFont(font)
        self.WASC_Radio_Button.setObjectName("WASC_Radio_Button")
        self.Name_Label = QtWidgets.QLabel(Search_Window)
        self.Name_Label.setGeometry(QtCore.QRect(10, 70, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.Name_Label.setFont(font)
        self.Name_Label.setObjectName("Name_Label")
        self.Discription_Label = QtWidgets.QLabel(Search_Window)
        self.Discription_Label.setGeometry(QtCore.QRect(10, 110, 501, 121))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.Discription_Label.setFont(font)
        self.Discription_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Discription_Label.setObjectName("Discription_Label")
        self.CVE_Label = QtWidgets.QLabel(Search_Window)
        self.CVE_Label.setGeometry(QtCore.QRect(10, 230, 511, 241))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.CVE_Label.setFont(font)
        self.CVE_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.CVE_Label.setObjectName("CVE_Label")

        self.retranslateUi(Search_Window)
        QtCore.QMetaObject.connectSlotsByName(Search_Window)

    def retranslateUi(self, Search_Window):
        _translate = QtCore.QCoreApplication.translate
        Search_Window.setWindowTitle(_translate("Search_Window", "ID_Search"))
        self.ID_Label.setText(_translate("Search_Window", "ID"))
        self.Serach_Button.setText(_translate("Search_Window", "Search"))
        self.CWE_Radio_Button.setText(_translate("Search_Window", "CWE"))
        self.WASC_Radio_Button.setText(_translate("Search_Window", "WASC"))
        self.Name_Label.setText(_translate("Search_Window", "Name : "))
        self.Discription_Label.setText(_translate("Search_Window", "Discription : "))
        self.CVE_Label.setText(_translate("Search_Window", "CVE : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search_Window = QtWidgets.QWidget()
    ui = Ui_Search_Window()
    ui.setupUi(Search_Window)
    Search_Window.show()
    sys.exit(app.exec_())
