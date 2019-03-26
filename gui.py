from appJar import gui
from load_image import *
from histogram import *
from settings import slice_number
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from matplotlib import pyplot as plt


def LoadOnScreen():
    LoadImg()

LoadImg()

window = tk.Tk()
figure_slice = plt.Figure(figsize=(6, 5), dpi=100)
bar_slice = FigureCanvasTkAgg(figure_slice, window)
bar_slice.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
plt.imshow(images[slice_number].pixel_array, cmap=plt.cm.gist_gray)
window.mainloop()

# LoadImg()
# img_data = images_jpg[slice_number].data
# window = gui('Kidney 3D segmentation', '1024x768')
# window.setBg('black')
# window.addButton('Load images', LoadOnScreen)
# #window.addPlotFig('d', ShowHistogram())
# fig = window.addPlotFig("du")