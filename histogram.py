from settings import *
from matplotlib import pyplot as plt

def ShowHistogram():
    #plt.figure()
    histogram1 = plt.hist(images_jpg[slice_number].flatten(), bins=50, color='c')
    # plt.title('Histogram')
    # plt.xlabel('Jasność pixeli')
    # plt.ylabel('Ilość pixeli')
    plt.show()

    return histogram1

# zmienna histogram1 jest potrzebna do
# wyliczenia różnicy histogramów. NIE TYKAć
