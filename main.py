# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from parser import parse_code
from vulnerability_detector import detect_vulnerabilities
from emulator import emulate_stack
from visualizer import visualize_stack
from protector import demonstrate_protection

class StackSmashingSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stack Smashing Simulator")
        self.setGeometry(100, 100, 800, 600)
        
        self.text_area = QTextEdit(self)
        self.output_label = QLabel(self)
        self.analyze_button = QPushButton("Analyze Code", self)
        self.analyze_button.clicked.connect(self.analyze_code)
        
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.analyze_button)
        layout.addWidget(self.output_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def analyze_code(self):
        code = self.text_area.toPlainText()
        parsed_code = parse_code(code)
        vulnerabilities = detect_vulnerabilities(parsed_code)
        stack_emulation = emulate_stack(parsed_code)
        visualization = visualize_stack(stack_emulation)
        protection = demonstrate_protection(stack_emulation)
        self.output_label.setText(f"Vulnerabilities: {vulnerabilities}\nStack Visualization: {visualization}\nProtections: {protection}")

if __name__ == "__main__":
    app = QApplication([])
    window = StackSmashingSimulator()
    window.show()
    app.exec_()
