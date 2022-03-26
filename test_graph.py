import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import numpy as np

title = "Data from Arduino"

x = [1, 2, 3]
y = [1, 2, 3]

   # for i in range(0, 10):
#        x[i] = i
 #       y[i] = i
        

plt = pg.plot()
plt.showGrid(x = True, y = True) # vals só dif de 0 a oartir do inhdice 2
plt.addLegend()
plt.setLabel('left', 'Value', units='V')
plt.setLabel('bottom', 'Time', units='s')
plt.setXRange(0, 4)
plt.setYRange(0, 4)
plt.setWindowTitle(title)

line = plt.plot(x, y, pen='b', symbol='x', symbolPen='b', symbolBrush=0.2, name='red')

if __name__ == '__main__':
    import sys
    
    if(sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance()