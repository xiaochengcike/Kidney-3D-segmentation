from settings import *
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import pydicom as dicom


def LoadImg():

    #Wczytanie plików do listy
    i = 1
    while(i < 190):
        dicom_number = str(i)

        if(i < 10):
            file_to_read_mid = "00" + dicom_number

        elif(i < 100):
            file_to_read_mid = "0" + dicom_number

        elif(i > 100):
            file_to_read_mid = dicom_number

        image_data = file_to_read_start + file_to_read_mid + file_to_read_end
        image_data_jpg = file_to_read_start + file_to_read_mid + file_to_read_end_jpg

        image = dicom.dcmread(path.join(image_folder, image_data))
        images.append(image)

        #image_jpg = Image.open(path.join(jpg_folder, image_data_jpg))
        image_jpg = mpimg.imread(path.join(jpg_folder, image_data_jpg))
        images_jpg.append(image_jpg)
        i += 1

def ShowImg():
    #Utworzenie rysunku z obrazem
    plt.figure()
    plt.title('Przekrój:')
    plt.imshow(images[slice_number].pixel_array, cmap=plt.cm.gist_gray)
    plt.show()

    #Utworzenie rysunku po konwersji na PNG
    # plt.figure()
    # plt.title('Przekrój po konwersji do PNG')
    # plt.imshow(images_jpg[slice_number], cmap=plt.cm.gist_gray)
    # plt.show()

