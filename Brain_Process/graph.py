import pyqtgraph as pg
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Temperature vs time plot
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        #time sb x temperature sb y mirip matplotlib
        self.plot_graph.setBackground("k") #Set bg color :  (default black) or bisa pakek kode RGB
        ''' "b"	Blue
        "c"	Cian
        "d"	Grey
        "g"	Green
        "k"	Black
        "m"	Magenta
        "r"	Red 
        "w"	White
        "y"	Yellow '''
        self.plot_graph.setTitle("Temperature vs Time", color="b", size="20pt")
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
        self.plot_graph.plot(time, temperature)

app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()