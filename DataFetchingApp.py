import sys
import csv
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *
from PySide2.QtCore import *


class DataApp(QWidget):
    def __init__(self):
        super(DataApp, self).__init__()
        label = QLabel("Customer Info")
        label.setFont(QFont("Sens serif", 28))
        label.setAlignment(Qt.AlignCenter)

        totalrow = self.row_count()
        table = QTableWidget(totalrow, 4, parent=None)
        cols = ["customer Id", "Customer Name", "Contact No", "Email"]
        table.setHorizontalHeaderLabels(cols)

        filename = 'customer.csv'
        fields = []
        rows = []

        r = 0
        c = 0
        with open(filename, 'r') as f:
            data = csv.reader(f)
            fields = data.line_num
            for row in data:
                for col in row:
                    print(col)
                    table.setItem(r, c, QTableWidgetItem(col))
                    c += 1
                c = 0
                r += 1

        # layout = QHBoxLayout()
        layout = QVBoxLayout()  # for vertical layout and label in top
        layout.addWidget(label)
        layout.addWidget(table)
        self.setLayout(layout)
        self.setWindowTitle("An app to customer records")
        self.show()

    def row_count(self):
        filename = 'customer.csv'
        fields = []
        rows = []

        with open(filename, 'r') as f:
            data = csv.reader(f)
            fields = data.line_num
            for row in data:
                rows.append(row)
            print(data.line_num)
            print(type(data.line_num))
            return data.line_num



app = QApplication([])
window = DataApp()
sys.exit(app.exec_())
