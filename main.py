from load_image import *
from histogram import *
#from gui import *
import gui

##################################
######Konwersja DICOM na PNG######
##################################
Convert_DICOMS = False           #
if Convert_DICOMS == True:       #
    from Convert_to_JPG import * #
##################################

program = gui.Window()
while True:
    program.matplotCanvas()
    program.update()

###########
# LoadImg()
# ShowImg()
# ShowHistogram()

#gui.window.go()

#*** NUMER PIERWSZEGO PRZEKROJU***
#00010001.dcm