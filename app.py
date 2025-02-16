from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        self.display = QLineEdit()
        layout.addWidget(self.display)
        
        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]
        
        for btn_text, x, y in buttons:
            button = QPushButton(btn_text)
            button.clicked.connect(lambda checked, text=btn_text: self.on_button_click(text))
            grid.addWidget(button, x, y)
        
        layout.addLayout(grid)
        self.setLayout(layout)
    
    def on_button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
