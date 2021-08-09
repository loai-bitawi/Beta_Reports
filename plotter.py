from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class Ui_Plotter(object):

    def setupUi(self, OtherWindow,d1,d2,plot_type):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(809, 609)
        OtherWindow.setGeometry(QtCore.QRect(500,200,809,609))
        self.centralwidget=QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        layout = QtWidgets.QVBoxLayout(self.centralwidget)        
        static_canvas = FigureCanvas(Figure())
        OtherWindow.addToolBar(NavigationToolbar(static_canvas, OtherWindow))
        OtherWindow.setLayout(layout)
        layout.addWidget(static_canvas)
        self._static_ax = static_canvas.figure.subplots()
        if plot_type =='Bar Chart':
            self._static_ax.bar(d1,d2)
        elif plot_type == 'Line Chart':
            self._static_ax.plot(d1,d2)
        elif plot_type == 'Scatter Plot':
            self._static_ax.scatter(d1,d2)
        elif plot_type == 'Pie Chart':
            self._static_ax.pie(d2,labels=d1,autopct='%1.1f%%')
        elif plot_type == 'Histogram':
            self._static_ax.hist(d1)
        OtherWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)
        
    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Chart Window"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_Plotter()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())