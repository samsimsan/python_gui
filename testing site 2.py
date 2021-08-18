from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class mywindow(QMainWindow):            # a class is used to link the functions together
    def __init(self):
        super(mywindow,self).__init__() #don't know this super thing, just paste this
        self.initUI()
        
    def initUI(self):                   #this is where all the stuffs of the window are gonna be placed 
        #inside the class all variables we make needs to be addressed as 'self.variable'
        # adding a label
        self.label = QtWidgets.QLabel(self)    # create a label named 'label' inside 'self'
        self.label.setText("this is my label") # write the text for the label
        self.label.move(10, 10)                # to move the label within the 'win' relative to top left corner
    
        #adding a button
        self.b1 = QtWidgets.QPushButton(self)     # create a button called b1 inside self
        self.b1.setText('click me here!')         # adding text to the button
        self.b1.clicked.connect(clicking_button)  # when the 'b1' is clicked it 'connects' to a function 'clicking_button'
        # in the connect call, DON'T USE THE () FOR THE FUNCTION
        self.b1.move(100, 100)                    # moving the button
        
        
        
        
        
        
        
        

def clicking_button():   # a function which will print a statement when called
    print('the button clicked') 

def windows():
    app = QApplication(sys.argv) # create the appli
    win = QMainWindow()# create the window
    win.setGeometry(100, 100, 500, 500)# set the pos and size of the windw
    win.setWindowTitle('my window testing') # give the window a name
    
    
    
    win.show() # to show the window
    sys.exit(app.exec_()) # to exit the appli cleanly 
windows() # calling the function 