# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_size.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_set_size(object):
    def setupUi(self, set_size):
        if not set_size.objectName():
            set_size.setObjectName(u"set_size")
        set_size.resize(459, 414)
        self.buttonBox = QDialogButtonBox(set_size)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(140, 360, 181, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(set_size)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 19, 441, 321))
        self.lengt_inp = QLineEdit(self.groupBox)
        self.lengt_inp.setObjectName(u"lengt_inp")
        self.lengt_inp.setGeometry(QRect(70, 90, 301, 32))
        self.heigh_inp = QLineEdit(self.groupBox)
        self.heigh_inp.setObjectName(u"heigh_inp")
        self.heigh_inp.setGeometry(QRect(70, 170, 301, 32))
        self.length = QLabel(self.groupBox)
        self.length.setObjectName(u"length")
        self.length.setGeometry(QRect(210, 70, 31, 20))
        self.height = QLabel(self.groupBox)
        self.height.setObjectName(u"height")
        self.height.setGeometry(QRect(200, 150, 41, 20))

        self.retranslateUi(set_size)
        self.buttonBox.accepted.connect(set_size.accept)
        self.buttonBox.rejected.connect(set_size.reject)

        QMetaObject.connectSlotsByName(set_size)
    # setupUi

    def retranslateUi(self, set_size):
        set_size.setWindowTitle(QCoreApplication.translate("set_size", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("set_size", u"\u0627\u0646\u062f\u0627\u0632\u0647 \u0647\u0627", None))
        self.length.setText(QCoreApplication.translate("set_size", u"\u0637\u0648\u0644", None))
        self.height.setText(QCoreApplication.translate("set_size", u"\u0627\u0631\u062a\u0641\u0627\u0639", None))
    # retranslateUi

