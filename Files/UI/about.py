# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 99)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.discription = QtWidgets.QLabel(Dialog)
        self.discription.setGeometry(QtCore.QRect(75, 10, 150, 30))
        self.discription.setAlignment(QtCore.Qt.AlignCenter)
        self.discription.setObjectName("discription")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 267, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_github = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_github.setObjectName("btn_github")
        self.horizontalLayout.addWidget(self.btn_github)
        self.btn_instagram = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_instagram.setObjectName("btn_instagram")
        self.horizontalLayout.addWidget(self.btn_instagram)
        self.btn_telegram = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_telegram.setObjectName("btn_telegram")
        self.horizontalLayout.addWidget(self.btn_telegram)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About us"))
        self.discription.setText(_translate("Dialog", "This program made by Sina.f"))
        self.btn_github.setText(_translate("Dialog", "GitHub"))
        self.btn_instagram.setText(_translate("Dialog", "Instagram"))
        self.btn_telegram.setText(_translate("Dialog", "Telegram"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
