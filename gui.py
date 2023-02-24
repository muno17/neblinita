from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(500,300))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()