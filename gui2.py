# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setObjectName("comboBox3")
        # self.comboBox3.addItem("")
        # self.comboBox3.addItem("")
        # self.comboBox3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox3)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.comboBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox4.setObjectName("comboBox4")
        # self.comboBox4.addItem("")
        # self.comboBox4.addItem("")
        # self.comboBox4.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox4)

        self.slider1 = QtWidgets.QSlider(self.centralwidget)
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.slider1.setMaximum(100)
        self.horizontalLayout_2.addWidget(self.slider1)

        self.slider1label = QtWidgets.QLabel(self.centralwidget)
        self.slider1label.setObjectName("slider1label")
        self.horizontalLayout_2.addWidget(self.slider1label)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.comboBox5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox5.setObjectName("comboBox5")
        # self.comboBox5.addItem("")
        # self.comboBox5.addItem("")
        # self.comboBox5.addItem("")
        # self.comboBox5.addItem("")
        # self.comboBox5.addItem("")
        # self.comboBox5.addItem("")
        # self.comboBox5.addItem("")
        self.gridLayout_4.addWidget(self.comboBox5, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.comboBox6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox6.setObjectName("comboBox6")
        # self.comboBox6.addItem("")
        # self.comboBox6.addItem("")
        # self.comboBox6.addItem("")
        self.horizontalLayout.addWidget(self.comboBox6)
        self.slider2 = QtWidgets.QSlider(self.centralwidget)
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setMaximum(100)
        self.slider2.setObjectName("slider2")
        self.horizontalLayout.addWidget(self.slider2)
        self.slider2label = QtWidgets.QLabel(self.centralwidget)
        self.slider2label.setObjectName("slider2label")
        self.horizontalLayout.addWidget(self.slider2label)
        self.gridLayout_4.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.comboBox7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox7.setObjectName("comboBox7")
        # self.comboBox7.addItem("")
        # self.comboBox7.addItem("")
        # self.comboBox7.addItem("")
        # self.comboBox7.addItem("")
        # self.comboBox7.addItem("")
        # self.comboBox7.addItem("")
        # self.comboBox7.addItem("")
        self.gridLayout_4.addWidget(self.comboBox7, 4, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)
        self.output1 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output1.sizePolicy().hasHeightForWidth())
        self.output1.setSizePolicy(sizePolicy)
        self.output1.setMinimumSize(QtCore.QSize(0, 0))
        self.output1.setObjectName("output1")
        self.gridLayout_3.addWidget(self.output1, 1, 0, 1, 1)
        self.output2 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output2.sizePolicy().hasHeightForWidth())
        self.output2.setSizePolicy(sizePolicy)
        self.output2.setMinimumSize(QtCore.QSize(0, 0))
        self.output2.setObjectName("output2")
        self.gridLayout_3.addWidget(self.output2, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setObjectName("comboBox2")
        # self.comboBox2.addItem("")
        # self.comboBox2.addItem("")
        # self.comboBox2.addItem("")
        # self.comboBox2.addItem("")
        # self.comboBox2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox2, 0, 1, 1, 1)
        self.image2 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image2.sizePolicy().hasHeightForWidth())
        self.image2.setSizePolicy(sizePolicy)
        self.image2.setMinimumSize(QtCore.QSize(0, 0))
        self.image2.setObjectName("image2")
        self.gridLayout_2.addWidget(self.image2, 1, 0, 1, 1)
        self.updated2 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updated2.sizePolicy().hasHeightForWidth())
        self.updated2.setSizePolicy(sizePolicy)
        self.updated2.setMinimumSize(QtCore.QSize(0, 0))
        self.updated2.setObjectName("updated2")
        self.gridLayout_2.addWidget(self.updated2, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setObjectName("comboBox1")
        # self.comboBox1.addItem("")
        # self.comboBox1.addItem("")
        # self.comboBox1.addItem("")
        # self.comboBox1.addItem("")
        # self.comboBox1.addItem("")
        self.gridLayout.addWidget(self.comboBox1, 0, 1, 1, 1)
        self.image1 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image1.sizePolicy().hasHeightForWidth())
        self.image1.setSizePolicy(sizePolicy)
        self.image1.setMinimumSize(QtCore.QSize(0, 0))
        self.image1.setObjectName("image1")
        self.gridLayout.addWidget(self.image1, 1, 0, 1, 1)
        self.updated1 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updated1.sizePolicy().hasHeightForWidth())
        self.updated1.setSizePolicy(sizePolicy)
        self.updated1.setMinimumSize(QtCore.QSize(0, 0))
        self.updated1.setObjectName("updated1")
        self.gridLayout.addWidget(self.updated1, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(535, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 26))
        self.menubar.setObjectName("menubar")
        self.menuopen = QtWidgets.QMenu(self.menubar)
        self.menuopen.setObjectName("menuopen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionimage1 = QtWidgets.QAction(MainWindow)
        self.actionimage1.setObjectName("actionimage1")
        self.actionimage2 = QtWidgets.QAction(MainWindow)
        self.actionimage2.setObjectName("actionimage2")
        self.menuopen.addAction(self.actionimage1)
        self.menuopen.addAction(self.actionimage2)
        self.menubar.addAction(self.menuopen.menuAction())
        self.slider1.sliderMoved['int'].connect(self.slider1label.setNum)
        self.slider2.sliderMoved['int'].connect(self.slider2label.setNum)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_17.setText(_translate("MainWindow", "mixer output to"))
        # self.comboBox3.setItemText(0, _translate("MainWindow", "output"))
        # self.comboBox3.setItemText(1, _translate("MainWindow", "output2"))
        # self.comboBox3.setItemText(2, _translate("MainWindow", "output1"))
        self.label_16.setText(_translate("MainWindow", "Component 1"))
        # self.comboBox4.setItemText(0, _translate("MainWindow", "image1,2"))
        # self.comboBox4.setItemText(1, _translate("MainWindow", "image1"))
        # self.comboBox4.setItemText(2, _translate("MainWindow", "image2"))
        self.slider2label.setText(_translate("MainWindow", "0%"))
        # self.comboBox5.setItemText(0, _translate("MainWindow", "mode1"))
        # self.comboBox5.setItemText(1, _translate("MainWindow", "magnitude"))
        # self.comboBox5.setItemText(2, _translate("MainWindow", "phase"))
        # self.comboBox5.setItemText(3, _translate("MainWindow", "real"))
        # self.comboBox5.setItemText(4, _translate("MainWindow", "imaginary"))
        # self.comboBox5.setItemText(5, _translate("MainWindow", "uniform magnitude"))
        # self.comboBox5.setItemText(6, _translate("MainWindow", "uniform phase"))
        self.label_15.setText(_translate("MainWindow", "Component 2"))
        # self.comboBox6.setItemText(0, _translate("MainWindow", "image 1,2"))
        # self.comboBox6.setItemText(1, _translate("MainWindow", "image1"))
        # self.comboBox6.setItemText(2, _translate("MainWindow", "image2"))
        self.slider1label.setText(_translate("MainWindow", "0%"))
        # self.comboBox7.setItemText(0, _translate("MainWindow", "mode2"))
        # self.comboBox7.setItemText(1, _translate("MainWindow", "magnitude"))
        # self.comboBox7.setItemText(2, _translate("MainWindow", "phase"))
        # self.comboBox7.setItemText(3, _translate("MainWindow", "real"))
        # self.comboBox7.setItemText(4, _translate("MainWindow", "imaginary"))
        # self.comboBox7.setItemText(5, _translate("MainWindow", "uniform magnitude"))
        # self.comboBox7.setItemText(6, _translate("MainWindow", "uniform phase"))
        self.label_13.setText(_translate("MainWindow", "output 1"))
        self.label_14.setText(_translate("MainWindow", "output 2"))
        self.label_2.setText(_translate("MainWindow", "Image 2"))
        # self.comboBox2.setItemText(0, _translate("MainWindow", "Mag,phase,Real,imag"))
        # self.comboBox2.setItemText(1, _translate("MainWindow", "magnitude"))
        # self.comboBox2.setItemText(2, _translate("MainWindow", "phase"))
        # self.comboBox2.setItemText(3, _translate("MainWindow", "real"))
        # self.comboBox2.setItemText(4, _translate("MainWindow", "imaginary"))
        self.label.setText(_translate("MainWindow", "Image 1"))
        # self.comboBox1.setItemText(0, _translate("MainWindow", "Mag,phase,Real,imag"))
        # self.comboBox1.setItemText(1, _translate("MainWindow", "magnitude"))
        # self.comboBox1.setItemText(2, _translate("MainWindow", "phase"))
        # self.comboBox1.setItemText(3, _translate("MainWindow", "real"))
        # self.comboBox1.setItemText(4, _translate("MainWindow", "imaginary"))
        self.menuopen.setTitle(_translate("MainWindow", "open"))
        self.actionimage1.setText(_translate("MainWindow", "image 1"))
        self.actionimage2.setText(_translate("MainWindow", "image2"))
from pyqtgraph import ImageView


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())