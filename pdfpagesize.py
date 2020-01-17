import PyPDF2
import time
from tkinter import *
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import select


start_time = time.time()
a4 = 0
a3 = 0
a2 = 0
a1 = 0
a0 = 0
directory = 'Originals/'
# Получаем список файлов в переменную files
files = os.listdir(directory)


for filename in files:
    pdf = PyPDF2.PdfFileReader('Originals/'+filename,"rb")
    pages = int(str(pdf.numPages))
    print(pages)
    print(filename)
    pageSizesList = []

    for page in range(pages):
        p = pdf.getPage(page)
        w_in_user_space_units = p.mediaBox.getWidth()
        h_in_user_space_units = p.mediaBox.getHeight()

        # 1 user space unit is 1/72 inch
        # 1/72 inch ~ 0.352 millimeters

        w = float(p.mediaBox.getWidth()) * 0.35278
        h = float(p.mediaBox.getHeight()) * 0.35278

        if (w > 914 and h < 594): h = 600
        if (h > 914 and w < 594): w = 600

        s = w*h
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(p)

        if s <= 63000:
            a4 += 1

            outputFilename = "A4/{}-{}.pdf".format(filename, (page + 1))
            with open(outputFilename, "wb") as out:
                pdf_writer.write(out)

        elif s > 63000 and s <= 125000:
            a3 += 1

            outputFilename = "A3/{}-{}.pdf".format(filename, (page + 1))
            with open(outputFilename, "wb") as out:
                pdf_writer.write(out)

        elif (s > 125000 and s <= 250000) and ((w >= 590 or w <= 600) or (h >= 590 or h <= 600)):


            a2 += 1

            outputFilename = "A2/{}-{}.pdf".format(filename, (page + 1))
            with open(outputFilename, "wb") as out:
                pdf_writer.write(out)

        elif (s > 250000 and s <= 500000)  and ((w >= 835 or w <= 845) or (h >= 835 or h <= 845)):
            a1 += 1

            outputFilename = "A1/{}-{}.pdf".format(filename, (page + 1))
            with open(outputFilename, "wb") as out:
                pdf_writer.write(out)

        elif (s > 500000 and s <= 1000000)  and ((w >= 1185 or w <= 1195) or (h >= 1185 or h <= 1195)):
            a0 += 1

            outputFilename = "A0/{}-{}.pdf".format(filename, (page + 1))
            with open(outputFilename, "wb") as out:
                pdf_writer.write(out)
        else:
            outputFilename = "Unformat/{}-{}.pdf".format(filename, (page + 1))
            with open(outputFilename, "wb") as out:
                pdf_writer.write(out)

            unformat = str(int(w)),  str(int(h))
            pageSizesList.append(unformat)
            print(pageSizesList)

    

ta4 = 'A4: ' + str(a4)
ta3 = 'A3: ' + str(a3)
ta2 = 'A2: ' + str(a2)
ta1 = 'A1: ' + str(a1)
ta0 = 'A0: ' + str(a0)
tunsize = 'Неформат: ' + str(pageSizesList)


print('A4: ', a4)
print('A3: ', a3)
print('A2: ', a2)
print('A1: ', a1)
print('A0: ', a0)
print(pageSizesList)
print("--- %s seconds ---" % (time.time() - start_time))
work_time = 'Время выполения: ' + str(int((time.time() - start_time))) + ' сек'



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(292, 886)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 9, 200, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("Результаты посчета:")
        self.verticalLayout.addWidget(self.label)
        self.label_a4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_a4.setFont(font)
        self.label_a4.setObjectName(ta4)
        self.verticalLayout.addWidget(self.label_a4)
        self.label_a3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_a3.setFont(font)
        self.label_a3.setObjectName(ta3)
        self.verticalLayout.addWidget(self.label_a3)
        self.label_a2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_a2.setFont(font)
        self.label_a2.setObjectName(ta2)
        self.verticalLayout.addWidget(self.label_a2)
        self.label_a1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_a1.setFont(font)
        self.label_a1.setObjectName(ta1)
        self.verticalLayout.addWidget(self.label_a1)
        self.label_a0 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_a0.setFont(font)
        self.label_a0.setObjectName(ta0)
        self.verticalLayout.addWidget(self.label_a0)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(19, 369, 261, 441))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("Unformat")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.label_time = QtWidgets.QLabel(Form)
        self.label_time.setGeometry(QtCore.QRect(20, 822, 261, 41))
        self.label_time.setObjectName('text')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Кидалка по форматам"))
        self.label.setText(_translate("Form", "Результат подсчета"))
        self.label_a4.setText(_translate("Form", ta4))
        self.label_a3.setText(_translate("Form", ta3))
        self.label_a2.setText(_translate("Form", ta2))
        self.label_a1.setText(_translate("Form", ta1))
        self.label_a0.setText(_translate("Form", ta0))
        self.textBrowser.setText(tunsize)
        self.label_time.setText(_translate("Form", str(work_time)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
