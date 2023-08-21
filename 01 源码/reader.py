"""

"""

import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from connect import *

cursor, conn = connect()  # 连接数据库


# 读者界面设计
class Ui_Reader(object):
    # 创建UI
    def setupUi(self, Reader):
        self.loginID = self.getreaderid()
        Reader.setObjectName("Reader")
        Reader.resize(719, 742)
        # readertab
        self.readertab = QtWidgets.QTabWidget(Reader)
        self.readertab.setGeometry(QtCore.QRect(11, 11, 701, 721))
        self.readertab.setObjectName("readertab")

        self.borrowbook = QtWidgets.QWidget()
        self.borrowbook.setObjectName("borrowbook") # 窗口换名字

        self.layoutWidget = QtWidgets.QWidget(self.borrowbook)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 10, 671, 671))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")

        #水平方向加窗口
        self.horizontalLayout.addWidget(self.label)

        self.borrowbookid = QtWidgets.QLineEdit(self.layoutWidget)
        self.borrowbookid.setObjectName("borrowbookid")

        self.horizontalLayout.addWidget(self.borrowbookid)
        self.borrowcheckbt = QtWidgets.QPushButton(self.layoutWidget)
        self.borrowcheckbt.setObjectName("borrowcheckbt")
        self.horizontalLayout.addWidget(self.borrowcheckbt)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.borrowtable = QtWidgets.QTableWidget(self.layoutWidget)
        self.borrowtable.setMouseTracking(False)
        self.borrowtable.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.borrowtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.borrowtable.setObjectName("borrowtable")
        self.borrowtable.setColumnCount(5)
        self.borrowtable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.borrowtable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.borrowokbt = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.borrowokbt.sizePolicy().hasHeightForWidth())

        self.borrowokbt.setSizePolicy(sizePolicy)
        self.borrowokbt.setObjectName("borrowokbt")
        self.horizontalLayout_2.addWidget(self.borrowokbt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.readertab.addTab(self.borrowbook, "")

        self.returnbook = QtWidgets.QWidget()
        self.returnbook.setObjectName("returnbook")
        self.layoutWidget1 = QtWidgets.QWidget(self.returnbook)
        self.layoutWidget1.setGeometry(QtCore.QRect(9, 9, 311, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.returnbo = QtWidgets.QLabel(self.layoutWidget1)
        self.returnbo.setObjectName("returnbo")
        self.horizontalLayout_3.addWidget(self.returnbo)
        self.returnbookid = QtWidgets.QLineEdit(self.layoutWidget1)
        self.returnbookid.setObjectName("returnbookid")
        self.horizontalLayout_3.addWidget(self.returnbookid)
        self.returnbookbt = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnbookbt.sizePolicy().hasHeightForWidth())
        self.returnbookbt.setSizePolicy(sizePolicy)
        self.returnbookbt.setObjectName("returnbookbt")
        self.horizontalLayout_3.addWidget(self.returnbookbt)
        self.readertab.addTab(self.returnbook, "")
        self.checkbook = QtWidgets.QWidget()
        self.checkbook.setObjectName("checkbook")
        self.tableWidget = QtWidgets.QTableWidget(self.checkbook)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 651, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.widget = QtWidgets.QWidget(self.checkbook)
        self.widget.setGeometry(QtCore.QRect(13, 13, 641, 162))
        self.widget.setObjectName("widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.bookid = QtWidgets.QLineEdit(self.widget)
        self.bookid.setObjectName("bookid")
        self.horizontalLayout_4.addWidget(self.bookid)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.bookname = QtWidgets.QLineEdit(self.widget)
        self.bookname.setObjectName("bookname")
        self.horizontalLayout_5.addWidget(self.bookname)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.author = QtWidgets.QLineEdit(self.widget)
        self.author.setObjectName("author")
        self.horizontalLayout_6.addWidget(self.author)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.type = QtWidgets.QLineEdit(self.widget)
        self.type.setObjectName("type")
        self.horizontalLayout_7.addWidget(self.type)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.press = QtWidgets.QLineEdit(self.widget)
        self.press.setObjectName("press")
        self.horizontalLayout_8.addWidget(self.press)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.checkbt = QtWidgets.QPushButton(self.widget)
        self.checkbt.setObjectName("checkbt")
        self.verticalLayout.addWidget(self.checkbt)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.readertab.addTab(self.checkbook, "")
        self.userinfo = QtWidgets.QWidget()
        self.userinfo.setObjectName("userinfo")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.userinfo)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.userinfo)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.userinfo)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_10.addWidget(self.lineEdit_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.userinfo)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.userinfo)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_11.addWidget(self.lineEdit_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.userinfo)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.userinfo)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_13.addWidget(self.lineEdit_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.pushButton_5 = QtWidgets.QPushButton(self.userinfo)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_14.addWidget(self.pushButton_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.userinfo)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_8.addWidget(self.textBrowser_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.readertab.addTab(self.userinfo, "")
        self.pay_2 = QtWidgets.QWidget()
        self.pay_2.setObjectName("pay_2")
        self.gridLayout = QtWidgets.QGridLayout(self.pay_2)
        self.gridLayout.setObjectName("gridLayout")
        self.money = QtWidgets.QLabel(self.pay_2)
        self.money.setText("")
        self.money.setObjectName("money")
        self.gridLayout.addWidget(self.money, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.pay_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.alipay = QtWidgets.QPushButton(self.pay_2)
        self.alipay.setObjectName("alipay")
        self.gridLayout.addWidget(self.alipay, 1, 2, 1, 1)
        self.wepay = QtWidgets.QPushButton(self.pay_2)
        self.wepay.setObjectName("wepay")
        self.gridLayout.addWidget(self.wepay, 1, 1, 1, 1)
        self.readertab.addTab(self.pay_2, "")

        self.retranslateUi(Reader)
        self.getreaderinfo()
        # self.textBrowser_2.setText(self.readerlogin
        self.readertab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Reader)
        self.borrowcheckbt.clicked.connect(self.borrowidcheck)
        self.borrowokbt.clicked.connect(self.submit)
        # 还书
        self.returnbookbt.clicked.connect(self.ReturnBook)
        # 查询所有书
        self.pushButton.clicked.connect(self.selectallbook)
        self.checkbt.clicked.connect(self.selectbook)

        # 信息修改 pushButton_5
        self.pushButton_5.clicked.connect(self.alterinfo)

        self.wepay.clicked.connect(self.paymoney)
        self.alipay.clicked.connect(self.paymoney)

    def retranslateUi(self, Reader):
        _translate = QtCore.QCoreApplication.translate

        Reader.setWindowTitle(_translate("Reader", "读者系统"))

        # 借书
        self.label.setText(_translate("Reader", "书号/书名"))
        self.borrowcheckbt.setText(_translate("Reader", "查询"))

        item = self.borrowtable.verticalHeaderItem(0)
        item.setText(_translate("Reader", "1"))
        item = self.borrowtable.horizontalHeaderItem(0)
        item.setText(_translate("Reader", "书号"))
        item = self.borrowtable.horizontalHeaderItem(1)
        item.setText(_translate("Reader", "书名"))
        item = self.borrowtable.horizontalHeaderItem(2)
        item.setText(_translate("Reader", "作者"))
        item = self.borrowtable.horizontalHeaderItem(3)
        item.setText(_translate("Reader", "出版社"))
        item = self.borrowtable.horizontalHeaderItem(4)
        item.setText(_translate("Reader", "在馆册数"))
        self.borrowokbt.setText(_translate("Reader", "确认借书"))
        # 页面表格
        self.readertab.setTabText(self.readertab.indexOf(self.borrowbook), _translate("Reader", "借书"))
        # 还书
        self.returnbo.setText(_translate("Reader", "书号"))
        self.returnbookbt.setText(_translate("Reader", "还书"))
        self.readertab.setTabText(self.readertab.indexOf(self.returnbook), _translate("Reader", "还书"))

        # 查询图书信息
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Reader", "书号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Reader", "书名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Reader", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Reader", "类别"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Reader", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Reader", "馆藏册数"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Reader", "在馆册数"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Reader", "书架号"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Reader", "被借次数"))

        self.label_3.setText(_translate("Reader", "书名"))
        self.label_4.setText(_translate("Reader", "书号"))
        self.label_5.setText(_translate("Reader", "作者"))
        self.label_6.setText(_translate("Reader", "类别"))
        self.label_7.setText(_translate("Reader", "出版社"))
        self.pushButton.setText(_translate("Reader", "查询所有"))
        self.checkbt.setText(_translate("Reader", "查询"))
        self.readertab.setTabText(self.readertab.indexOf(self.checkbook), _translate("Reader", "查询图书信息"))

        # 用户信息
        self.label_8.setText(_translate("Reader", "姓名"))
        self.label_9.setText(_translate("Reader", "性别"))
        self.label_11.setText(_translate("Reader", "密码"))
        self.pushButton_5.setText(_translate("Reader", "修改"))
        self.readertab.setTabText(self.readertab.indexOf(self.userinfo), _translate("Reader", "用户信息修改"))


        self.label_12.setText(_translate("Reader", "需支付罚款"))
        self.alipay.setText(_translate("Reader", "支付宝支付"))
        self.wepay.setText(_translate("Reader", "微信支付"))
        self.readertab.setTabText(self.readertab.indexOf(self.pay_2), _translate("Reader", "逾期罚款"))  #####

    # 01 借书信息查询
    def borrowidcheck(self):
        bookin = self.borrowbookid.text()
        sql = 'select * from books where 书号="%s" or 书名="%s"' % (bookin, bookin)
        res = cursor.execute(sql)
        bookinfo = cursor.fetchall()
        n = len(bookinfo)
        self.borrowtable.setRowCount(n)
        for i in range(n):
            book = bookinfo[i]
            bookid = QTableWidgetItem(book[0])
            bookname = QTableWidgetItem(book[1])
            bookauthor = QTableWidgetItem(book[2])
            bookpress = QTableWidgetItem(book[5])
            booknumber = QTableWidgetItem(str(book[8]))
            self.borrowtable.setItem(i, 0, bookid)
            self.borrowtable.setItem(i, 1, bookname)
            self.borrowtable.setItem(i, 2, bookauthor)
            self.borrowtable.setItem(i, 3, bookpress)
            self.borrowtable.setItem(i, 4, booknumber)

    # 02 获取当前读者ID
    def getreaderid(self):
        nowtime = time.strftime("%Y-%m-%d", time.localtime())
        sql = 'SELECT * FROM loginrecord where time = "%s" order by number' % nowtime
        cursor.execute(sql)
        todaylogin = cursor.fetchall()
        readerlogin = todaylogin[-1]
        ID = readerlogin[0]
        print(ID)
        return ID

    # 03 获取读者信息
    def getreaderinfo(self):
        sql = 'SELECT * FROM readers where ID="%s"' % (self.loginID)
        cursor.execute(sql)
        readerlogined = cursor.fetchall()
        readerlogined = readerlogined[0]
        text = '读者ID：%s\n姓名：%s\n性别：%s\n单位：%s\n读者类型：%s\n可借册数：%d\n在借册数：%d\n密码：%s\n欠款：%.2f' % readerlogined
        self.textBrowser_2.setText(text)
        money = str(readerlogined[-1]) + '元'
        self.money.setText(money)

    # 04 提交借书申请
    def submit(self):
        s = self.borrowtable.currentRow()
        if s == -1:
            QMessageBox.warning(self, "警告", "请点击想借阅的书！", QMessageBox.Yes)
        else:
            remain = int(self.borrowtable.item(s, 4).text())
            if remain == 0:
                QMessageBox.warning(self, "警告", "这本书已经借光啦！", QMessageBox.Yes)
            else:
                t = self.borrowtable.item(s, 0).text()
                sql = 'SELECT * FROM item where ID="%s" and bookid="%s" and type="borrow"' % (self.loginID, t)
                res = cursor.execute(sql)
                if res:
                    QMessageBox.warning(self, "警告", "请勿重复提交！", QMessageBox.Yes)
                else:
                    nowtime = time.strftime("%Y-%m-%d", time.localtime())
                    sql = 'INSERT INTO item(bookid,ID,time,type) VALUES ("%s","%s","%s","borrow")' % (t, self.loginID, nowtime)
                    cursor.execute(sql)
                    conn.commit()
                    QMessageBox.warning(self, "提示", "提交成功！", QMessageBox.Yes)

    # 05 提交还书申请
    def ReturnBook(self):
        bookid = self.returnbookid.text()
        sql = 'SELECT * FROM books where 书号="%s"' % (bookid)
        res = cursor.execute(sql)
        if res:
            sql = 'SELECT * from borrow where 书号="%s" and ID="%s"' % (bookid, self.loginID)
            res = cursor.execute(sql)
            borrowinfo = cursor.fetchall()
            if res:
                nowtime = time.strftime("%Y-%m-%d", time.localtime())
                sql = 'SELECT * FROM item where ID="%s" and time="%s" and type= "return" and bookid="%s"' % (
                    self.loginID, nowtime, bookid)
                res = cursor.execute(sql)
                if res:
                    QMessageBox.warning(self, "警告", "请勿重复提交！", QMessageBox.Yes)
                else:
                    sql = 'INSERT INTO item(bookid,ID,time,type) VALUES ("%s","%s","%s","return")' % (
                        bookid, self.loginID, nowtime)
                    cursor.execute(sql)
                    conn.commit()
                    QMessageBox.warning(self, "提示", "提交成功！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "您未借过这本书！", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "书号输入错误！请重新输入！", QMessageBox.Yes)

    # 05 查询所有书籍
    def selectallbook(self):
        sql = 'SELECT * FROM books'
        cursor.execute(sql)
        books = cursor.fetchall()
        booknumber = len(books)
        self.tableWidget.setRowCount(booknumber)
        for i in range(booknumber):
            book = books[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(book[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(book[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(book[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(book[3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(book[5]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(book[7])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(book[8])))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(book[9]))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(str(book[10])))

    # 06 条件查询书籍
    def selectbook(self):
        bookname = self.bookid.text()
        bookid = self.bookname.text()
        bookauthor = self.author.text()
        booktype = self.type.text()
        bookpress = self.press.text()
        an = 0
        if bookname:
            bookname = ' 书名="%s"' % (bookname)
            an = 1
        if bookid:
            if an == 1:
                bookid = ' and 书号="%s"' % (bookid)
            else:
                bookid = ' 书号="%s"' % (bookid)
                an = 1
        if bookauthor:
            if an == 1:
                bookauthor = 'and 作者="%s"' % (bookauthor)
            else:
                bookauthor = '作者="%s"' % (bookauthor)
                an = 1
        if booktype:
            if an == 1:
                booktype = ' and 类型="%s"' % (booktype)
            else:
                booktype = ' 类型="%s"' % (booktype)
                an = 1
        if bookpress:
            if an == 1:
                bookpress = ' and 出版社="%s"' % (bookpress)
            else:
                bookpress = ' 出版社="%s"' % (bookpress)
        sql1 = 'SELECT * FROM books where'
        sql = sql1 + bookname + bookid + bookauthor + booktype + bookpress
        res = cursor.execute(sql)
        books = cursor.fetchall()
        if res:
            booknumber = len(books)
            self.tableWidget.setRowCount(booknumber)
            for i in range(booknumber):
                book = books[i]
                self.tableWidget.setItem(i, 0, QTableWidgetItem(book[0]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(book[1]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(book[2]))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(book[3]))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(book[5]))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(str(book[7])))
                self.tableWidget.setItem(i, 6, QTableWidgetItem(str(book[8])))
                self.tableWidget.setItem(i, 7, QTableWidgetItem(book[9]))
                self.tableWidget.setItem(i, 8, QTableWidgetItem(str(book[10])))
        else:
            QMessageBox.warning(self, "警告", "没有符合条件的书！", QMessageBox.Yes)

    # 07 读者修改自己的信息
    def alterinfo(self):
        name = self.lineEdit_8.text()
        sex = self.lineEdit_9.text()
        password = self.lineEdit_11.text()
        if name:
            sql = 'UPDATE readers SET 姓名="%s" WHERE ID="%s"' % (name, self.loginID)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        if sex == '男' or sex == '女':
            sql = 'UPDATE readers SET 性别="%s" WHERE ID="%s"' % (sex, self.loginID)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        elif sex != '':
            QMessageBox.warning(self, "警告", "性别输入错误，请输入男/女！", QMessageBox.Yes)
        if password:
            sql = 'UPDATE readers SET password="%s" WHERE ID="%s"' % (password, self.loginID)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        self.getreaderinfo()

    # 08 支付欠款（链接支付接口）
    def paymoney(self):
        money = 0.00
        sql = 'UPDATE readers SET 欠款="%f" WHERE ID="%s"' % (money, self.loginID)
        cursor.execute(sql)
        conn.commit()
        self.getreaderinfo()
