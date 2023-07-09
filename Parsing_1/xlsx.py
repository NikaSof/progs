import xlsxwriter
import odfpy
from main import array


def writer(parametr):

    book = xlsxwriter.Workbook(r"C:\Users\Nika\Desktop\Parsing.ods")
    page = book.add_worksheet("товар")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 20)

    for item in parametr:
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row += 1

    book.close()


writer(array)
