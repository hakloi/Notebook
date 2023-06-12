# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PyQt5.QtCore import Qt, QTimer
# import sys
# import datetime


    
# class Window(QMainWindow):
#     def __init__(self):
#         super(Window, self).__init__()
        
#         self.setWindowTitle("Notebook")
#         self.setGeometry(400,400,600,300)
        
#         self.text_data = QtWidgets.QLabel(self)
#         self.text_data.setText("Дата:")
#         self.text_data.adjustSize()
#         self.text_data.move(10,52)
        
#         self.text_time = QtWidgets.QLabel(self)
#         self.text_time.setText("Время:")
#         self.text_time.adjustSize()
#         self.text_time.move(10,103)
        
#         self.data=QtWidgets.QDateEdit(self)
#         self.data.move(100,50)
#         self.data.adjustSize()
        
#         self.time = QtWidgets.QTimeEdit(self)
#         self.time.move(110,100)
#         self.time.adjustSize()
        
#         self.message = QtWidgets.QLineEdit(self)
#         self.message.setGeometry(100,150,160,30)
#         self.message.adjustSize()
#         self.message.setPlaceholderText("Сообщение:")
        
#         self.button = QtWidgets.QPushButton(self)
#         self.button.move(210,80)
#         self.button.setText("Готово!")
#         self.button.adjustSize()
        
        
# def aplic():
#     app = QApplication(sys.argv)
#     window = Window()
    
#     window.show()
#     sys.exit(app.exec_())
    
# if __name__ == '__main__':
#     aplic()    