from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
QPushButton, QLabel, QVBoxLayout, QButtonGroup, QRadioButton, QHBoxLayout, QGroupBox)

from random import shuffle , randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('В каком году родился Аль-Хорезми?', '783', '971', '865', '1995'))
question_list.append(Question('Какая самая быстрая машина в мире', 'Bugatti Chiron', 'Pagani', 'Bugatti Veyron', 'BMW'))
question_list.append(Question('Сколько истребителей в Узбекистане?', '450', '115', '250', '10'))
        
app =QApplication([])
main_win = QWidget()

btn_ok = QPushButton('Ответить')
question = QLabel()
