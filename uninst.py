from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QMessageBox, QProgressBar
)
from PyQt6.QtCore import Qt, QTimer
import os
import sys

class Uninstaller(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Uninstaller - MercuryOS Professional")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Click the button below to uninstall MercuryOS Professional if you are sure.", self)
        self.label.setWordWrap(True)

        self.uninstall_button = QPushButton("Uninstall MercuryOS Ultimate", self)
        self.uninstall_button.clicked.connect(self.confirm_uninstall)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.uninstall_button)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def confirm_uninstall(self):
        reply = QMessageBox.question(
            self, 'Confirm Uninstall',
            "Are you sure you want to uninstall MercuryOS Ultimate?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.start_uninstall()

    def start_uninstall(self):
        self.progress_bar.setVisible(True)
        self.uninstall_button.setEnabled(False)
        self.label.setText("Uninstalling MercuryOS Ultimate...")
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        self.timer.start(100)

    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 10
            self.progress_bar.setValue(self.progress_value)
        else:
            self.timer.stop()
            self.delete_file()

    def delete_file(self):
        file_path = r"C:\Users\kumar17\OneDrive - Ecolab\Desktop\MercuryOS Ultimate\MercuryOS Professional.py"
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                QMessageBox.information(self, "Uninstall Complete", "MercuryOS Ultimate has been successfully uninstalled.")
            else:
                QMessageBox.warning(self, "File Not Found", "The file does not exist.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while uninstalling: {e}")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Uninstaller()
    window.show()
    sys.exit(app.exec())