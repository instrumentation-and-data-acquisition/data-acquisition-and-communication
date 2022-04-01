import serial
import time
import os
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from sys import exit
import numpy as np

class MainWindow(QtWidgets.QMainWindow,):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.startbutton= QPushButton('stop',self)
        self.startbutton.clicked.connect(self.startMethod)
        
        self.clearbutton= QPushButton('clear',self)
        self.clearbutton.clicked.connect(self.clearMethod)
        self.clearbutton.move(120,0)

        self.x = list(range(100))  # 100 time points
        self.y = [0] * 100  # 100 data points
        
        self.i = 0 #iteration variable for update_plot_data fucntion

        self.option = ''

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        
        
        
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        
    def initialQuestion(self):
        
        print("Deseja começar a aquisição?\n")
        self.option=input("Escreva start\n")
        ser.write(self.option.encode('utf-8'))
        dummyRead = ser.readline().decode('utf-8').rstrip()
        while self.option!='start':
            error = ser.readline().decode('utf-8').rstrip() # read só funciona tendo write
            print(error)
            print("Deseja começar a aquisição?\n")
            self.option=input("Escreva start\n")
            ser.write(self.option.encode('utf-8'))
            error = ser.readline().decode('utf-8').rstrip()
            print(error)
            
        
    def startMethod(self):
        if self.startbutton.isEnabled(): #quando o startbutton esta enable o grafico está parado
            if self.startbutton.text()=='stop':
                print("tou ligado")
                #self.startbutton.setEnabled(False)
                self.startbutton.setText('start')
                self.timer.stop()
            else:
                print("tou ligado1")
                #self.startbutton.setEnabled(False)
                self.startbutton.setText('stop')
                self.timer.start()
                
                
    def clearMethod(self):
        if self.clearbutton.isEnabled(): #quando o startbutton esta enable o grafico está parado
            self.data_line.clear()
            #self.x=0
            self.x = list(range(100))  # 100 time points
            self.y = [0] * 100
            

    def update_plot_data(self):
        
        #if (self.i == 0):
         #   self.initialQuestion
          #  ++self.i

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        
        
        #if ser.in_waiting> 0:
        ser.write(self.option.encode('utf-8')) # quando dá fatal error dá erro
        aux = ser.readline().decode('utf-8').rstrip()
        
        #if (aux):
            #if (self.i < 100):
            #    print(aux)
            #   self.y[self.i] = int(aux)
            #else:
        self.y = self.y[1:]
        self.y.append(int(aux))
            #++self.i
        #line = ser.readline().decode('utf-8').rstrip()
        print(aux)
        #.sleep(1)

        self.data_line.setData(self.x, self.y)  # Update the data.
if(os.path.exists('/dev/ttyACM0')):
    path='/dev/ttyACM0'
if(os.path.exists('/dev/ttyACM1')):
    path='/dev/ttyACM1'
    
   

if __name__ == '__main__':
    ser = serial.Serial(path , 9600, timeout=1)
    ser.reset_input_buffer()
    
    import sys
    
    #else:
    app = QtWidgets.QApplication(sys.argv)
    
    w = MainWindow()
    w.initialQuestion()
    w.show()
    sys.exit(app.exec_())
