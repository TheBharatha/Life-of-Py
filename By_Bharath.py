"""
Python program to import files of different format and display them
Written by Bharath Kumar Shivakumar
"""
import pyabf
import matplotlib.pyplot as plt
import matplotlib.image as myimg
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import csv
import numpy as np
import pandas as pd

##This is the function that takes in image file as argument
def pics(img_file):
    try:
        picture = Image.open(open(img_file, 'rb'))
        print(type(picture))
        return(picture.show())
    except:
        messagebox.showerror('Operation failed', 'Unbale to display the image; Invalid file or no file selected')

##This is the function that accepts binary file as argument
def abf(binary_file):
    try:
        date_time = (type(binary_file.abfDateTime), binary_file.abfDateTime)
        date_time_string = (type(binary_file.abfDateTimeString), binary_file.abfDateTimeString)
        both = str(date_time) + ' \n ' + str(date_time_string)
        messagebox.showinfo('Date time class  type from binary file', both)
        return(date_time, date_time_string)
    except:
        messagebox.showerror('Operation failed', 'Unbale to open the binary file; Invalid file or no file selected')

##This is the function that takes in csv file as argument
def csV(comma_file):
    try:
        with open(comma_file, 'r') as csvFile:
            nuclei = list(csv.reader(csvFile, delimiter = ";"))
            nuclei = np.array(nuclei[1:], dtype = np.str)
        csvShape = 'Number of rows in the csv file selected is: ' + str(nuclei.shape)
        return(messagebox.showinfo('Rows in the file: ', csvShape))
    except:
        messagebox.showerror('Operation failed', 'Unbale to process the csv file; Invalid file or no file selected')

##This is the function that takes Excel file as argument
def xlsx(xl_file):
    try:
        excel = pd.read_excel(open(xl_file, 'rb'), sheet_name = 'data')
        file_shape = 'The selected excel file has the shape of: ' + str(excel.shape)
        return(messagebox.showinfo("Dimension of the excel file",file_shape))
    except:
        messagebox.showerror('Operation failed', 'Unbale to process the excel file; Invalid file or no file selected')

#Driving code
if __name__ == "__main__":
    #.withdraw() will stop an unnecessary empty GUI from appearing on the screen
    Tk().withdraw()
    #Guided steps to select image file
    messagebox.showinfo('Image selection!', '1 of 4 files. You will be asked to select a JPG file with .jpg file extension')
    img_file = askopenfilename(title = 'Select a JPG file',filetypes = [("JPG file","*.jpg")])
    #Guided steps to select binary file
    messagebox.showinfo('Binary file selection!', '2 of 4 files. You will be asked to select a Binary file with .abf file extension')
    bin_file = askopenfilename(title = 'Select a Binary file',filetypes = [("ABF file","*.abf")])
    #Making use of ABF package to read the binary file
    binary_file = pyabf.ABF(bin_file)
    #Guided steps to select csv file
    messagebox.showinfo('CSV file selection!', '3 of 4 files. You will be asked to select a csv file with .csv file extension')
    comma_file = askopenfilename(title = 'Select a csv file',filetypes = [("csv file","*.csv")])
    #Guided steps to select csv file
    messagebox.showinfo('xlsx file selection!', '4 of 4 files. You will be asked to select a xlsx file with .xlsx file extension')
    xl_file = askopenfilename(title = 'Select a Excel file',filetypes = [("xlsx file","*.xlsx")])
    
    #Passing the image file as argument
    pics(img_file)
    #Passing Binary file as argument
    abf(binary_file)
    #Passing Binary file as argument
    csV(comma_file)
    #Passing Excel file as argument
    xlsx(xl_file)