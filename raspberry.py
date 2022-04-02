import serial #import serial to communicate with arduino
import time #import time to create timer to repeat data acquisition
import os #used to check in which port the arduino connected to the raspberry pi on
import pyqtgraph as pg #used to create the window and the graph
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from sys import exit #for closing the app

class MainWindow(QtWidgets.QMainWindow,): #class made for creating the window and everything that needs to be done in it

    def __init__(self, *args, **kwargs): #constructor of the class
        super(MainWindow, self).__init__(*args, **kwargs) 

        self.graphWidget = pg.PlotWidget() #setting the window to have a graph widget
        self.setCentralWidget(self.graphWidget) # centring the graph

        self.startbutton = QPushButton('Stop',self) #creating a stop button to stop acquisition
        self.startbutton.clicked.connect(self.startMethod) #calling the method to stop the acquisition
        
        self.clearbutton = QPushButton('Clear',self) #creating a clear button to clear the graph and start again
        self.clearbutton.clicked.connect(self.clearMethod) #calling the method to clear the graph
        self.clearbutton.move(120,0)

        self.x = list(range(100))  #graph displays 100 points from 0 to 99 on x
        self.y = [0] * 100  #and 100 points at 0 initially for y
        
        self.option = ''

        self.graphWidget.setBackground('k') #setting background color to black
        pen = pg.mkPen(color=(0, 157, 224)) #setting the line color to ist blue
        
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen) #initializes the line for the data
        self.timer = QtCore.QTimer() #initializes the timer
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.update_plot_data) #iterates through the function update_plot_data while the timer is counting
        self.timer.start() #starts the timer
        
    def initialQuestion(self):
        """
        sends the initial question to the user to start (or not) the acquisition
        saves the option the user picks in the variable self.option and then always sends it to arduino
        """
        print("Deseja começar a aquisição?")
        self.option=input("Escreva start:\n") #gets input from the user and saves it to self.option
        ser.write(self.option.encode('utf-8')) #sends self.option to the serial for arduino to read
        dummyRead = ser.readline().decode('utf-8').rstrip() #arduino sends in a first line that is blank
        arduino = ser.readline().decode('utf-8').rstrip() # reads the proper answer from arduino
        print(arduino) #prints the message from arduino, FATAL ERROR if self.option is not start and
                       #the voltage value mapped to 0, 1023 if it is
        while (arduino.isdigit() == False): #checks if arduino sent a number, if not then it sent FATAL ERROR
                                            #and repeats what it did before again
            print("\nDeseja começar a aquisição?")
            self.option=input("Escreva start:\n")
            ser.write(self.option.encode('utf-8'))
            arduino = ser.readline().decode('utf-8').rstrip()
            
    def startMethod(self):
        """
        method for starting and stopping the acquisition with a button
        """
        if self.startbutton.isEnabled(): #if the start button is clicked, then check for the other conditions to start/stop
            if self.startbutton.text()=='Stop': #if the sbutton says stop, then the graph is going
                print("Stopping Acquisition...")
                self.startbutton.setText('Start') #changes the text to start again
                self.timer.stop() #stops the timer stopping the acquisition
            elif self.startbutton.text()=='Start': #if the button says start, then the graph is stopped
                print("Resuming Acquisition...")
                self.startbutton.setText('Stop') #changes the text to sgtop again
                self.timer.start() #starts the timer to resume acquisition                
                
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
        if (aux.isdigit()):
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
