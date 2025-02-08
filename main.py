from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_window import *

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.swtText("Next question")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.show()
    btn_OK.setText("Widowisti")

    