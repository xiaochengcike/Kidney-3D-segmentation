from os import path

slice_number = 140

#Ustawienie ścierzki do folderu z DICOMAMI
program_folder = path.dirname(__file__)
image_folder = path.join(program_folder, 'KidneyDICOMS')
jpg_folder = path.join(program_folder, 'KidneyJPG')

#Inicjalizacja procesu wczytywania z pliku
file_to_read_start = "00010"
file_to_read_mid = "000"
file_to_read_end = ".dcm"
file_to_read_end_jpg = ".png"

#inicjalizacja pustej listy na obrazy
images = []
images_jpg = []