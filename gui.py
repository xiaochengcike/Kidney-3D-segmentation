from appJar import gui
from load_image import *
from histogram import *
from settings import slice_number
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Window(Tk):

    def __init__(self):
        super(Window, self).__init__()
        self.title("Kidney 3D segmentation")
        self.minsize(640, 400)

        LoadImg()

        self.matplotCanvas()
        mainloop()

    def matplotCanvas(self):
        fig = Figure(figsize=(5, 5), dpi=100)
        sbplt = fig.add_subplot(111)
        #sbplt.plot([1, 2, 3, 4], [5, 6, 7, 8])
        sbplt.imshow(images_jpg[slice_number], cmap=plt.cm.gist_gray)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

