import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        # setting title
        root.title("City Data")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.ButtonM = tk.Button(root)
        self.ButtonM["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.ButtonM["font"] = ft
        self.ButtonM["fg"] = "#000000"
        self.ButtonM["justify"] = "center"
        self.ButtonM["text"] = "Load File"
        self.ButtonM.place(x=70, y=50, width=70, height=25)
        self.ButtonM["command"] = self.__GButton_450_command

        self.List01 = ttk.Combobox(root)
        self.List01.place(x=350, y=50, width=80, height=25)
        self.List01.bind("<<ComboboxSelected>>", self.__comboBoxCb)

        self.SelectCityLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.SelectCityLabel["font"] = ft
        self.SelectCityLabel["fg"] = "#333333"
        self.SelectCityLabel["justify"] = "center"
        self.SelectCityLabel["text"] = "Choose data file               Select city"
        self.SelectCityLabel.place(x=150, y=50, width=200, height=25)

        # these canvases are broken, fix them
        self.__GLineEdit_517 = tk.Canvas(root)
        self.__GLineEdit_517.place(x=50, y=130, width=234, height=140)

        self.__GLineEdit_985 = tk.Canvas(root)
        self.__GLineEdit_985.place(x=310, y=130, width=239, height=139)

        self.__GLineEdit_392 = tk.Canvas(root)
        self.__GLineEdit_392.place(x=50, y=290, width=233, height=157)

        self.__GLineEdit_700 = tk.Canvas(root)
        self.__GLineEdit_700.place(x=310, y=290, width=234, height=158)

    def __GButton_450_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.List01['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
        except:
            # quick and dirty, desired behavior would be to show a notification pop up that says
            # "nope!"
            print('nope')

    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def __comboBoxCb(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.List01.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(self.__GLineEdit_392.winfo_width, self.__GLineEdit_392.winfo_height), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc['KWH JANUARY 2010'], 12)].mean().plot.bar(ax=ax1)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
