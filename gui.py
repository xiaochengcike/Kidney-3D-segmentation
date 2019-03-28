from load_image import *
from histogram import *
from settings import SLICE_NUMBER
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

counter = 0

class Window(Tk):

    def __init__(self):
        super(Window, self).__init__()
        self.title("Kidney 3D segmentation")
        self.minsize(640, 400)
        LoadImg()
        self.matplotCanvas()

    def matplotCanvas(self):
        #self.slice_number = SLICE_NUMBER
        fig = Figure(figsize=(10, 6), dpi=100)
        sbplt = fig.add_subplot(111)
        # if self.slice_number != None:
        #     sbplt.imshow(images_jpg[self.slice_number], cmap=plt.cm.gist_gray)

        scroll_bar = Scrollbar(self, orient=VERTICAL)
        scroll_bar.pack(side=RIGHT, fill=Y)

        guise_img_list = Listbox(self, yscrollcommand=scroll_bar.set, height=30)
        for i in range(len(images_jpg)):
            guise_img_list.insert(END, "Przekrój nr. " + str(i))
        guise_img_list.pack(side=RIGHT)
        scroll_bar.config(command=guise_img_list.yview)

        self.current_place = guise_img_list.curselection()
        if len(self.current_place) > 0:
            sbplt.imshow(images_jpg[self.slice_number], cmap=plt.cm.gist_gray)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side=RIGHT)
        canvas.draw()

        # self.current_place = guise_img_list.curselection()

        mainloop()

    def update(self):
        counter = len(self.current_place)
        self.slice_number = int(self.current_place[counter - 1])
        return self.slice_number
