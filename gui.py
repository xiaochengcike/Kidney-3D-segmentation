from load_image import *
from histogram import *
from settings import slice_number
from tkinter import *
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

    def matplotCanvas(self):
        fig = Figure(figsize=(10, 6), dpi=100)
        sbplt = fig.add_subplot(111)
        sbplt.imshow(images_jpg[slice_number], cmap=plt.cm.gist_gray)

        scroll_bar = Scrollbar(self, orient=VERTICAL)
        scroll_bar.pack(side=RIGHT, fill=Y)

        guise_img_list = Listbox(self, yscrollcommand=scroll_bar.set, height=30)
        for i in range(len(images_jpg)):
            guise_img_list.insert(END, "Przekrój nr. " + str(i))
        guise_img_list.pack(side=RIGHT)
        scroll_bar.config(command=guise_img_list.yview)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side=RIGHT)
        canvas.draw()

        current_place = guise_img_list.curselection()

        mainloop()