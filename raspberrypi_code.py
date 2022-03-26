import serial
import time
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import numpy as np

title = "Data from Arduino"
vals = np.zeros(10)
t = np.zeros(10)


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0' , 9600, timeout=1)
    ser.reset_input_buffer()
    
    import sys

    i = 0

    while True:
        ser.write("start".encode('utf-8')) # quando dá fatal error dá erro
        #if ser.in_waiting> 0:
        aux = ser.readline().decode('utf-8').rstrip()
        if (aux):
            vals[i] = int(aux)
        #line = ser.readline().decode('utf-8').rstrip()
        print(vals[i])
        time.sleep(1)
        t[i] = i
        if (i == 9):
            break
        i += 1

    plt = pg.plot()
    plt.showGrid(x = True, y = True) # vals só dif de 0 a oartir do inhdice 2
    plt.setXRange(0, 9)
    plt.setYRange(0, 700)
    plt.setWindowTitle(title)

    line = plt.plot(t, vals)
    
    if(sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance()