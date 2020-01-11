import PyPDF2
import time
from tkinter import *
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

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

        w = float(p.mediaBox.getWidth()) * 0.352
        h = float(p.mediaBox.getHeight()) * 0.352
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

            unformat = str(str(w), '*', str(h))
            pageSizesList.append(unformat)

    # pdf.close()

ta4 = 'A4: ' + str(a4)
ta3 = 'A3: ' + str(a3)
ta2 = 'A2: ' + str(a2)
ta1 = 'A1: ' + str(a1)
ta0 = 'A0: ' + str(a0)
tunsize = 'Неформат:' + str(pageSizesList)


print('A4: ', a4)
print('A3: ', a3)
print('A2: ', a2)
print('A1: ', a1)
print('A0: ', a0)
print(pageSizesList)
print("--- %s seconds ---" % (time.time() - start_time))
work_time = 'Время выполения: ', str(float((time.time() - start_time))), 'сек'

window = Tk()
window.geometry('600x250')
window.title("Результаты анализа файла")
lbl = Label(window, text=ta4, font=("Arial Bold", 14))
lbl.grid(column=0, row=0)
lbl = Label(window, text=ta3, font=("Arial Bold", 14))
lbl.grid(column=1, row=0)
lbl = Label(window, text=ta2, font=("Arial Bold", 14))
lbl.grid(column=0, row=1)
lbl = Label(window, text=ta1, font=("Arial Bold", 14))
lbl.grid(column=1, row=1)
lbl = Label(window, text=ta0, font=("Arial Bold", 14))
lbl.grid(column=0, row=2)
lbl = Label(window, text=tunsize, font=("Arial Bold", 14))
lbl.grid(column=0, row=3)
lbl = Label(window, text=work_time, font=("Arial Bold", 14))
lbl.grid(column=0, row=4)
window.mainloop()
