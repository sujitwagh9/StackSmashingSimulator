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
        
        # Text editor for input code
        self.text_area = QTextEdit(self)
        self.text_area.setPlaceholderText("Enter C/C++ code here...")
        
        # Output label to display results
        self.output_label = QLabel(self)
        self.output_label.setWordWrap(True)
        
        # Analyze button to trigger analysis
        self.analyze_button = QPushButton("Analyze Code", self)
        self.analyze_button.clicked.connect(self.analyze_code)
        
        # Layout configuration
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.analyze_button)
        layout.addWidget(self.output_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def analyze_code(self):
        """
        This function triggers the analysis of the input code.
        It parses, detects vulnerabilities, emulates the stack, visualizes the results, and demonstrates protections.
        """
        code = self.text_area.toPlainText()  # Get the code from the text area
        
        if not code.strip():
            self.output_label.setText("Please enter some C/C++ code for analysis.")
            return
        
        # Step 1: Parse the code
        parsed_code = parse_code(code)
        
        # Step 2: Detect vulnerabilities
        vulnerabilities = detect_vulnerabilities(parsed_code)
        
        # Step 3: Emulate the stack based on the parsed code
        stack_emulation = emulate_stack(parsed_code)
        
        # Step 4: Visualize the stack emulation
        visualization = visualize_stack(stack_emulation)
        
        # Step 5: Demonstrate protection mechanisms
        protection = demonstrate_protection(stack_emulation)
        
        # Format the output for display
        output_text = (
            f"Vulnerabilities Detected:\n{vulnerabilities}\n\n"
            f"Stack Visualization:\n{visualization}\n\n"
            f"Protection Mechanisms:\n{protection}"
        )
        
        # Set the output text in the label
        self.output_label.setText(output_text)

if __name__ == "__main__":
    app = QApplication([])
    window = StackSmashingSimulator()
    window.show()
    app.exec_()
