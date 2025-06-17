from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QComboBox,
    QVBoxLayout, QSpinBox, QMessageBox
)
from database import create_connection


class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales Form")
        self.setMinimumWidth(600)

        # --- Fields ---
        self.product_input = QLineEdit()
        self.customer_input = QLineEdit()

        self.quantity_input = QSpinBox()
        self.quantity_input.setMaximum(10000)

        self.unit_input = QComboBox()
        self.unit_input.addItems(["PCS", "KG", "Litre", "Dozen"])

        self.rate_input = QLineEdit()
        self.tax_input = QSpinBox()
        self.tax_input.setMaximum(100)

        self.total_rate_display = QLineEdit()
        self.total_rate_display.setReadOnly(True)

        calc_btn = QPushButton("Calculate Total")
        calc_btn.clicked.connect(self.calculate_total)

        save_btn = QPushButton("Save Sale")
        save_btn.clicked.connect(self.save_sale)

        # --- Layout ---
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Product Name"))
        layout.addWidget(self.product_input)

        layout.addWidget(QLabel("Customer Name"))
        layout.addWidget(self.customer_input)

        layout.addWidget(QLabel("Quantity"))
        layout.addWidget(self.quantity_input)

        layout.addWidget(QLabel("Unit of Measurement"))
        layout.addWidget(self.unit_input)

        layout.addWidget(QLabel("Rate per Unit"))
        layout.addWidget(self.rate_input)

        layout.addWidget(QLabel("Tax (%)"))
        layout.addWidget(self.tax_input)

        layout.addWidget(QLabel("Total Rate"))
        layout.addWidget(self.total_rate_display)

        layout.addWidget(calc_btn)
        layout.addWidget(save_btn)

        self.setLayout(layout)

    def calculate_total(self):
        try:
            quantity = self.quantity_input.value()
            rate = float(self.rate_input.text())
            tax = self.tax_input.value()

            subtotal = quantity * rate
            total = subtotal + (subtotal * tax / 100)
            self.total_rate_display.setText(f"{total:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid rate.")

    def save_sale(self):
        conn = create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO sales 
                (product_id, customer, quantity, unit, rate_per_unit, tax, total_rate)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                self.product_input.text(),
                self.customer_input.text(),
                self.quantity_input.value(),
                self.unit_input.currentText(),
                self.rate_input.text(),
                self.tax_input.value(),
                self.total_rate_display.text()
            ))
            conn.commit()
            QMessageBox.information(self, "Saved", "Sales entry saved.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saving to DB:\n{e}")
        finally:
            conn.close()
