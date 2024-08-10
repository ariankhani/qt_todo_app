# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_todo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(818, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 791, 371))
        self.Todo_list = QTableWidget(self.groupBox)
        if (self.Todo_list.columnCount() < 4):
            self.Todo_list.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.Todo_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Todo_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Todo_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Todo_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.Todo_list.setObjectName(u"Todo_list")
        self.Todo_list.setGeometry(QRect(10, 30, 771, 331))
        self.Todo_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Todo_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Todo_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Todo_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Todo_list.setWordWrap(True)
        self.Todo_list.setRowCount(0)
        self.Todo_list.setColumnCount(4)
        self.Todo_list.horizontalHeader().setVisible(True)
        self.Todo_list.horizontalHeader().setDefaultSectionSize(100)
        self.Todo_list.horizontalHeader().setHighlightSections(True)
        self.Todo_list.horizontalHeader().setStretchLastSection(True)
        self.Todo_list.verticalHeader().setVisible(False)
        self.add_todo_gp = QGroupBox(self.centralwidget)
        self.add_todo_gp.setObjectName(u"add_todo_gp")
        self.add_todo_gp.setGeometry(QRect(10, 380, 791, 161))
        self.Add_todo = QPushButton(self.add_todo_gp)
        self.Add_todo.setObjectName(u"Add_todo")
        self.Add_todo.setGeometry(QRect(690, 130, 89, 25))
        self.label = QLabel(self.add_todo_gp)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 67, 17))
        self.lineEdit = QLineEdit(self.add_todo_gp)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 30, 113, 25))
        self.lineEdit_2 = QLineEdit(self.add_todo_gp)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 70, 113, 25))
        self.label_2 = QLabel(self.add_todo_gp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 67, 17))
        self.lineEdit_4 = QLineEdit(self.add_todo_gp)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(310, 30, 371, 121))
        self.label_4 = QLabel(self.add_todo_gp)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(216, 30, 81, 20))
        self.label_3 = QLabel(self.add_todo_gp)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 120, 67, 17))
        self.lineEdit_3 = QLineEdit(self.add_todo_gp)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 120, 113, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 818, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"List", None))
        ___qtablewidgetitem = self.Todo_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem1 = self.Todo_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.Todo_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.Todo_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.add_todo_gp.setTitle(QCoreApplication.translate("MainWindow", u"Add new", None))
        self.Add_todo.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Staus:", None))
    # retranslateUi

