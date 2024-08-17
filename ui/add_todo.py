# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_todo.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QTextEdit, QWidget)

class Ui_AddTodo(object):
    def setupUi(self, AddTodo):
        if not AddTodo.objectName():
            AddTodo.setObjectName(u"AddTodo")
        AddTodo.resize(543, 418)
        self.ok_cancel_btn = QDialogButtonBox(AddTodo)
        self.ok_cancel_btn.setObjectName(u"ok_cancel_btn")
        self.ok_cancel_btn.setGeometry(QRect(350, 360, 181, 51))
        self.ok_cancel_btn.setOrientation(Qt.Horizontal)
        self.ok_cancel_btn.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(AddTodo)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 521, 331))
        self.add_name_inp = QLineEdit(self.groupBox)
        self.add_name_inp.setObjectName(u"add_name_inp")
        self.add_name_inp.setGeometry(QRect(20, 60, 251, 32))
        self.add_description_inp = QTextEdit(self.groupBox)
        self.add_description_inp.setObjectName(u"add_description_inp")
        self.add_description_inp.setGeometry(QRect(10, 150, 491, 141))
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(380, 60, 71, 31))
        self.name_lbl = QLabel(self.groupBox)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setGeometry(QRect(20, 40, 41, 16))
        self.description_lbl = QLabel(self.groupBox)
        self.description_lbl.setObjectName(u"description_lbl")
        self.description_lbl.setGeometry(QRect(10, 130, 71, 18))

        self.retranslateUi(AddTodo)
        self.ok_cancel_btn.accepted.connect(AddTodo.accept)
        self.ok_cancel_btn.rejected.connect(AddTodo.reject)

        QMetaObject.connectSlotsByName(AddTodo)
    # setupUi

    def retranslateUi(self, AddTodo):
        AddTodo.setWindowTitle(QCoreApplication.translate("AddTodo", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddTodo", u"Add Todo", None))
        self.checkBox.setText(QCoreApplication.translate("AddTodo", u"Status", None))
        self.name_lbl.setText(QCoreApplication.translate("AddTodo", u"Name", None))
        self.description_lbl.setText(QCoreApplication.translate("AddTodo", u"Description", None))
    # retranslateUi

