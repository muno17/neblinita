from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = QMainWindow()
window.show()

app.exec()