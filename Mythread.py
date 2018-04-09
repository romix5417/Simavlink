from PyQt5.QtCore import * 


class MyThread(QThread):
    def run(self, func):
        func()


