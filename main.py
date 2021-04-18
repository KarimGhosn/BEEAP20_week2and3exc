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

        # Loading csv file button settings
        self.ButtonM = tk.Button(root)
        self.ButtonM["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.ButtonM["font"] = ft
        self.ButtonM["fg"] = "#000000"
        self.ButtonM["justify"] = "center"
        self.ButtonM["text"] = "Load File"
        self.ButtonM.place(x=70, y=50, width=70, height=25)
        self.ButtonM["command"] = self.__GButton_450_command

        # ComboBox (List) settings
        self.List01 = ttk.Combobox(root)
        self.List01.place(x=350, y=50, width=200, height=25)
        self.List01.bind("<<ComboboxSelected>>", self.__comboBoxCb)

        # Label frame settings
        self.SelectCityLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.SelectCityLabel["font"] = ft
        self.SelectCityLabel["fg"] = "#333333"
        self.SelectCityLabel["justify"] = "center"
        self.SelectCityLabel["text"] = "Choose data file               Select city"
        self.SelectCityLabel.place(x=150, y=50, width=200, height=25)

        # Canvas

        self.Canvas1 = tk.Canvas(root)
        self.Canvas1.place(x=60, y=100, width=234, height=140)

        self.Canvas2 = tk.Canvas(root)
        self.Canvas2.place(x=300, y=100, width=239, height=139)

        self.Canvas3 = tk.Canvas(root)
        self.Canvas3.place(x=60, y=300, width=233, height=157)

        self.Canvas4 = tk.Canvas(root)
        self.Canvas4.place(x=300, y=300, width=234, height=158)

        

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
        self.__SubDataFrame = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.List01.get()]

        # Figure 1 configuration
        FigureA = plt.figure(dpi=50)
        AxisA = FigureA.add_subplot(111)
        GraphA = FigureCanvasTkAgg(FigureA, root)
        GraphA.get_tk_widget().place(x=40, y=120, width=250, height=180)                             # Creating the bar graph (Dimensions of the bar graph)
        plt.xticks(rotation = 45)                         
        CityIndex = (self.__SubDataFrame.columns.get_loc('KWH MAY 2010'))                                   # Starting first bar from January                                                                   # Having the names sideway under the bars on the x-axis
        print(CityIndex)
        DataFrame = self.__SubDataFrame.iloc[:, range(CityIndex, CityIndex+12)].mean().plot.bar(ax=AxisA)   # Moving from 1st month to 12th month gradually bar after the other
        AxisA.set_title('Mean (KWH)')                                            

        # Figure 2 configuration
        FigureB = plt.figure(dpi=50)
        AxisB = FigureB.add_subplot(111)
        GraphB = FigureCanvasTkAgg(FigureB, root)
        GraphB.get_tk_widget().place(x=300, y=120, width=250, height=180)
        plt.xticks(rotation = 45)
        CityIndex = (self.__SubDataFrame.columns.get_loc('THERM MARCH 2010'))
        print(CityIndex)
        DataFrame = self.__SubDataFrame.iloc[:, range(CityIndex, CityIndex+12)].mean().plot.bar(ax=AxisB)
        AxisB.set_title('Mean (THERM)')

        # Figure 3 configuration
        FigureC = plt.figure(dpi=50)
        AxisC = FigureC.add_subplot(111)
        GraphC = FigureCanvasTkAgg(FigureC, root)
        GraphC.get_tk_widget().place(x=40, y=315, width=250, height=180)
        plt.xticks(rotation = 45)
        CityIndex = (self.__SubDataFrame.columns.get_loc('KWH JANUARY 2010'))
        print(CityIndex)
        DataFrame = self.__SubDataFrame.iloc[:, range(CityIndex, CityIndex+12)].max().plot.bar(ax=AxisC)
        AxisC.set_title('Max value (KWH)')

        # Figure 4 configuration
        FigureD = plt.figure(dpi=50)
        AxisD = FigureD.add_subplot(111)
        GraphD = FigureCanvasTkAgg(FigureD, root)
        GraphD.get_tk_widget().place(x=300, y=315, width=250, height=180)
        plt.xticks(rotation = 45)
        CityIndex = (self.__SubDataFrame.columns.get_loc('THERM FEBRUARY 2010'))
        print(CityIndex)
        DataFrame = self.__SubDataFrame.iloc[:, range(CityIndex, CityIndex+12)].max().plot.bar(ax=AxisD)
        AxisD.set_title('Max value (THERM)')



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
