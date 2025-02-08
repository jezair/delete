''' Вікно для картки питання '''
from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_window_copy import *

def show_result():
   ''' показати панель відповідей '''
   RadioGroupBox.hide()
   AnsGroupBox.show()
   btn_OK.setText('Наступне питання')

def show_question():
   ''' показати панель питань '''
   RadioGroupBox.show()
   AnsGroupBox.hide()
   btn_OK.setText('Відповісти')
   # скинути вибрану радіо-кнопку
   RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки
   rbtn_1.setChecked(False)
   rbtn_2.setChecked(False)
   rbtn_3.setChecked(False)
   rbtn_4.setChecked(False)
   RadioGroup.setExclusive(True) # повернули обмеження, тепер лише одна радіокнопка може бути вибрана

def show_data():
   ''' показує потрібну інформацію на екрані '''
   # об'єднаємо у функцію схожі дії
   lb_Question.setText(frm_question)
   lb_Correct.setText(frm_right)
   answer.setText(frm_right)
   wrong_answer1.setText(frm_wrong1)
   wrong_answer2.setText(frm_wrong2)
   wrong_answer3.setText(frm_wrong3)

def check_result():
   ''' перевірка, чи правильна відповідь обрана
   якщо відповідь була обрана, то напис "правильно/неправильно" набуває потрібного
   значення і показується панель відповідей
   '''
   correct = answer.isChecked() # у цьому радіобаттоні лежить наша відповідь!
   if correct:
       # відповідь вірна, запишемо
       lb_Result.setText(text_correct) # напис "правильно" або "неправильно"
       show_result()
   else:
       incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
       if incorrect:
           # відповідь невірна, запишемо і відобразимо у статистиці
           lb_Result.setText(text_wrong) # напис "правильно" або "неправильно"
           show_result()

def click_OK(self):
   # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
   if btn_OK.text() != 'Наступне питання':
       check_result()

show_data()
show_question()
btn_OK.clicked.connect(click_OK)

app.exec_()