# dashboard.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from product import ProductMasterForm
from goods import GoodsReceivingForm
from sales_form import SalesForm

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        layout = QVBoxLayout()

        self.btn_product = QPushButton("Product Master")
        self.btn_product.clicked.connect(self.open_product)
        layout.addWidget(self.btn_product)

        self.btn_goods = QPushButton("Goods Receiving")
        self.btn_goods.clicked.connect(self.open_goods)
        layout.addWidget(self.btn_goods)

        self.btn_sales = QPushButton("Sales")
        self.btn_sales.clicked.connect(self.open_sales)
        layout.addWidget(self.btn_sales)

        self.setLayout(layout)

    def open_product(self):
        self.pm = ProductMasterForm()
        self.pm.show()

    def open_goods(self):
        self.gr = GoodsReceivingForm()
        self.gr.show()

    def open_sales(self):
        self.sf = SalesForm()
        self.sf.show()
