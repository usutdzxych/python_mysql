"""
@author:兵慌码乱
@project_name:python图书管理系统
@time:2021/06/01 17:51
@remarks:登录界面设计模块
"""
from PyQt5 import QtCore, QtGui, QtWidgets


# 登录界面设计
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setWindowModality(QtCore.Qt.ApplicationModal)
        Login.resize(652, 385)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(300, 20, 111, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.user = QtWidgets.QLabel(Login)
        self.user.setGeometry(QtCore.QRect(150, 90, 60, 41))
        self.user.setObjectName("user")
        self.password = QtWidgets.QLabel(Login)
        self.password.setGeometry(QtCore.QRect(160, 150, 60, 26))
        self.password.setObjectName("password")
        self.identify = QtWidgets.QLabel(Login)
        self.identify.setGeometry(QtCore.QRect(140, 180, 91, 59))
        self.identify.setObjectName("identify")
        self.userline = QtWidgets.QLineEdit(Login)
        self.userline.setGeometry(QtCore.QRect(290, 100, 191, 21))
        self.userline.setObjectName("userline")
        self.pwline = QtWidgets.QLineEdit(Login)
        self.pwline.setGeometry(QtCore.QRect(290, 150, 191, 21))
        self.pwline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwline.setObjectName("pwline")
        self.idbox = QtWidgets.QComboBox(Login)
        self.idbox.setGeometry(QtCore.QRect(320, 200, 121, 22))
        self.idbox.setObjectName("idbox")
        self.idbox.addItem("")
        self.idbox.addItem("")
        self.idbox.addItem("")
        self.loginbt = QtWidgets.QPushButton(Login)
        self.loginbt.setGeometry(QtCore.QRect(250, 270, 93, 28))
        self.loginbt.setObjectName("loginbt")
        self.exitbt = QtWidgets.QPushButton(Login)
        self.exitbt.setGeometry(QtCore.QRect(420, 270, 93, 28))
        self.exitbt.setObjectName("exitbt")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate #
        Login.setWindowTitle(_translate("Login", "Python图书馆管理系统"))
        self.label.setText(
            _translate("Login", "<html><head/><body><p><span style=\" font-size:16pt;\">用户登录</span></p></body></html>"))
        self.user.setText(
            _translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">用户id</span></p></body></html>"))
        self.password.setText(
            _translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">密码</span></p></body></html>"))
        self.identify.setText(
            _translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">身份类型</span></p></body></html>"))
        self.idbox.setItemText(0, _translate("Login", "读者"))
        self.idbox.setItemText(1, _translate("Login", "图书管理员"))
        self.idbox.setItemText(2, _translate("Login", "系统管理员"))
        self.loginbt.setText(_translate("Login", "登录"))
        self.exitbt.setText(_translate("Login", "退出"))
