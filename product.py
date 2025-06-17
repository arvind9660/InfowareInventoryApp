from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox,
    QVBoxLayout, QHBoxLayout, QFileDialog, QSpinBox, QMessageBox
)
from PySide6.QtGui import QPixmap
from database import create_connection
import os
import shutil


class ProductMasterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master Form")
        self.setMinimumWidth(600)

        # --- Fields ---
        self.barcode_input = QLineEdit()
        self.sku_input = QLineEdit()
        self.category_input = QLineEdit()
        self.subcategory_input = QLineEdit()
        self.name_input = QLineEdit()
        self.description_input = QTextEdit()
        self.tax_input = QSpinBox()
        self.tax_input.setMaximum(100)
        self.price_input = QLineEdit()
        self.unit_input = QComboBox()
        self.unit_input.addItems(["PCS", "KG", "Litre", "Dozen"])

        # Image
        self.image_path = ""
        self.image_label = QLabel("No Image Selected")
        self.image_label.setFixedHeight(100)
        self.image_label.setScaledContents(True)

        image_btn = QPushButton("Upload Product Image")
        image_btn.clicked.connect(self.select_image)

        # Save Button
        save_btn = QPushButton("Save Product")
        save_btn.clicked.connect(self.save_product)

        # --- Layout ---
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Barcode"))
        layout.addWidget(self.barcode_input)

        layout.addWidget(QLabel("SKU ID"))
        layout.addWidget(self.sku_input)

        layout.addWidget(QLabel("Category"))
        layout.addWidget(self.category_input)

        layout.addWidget(QLabel("Subcategory"))
        layout.addWidget(self.subcategory_input)

        layout.addWidget(QLabel("Product Name"))
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Description"))
        layout.addWidget(self.description_input)

        layout.addWidget(QLabel("Tax (%)"))
        layout.addWidget(self.tax_input)

        layout.addWidget(QLabel("Price"))
        layout.addWidget(self.price_input)

        layout.addWidget(QLabel("Unit of Measurement"))
        layout.addWidget(self.unit_input)

        layout.addWidget(QLabel("Product Image"))
        layout.addWidget(self.image_label)
        layout.addWidget(image_btn)

        layout.addWidget(save_btn)

        self.setLayout(layout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)

    def save_product(self):
        conn = create_connection()
        cursor = conn.cursor()

        # Copy image to local folder
        saved_image_path = ""
        if self.image_path:
            folder = "product_images"
            os.makedirs(folder, exist_ok=True)
            filename = os.path.basename(self.image_path)
            saved_image_path = os.path.join(folder, filename)
            shutil.copy(self.image_path, saved_image_path)

        # Insert data
        try:
            cursor.execute("""
                INSERT INTO product_master 
                (barcode, sku_id, category, subcategory, name, description, tax, price, unit, image_path)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.barcode_input.text(),
                self.sku_input.text(),
                self.category_input.text(),
                self.subcategory_input.text(),
                self.name_input.text(),
                self.description_input.toPlainText(),
                self.tax_input.value(),
                self.price_input.text(),
                self.unit_input.currentText(),
                saved_image_path
            ))
            conn.commit()
            QMessageBox.information(self, "Success", "Product saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save product:\n{e}")
        finally:
            conn.close()
