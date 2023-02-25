import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello app')
        self.resize(500,300)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.inputField = QLineEdit()
        button = QPushButton('&Say Hello', clicked=self.sayHello)
        #button.clicked.connect(self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello {0}'.format(inputText))


app = QApplication(sys.argv)

window = MyApp()
window.show()

sys.exit(app.exec())