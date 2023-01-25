from concurrent.futures import thread
from turtle import heading
import customtkinter
from doctest import master
from logging import PlaceHolder
import tkinter
import time
from tkinter import ttk
import tkinter.messagebox
import customtkinter
from matplotlib.ft2font import HORIZONTAL
from matplotlib.pyplot import cla
from pip import main
from pyscreeze import center
from sqlalchemy import column, true
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib import animation
from matplotlib import style
import os
from PIL import Image, ImageTk
from FINAL_SCRAPPING import scrapData,startScraping,Scrapping
import threading
PATH = os.path.dirname(os.path.realpath(__file__))
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):
    
    def __init__(self):
        # threading.Thread.__init__(self)
        super().__init__()
        self.currentFrame="None";
        self.title("LIBRARY MANAGMENT SYSTEM")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()  # HEIGHT and WIDTH of SCREEN
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.state('zoomed')
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=600)
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=600)
        # =====================================Grids=========================================================================
        self.scrapingImg = self.load_image("/Resources/Images/scraping.png", (50,50))
        self.bookImg = self.load_image("/Resources/Images/book.png", (60,38))
        self.exitImg = self.load_image("/Resources/Images/exit.png", (50,50))
        self.sideBar = customtkinter.CTkFrame(master=self,corner_radius=0, fg_color=("#686868", "#000000"), border_color=('#FFFFFF', '#FFFFFF'),highlightbackground="black", highlightthickness=2)
        self.sideBar.grid(row=0, column=0,rowspan=2, sticky="wens")
        self.heading = customtkinter.CTkFrame(master=self,width=150,fg_color=("#686868", "#000000"),corner_radius=0,highlightbackground="black", highlightthickness=2)
        self.heading.grid(row=0, column=1, sticky="wens", padx=1, pady=1)
        self.mainArea1 = customtkinter.CTkFrame(master=self,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
        self.mainArea1.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
        #################### SIDE Bar Menu ################
        self.sideBar.grid_rowconfigure(0, minsize=10)
        self.sideBar.grid_rowconfigure(5, weight=1)
        self.sideBar.grid_rowconfigure(8, minsize=20)
        self.sideBar.grid_rowconfigure(11, minsize=10)
        
        self.txtLogo = customtkinter.CTkLabel(master=self.sideBar,text="L M S",text_font=("Century Gothic", 48))
        self.txtLogo.grid(row=1, column=0, pady=0, padx=0,sticky='s')

        self.menubtnScrap = customtkinter.CTkButton(master=self.sideBar,width=170, height=60,image=self.scrapingImg,text="SCRAP DATA",command=self.switchtoScrapping,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.menubtnScrap.grid(row=2, column=0, pady=10, padx=20,sticky='s')
        # #023246
        self.menubtndashBoard = customtkinter.CTkButton(master=self.sideBar,width=170, height=60,image=self.bookImg,text="DASHBOARD",command=self.switchtoDashBoard,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.menubtndashBoard.grid(row=3, column=0, pady=10, padx=20,sticky='s')
        self.menubtnExit = customtkinter.CTkButton(master=self.sideBar,width=170, height=60,image=self.exitImg,text="EXIT",command=self.close,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.menubtnExit.grid(row=4, column=0, pady=10, padx=20,sticky='s')

        self.lblMode = customtkinter.CTkLabel(master=self.sideBar, text="CHANGE THEME",text_font=("Century Gothic", 11))
        self.lblMode.grid(row=9, column=0, pady=0, padx=20, sticky="w")
        self.cmbTheme = customtkinter.CTkOptionMenu(master=self.sideBar,values=["LIGHT", "DARK", "SYSTEM"],command=self.change_appearance_mode,text_font=("Century Gothic", 11))
        self.cmbTheme.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        
        self.heading.grid_columnconfigure(0, weight=1)
        self.lblHeading = customtkinter.CTkLabel(master=self.heading, text="WELCOME",text_font=("Century Gothic", 48))
        self.lblHeading.grid(column=0, row=0)
        self.after(2,self.scrapData1)
        ########################################################### Methods ######################################################
    def change_appearance_mode(self,new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def clearFrame(self):
        for widget in self.mainArea1.winfo_children():
            widget.destroy()
    def load_image(self, path, image_size):
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size[0], image_size[1])))
    def btn(self):
        return
    def switchtoDashBoard(self):
        heading="DASHBOARD"
        if(self.currentFrame!=heading):
            self.clearFrame()
            self.currentFrame=heading
            self.lblHeading.config(text = heading)
            self.DashBoardWindow = customtkinter.CTkFrame(master=self,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
            self.DashBoardWindow.grid_columnconfigure(0, weight=1)
            self.DashBoardWindow.grid_columnconfigure(1, weight=10)
            self.DashBoardWindow.grid_rowconfigure(0, weight=1)
            self.DashBoardWindow.grid_rowconfigure(1, weight=1)
            self.SortingFrame=customtkinter.CTkFrame(master=self.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.SortingFrame.grid(row=0, column=0,rowspan=2, sticky="wens",padx=10,pady=10)
            self.SearchingFrame=customtkinter.CTkFrame(master=self.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.SearchingFrame.grid(row=0, column=1, sticky="wens",padx=10,pady=10)
            self.TableFrame=customtkinter.CTkFrame(master=self.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.TableFrame.grid(row=1, column=1, sticky="wens",padx=10,pady=10)
            self.DashBoardWindow.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
                        ################# Sorting Frame  ################
            self.SortingFrame.grid_columnconfigure(0, weight=1)
            self.SortingFrame.grid_columnconfigure(1, weight=1)
            self.SortingFrame.grid_rowconfigure(0, weight=1)
            self.SortingFrame.grid_rowconfigure(1, weight=1)
            self.SortingFrame.grid_rowconfigure(2, weight=1)
            self.SortingFrame.grid_rowconfigure(3, weight=1)
            self.SortingFrame.grid_rowconfigure(4, weight=1)
            self.SortingFrame.grid_rowconfigure(5, weight=15)
            self.SortingFrame.grid_rowconfigure(6, weight=15)
            self.lblSorting = customtkinter.CTkLabel(master=self.SortingFrame, text="Multi-Level Sorting",text_font=("Century Gothic", 16))
            self.lblSorting.grid(column=0, row=0,sticky="e")
            Columns = ["Option 1", "Option 2", "Option 3", "Option 4"]
            valueColumn = tkinter.StringVar(self.SortingFrame)
            valueColumn.set("Select a Column")
            Algorithms = ["Option 1", "Option 2", "Option 3", "Option 4"]
            valueAlgorithm = tkinter.StringVar(self.SortingFrame)
            valueAlgorithm.set("Select an Algorithm")
            Order = ["Option 1", "Option 2", "Option 3", "Option 4"]
            valueOrder = tkinter.StringVar(self.SortingFrame)
            valueOrder.set("Select Order")
            self.selectColumn = customtkinter.CTkOptionMenu(master=self.SortingFrame,width=200,values=Columns,variable=valueColumn)
            self.selectColumn.grid(column=0,row=1,sticky='e')
            self.selectAlgorithm = customtkinter.CTkOptionMenu(master=self.SortingFrame,width=200,values=Algorithms,variable=valueAlgorithm)
            self.selectAlgorithm.grid(column=0,row=2,sticky='e')
            self.selectOrder = customtkinter.CTkOptionMenu(master=self.SortingFrame,width=200,values=Order,variable=valueOrder)
            self.selectOrder.grid(column=0,row=3,sticky='e')
            self.btnClearSortingFilters = customtkinter.CTkButton(master=self.SortingFrame,text="CLEAR",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
            self.btnClearSortingFilters.grid(row=4, column=0,columnspan=2,sticky="w",padx=5)
            self.btnStartSorting = customtkinter.CTkButton(master=self.SortingFrame,text="START",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
            self.btnStartSorting.grid(row=4, column=0,sticky="e",columnspan=2,padx=5)
            lstofAllLevels=["pa","pb"]
            rows = len(lstofAllLevels)
            self.treeOfAllLevels = ttk.Treeview(self.SortingFrame, columns=(1, 2), height=rows, show="headings")
            self.treeOfAllLevels.grid(row=5, column=0,columnspan=2,sticky="nesw",pady=5)
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
            style.map("Treeview",background=[('selected', 'green')])
            self.treeOfAllLevels.heading("#1", text="LEVEL", anchor='center')
            self.treeOfAllLevels.heading("#2", text="DETAILS", anchor='center')
            self.treeOfAllLevels.column("#1", width=150, minwidth=25, anchor='w')
            self.treeOfAllLevels.column("#2", width=150, minwidth=25, anchor='center')
            scroll = ttk.Scrollbar(self.SortingFrame, orient="vertical", command=self.treeOfAllLevels.yview)
            self.treeOfAllLevels.configure(yscrollcommand=scroll.set)
            lstofAllTimes=["pa","pb"]
            rows = len(lstofAllTimes)
            self.treeOfLevelsTimes = ttk.Treeview(self.SortingFrame, columns=(1, 2), height=rows, show="headings")
            self.treeOfLevelsTimes.grid(row=6, column=0,columnspan=2,sticky="nesw",pady=5)
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
            style.map("Treeview",background=[('selected', 'green')])
            self.treeOfLevelsTimes.heading("#1", text="LEVEL", anchor='center')
            self.treeOfLevelsTimes.heading("#2", text="Time", anchor='center')
            self.treeOfLevelsTimes.column("#1", width=150, minwidth=25, anchor='w')
            self.treeOfLevelsTimes.column("#2", width=150, minwidth=25, anchor='center')
            scroll = ttk.Scrollbar(self.SortingFrame, orient="vertical", command=self.treeOfLevelsTimes.yview)
            self.treeOfLevelsTimes.configure(yscrollcommand=scroll.set)
                        ################# Searching Frame  ################
            self.SearchingFrame.grid_columnconfigure(0, weight=1)
            self.SearchingFrame.grid_columnconfigure(1, weight=1)
            self.SearchingFrame.grid_columnconfigure(2, weight=1)
            self.SearchingFrame.grid_rowconfigure(0, weight=1)
            self.SearchingFrame.grid_rowconfigure(1, weight=1)
            self.SearchingFrame.grid_rowconfigure(2, weight=1)
            self.SearchingFrame.grid_rowconfigure(3, weight=1)
            Operators = ["Option 1", "Option 2", "Option 3", "Option 4"]
            valueOperator = tkinter.StringVar(self.SearchingFrame)
            valueOperator.set("Select Operator")
            self.lblSorting = customtkinter.CTkLabel(master=self.SearchingFrame, text="Multi-Level Searching",text_font=("Century Gothic", 16))
            self.lblSorting.grid(column=0, row=0,columnspan=3,sticky="nesw")
            self.search1 = customtkinter.CTkEntry(master=self.SearchingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="Harry Potter")
            self.search1.grid(column=0, row=1,pady=0,padx=0,sticky="w")
            self.selectOperater = customtkinter.CTkOptionMenu(master=self.SearchingFrame,width=200,values=Operators,variable=valueOperator)
            self.selectOperater.grid(column=0,row=2,sticky='w')
            self.search2 = customtkinter.CTkEntry(master=self.SearchingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="philospher's stone")
            self.search2.grid(column=0, row=3,pady=0,padx=0,sticky="w")
            self.selectOperater = customtkinter.CTkOptionMenu(master=self.SearchingFrame,width=200,values=Operators,variable=valueOperator)
            self.selectOperater.grid(column=1,row=1,sticky='w')
            self.selectOperater = customtkinter.CTkOptionMenu(master=self.SearchingFrame,width=200,values=Operators,variable=valueOperator)
            self.selectOperater.grid(column=1,row=2,sticky='w')
            self.selectOperater = customtkinter.CTkOptionMenu(master=self.SearchingFrame,width=200,values=Operators,variable=valueOperator)
            self.selectOperater.grid(column=1,row=3,sticky='w')
            # self.treeOfBooks = ttk.Treeview(self.TableFrame, columns=(1, 5), height=rows, show="headings")
            # self.treeOfBooks.grid(row=0, column=0,sticky="nesw")
            # style = ttk.Style()
            # style.theme_use("clam")
            # style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
            # style.map("Treeview",background=[('selected', 'green')])
            # self.treeOfBooks.heading("#1", text="TITLE", anchor='center')
            # self.treeOfBooks.heading("#2", text="AUTHOR(S)", anchor='center')
            # self.treeOfBooks.heading("#3", text="LANGUAGE", anchor='center')
            # self.treeOfBooks.heading("#4", text="PUBLISH YEAR", anchor='center')
            # self.treeOfBooks.heading("#5", text="PUBLISHER)", anchor='center')
            # self.treeOfBooks.heading("#6", text="FILE FORMAT", anchor='center')
            # self.treeOfBooks.heading("#7", text="FILE SIZE", anchor='center')
            # self.treeOfBooks.column("#1", width=150, minwidth=25, anchor='w')
            # self.treeOfBooks.column("#2", width=150, minwidth=25, anchor='center')
            # self.treeOfBooks.column("#3", width=150, minwidth=25, anchor='center')
            # self.treeOfBooks.column("#4", width=150, minwidth=25, anchor='center')
            # self.treeOfBooks.column("#5", width=150, minwidth=25, anchor='center')
            # self.treeOfBooks.column("#6", width=150, minwidth=25, anchor='center')
            # self.treeOfBooks.column("#7", width=150, minwidth=25, anchor='center')
            # scroll = ttk.Scrollbar(self.scrapingFrame, orient="vertical", command=self.treeOfBooks.yview)
            # self.treeOfBooks.configure(yscrollcommand=scroll.set)

    def switchtoScrapping(self):
         heading="SCRAPPING"
         if(self.currentFrame!=heading):
            self.clearFrame()
            self.currentFrame=heading
            self.ScrappingWindow = customtkinter.CTkFrame(master=self,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
            self.ScrappingWindow.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
            self.ScrappingWindow.grid_columnconfigure(0, weight=1)
            self.ScrappingWindow.grid_columnconfigure(1, weight=5)
            self.ScrappingWindow.grid_rowconfigure(0, weight=5)
            self.ScrappingWindow.grid_rowconfigure(1, weight=1)
            self.scrapingFrame=customtkinter.CTkFrame(master=self.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.scrapingFrame.grid(row=0, column=0, sticky="wens",padx=10,pady=10)
            self.statsFrame=customtkinter.CTkFrame(master=self.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.statsFrame.grid(row=0, column=1, sticky="wens",padx=10,pady=10)
            self.progessFrame=customtkinter.CTkFrame(master=self.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.progessFrame.grid(row=1, column=0,columnspan=2, sticky="wens",padx=10,pady=10)
                            ################# Scraping Frame  ################
            self.scrapingFrame.grid_columnconfigure(0, weight=1)
            self.scrapingFrame.grid_columnconfigure(1, weight=1)
            self.scrapingFrame.grid_rowconfigure(0, weight=1)
            self.scrapingFrame.grid_rowconfigure(1, weight=1)
            self.scrapingFrame.grid_rowconfigure(2, weight=1)
            self.scrapingFrame.grid_rowconfigure(3, weight=1)
            self.scrapingFrame.grid_rowconfigure(4, weight=30)
            self.lblScrapWebsite = customtkinter.CTkLabel(master=self.scrapingFrame, text="SCRAP TAB",text_font=("Century Gothic", 16))
            self.lblScrapWebsite.grid(column=0, row=0,sticky="nesw",columnspan=2)
            self.lblScrapWebsite = customtkinter.CTkLabel(master=self.scrapingFrame, text="SCRAP FROM URL:",text_font=("Century Gothic", 12))
            self.lblScrapWebsite.grid(column=0, row=1,sticky="w")
            self.entURl = customtkinter.CTkEntry(master=self.scrapingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="example https://archive.org/")
            self.entURl.grid(column=1, row=1,pady=0,padx=0,sticky="w")
            self.btnStart1 = customtkinter.CTkButton(master=self.scrapingFrame,text="Start",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 12))
            self.btnStart1.grid(row=2, column=1,sticky='w')
            self.lblScrapPrecoded = customtkinter.CTkLabel(master=self.scrapingFrame, text="SCRAP FROM  PRE-CODED WEBSITE:",text_font=("Century Gothic", 12))
            self.lblScrapPrecoded.grid(column=0, row=3,sticky="w") 
            self.btnStart2 = customtkinter.CTkButton(master=self.scrapingFrame,text="Start",command=startScraping,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 12))
            self.btnStart2.grid(row=3, column=1,sticky="w")
            lstFailAttribs=["pa","pb"]
            rows = len(lstFailAttribs)
            self.treeOfFailAttributes = ttk.Treeview(self.scrapingFrame, columns=(1, 2), height=rows, show="headings")
            self.treeOfFailAttributes.grid(row=4, column=0,columnspan=2,sticky="nesw")
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
            style.map("Treeview",background=[('selected', 'green')])
            self.treeOfFailAttributes.heading("#1", text="ATTRIBUTES", anchor='center')
            self.treeOfFailAttributes.heading("#2", text="STATUS", anchor='center')
            self.treeOfFailAttributes.column("#1", width=150, minwidth=25, anchor='w')
            self.treeOfFailAttributes.column("#2", width=150, minwidth=25, anchor='center')
            scroll = ttk.Scrollbar(self.scrapingFrame, orient="vertical", command=self.treeOfFailAttributes.yview)
            self.treeOfFailAttributes.configure(yscrollcommand=scroll.set)
                            ################# Progress Bar Frame  ################
            self.progessFrame.grid_columnconfigure(0, weight=1)
            self.progessFrame.grid_columnconfigure(1, weight=1)
            self.progessFrame.grid_rowconfigure(0, weight=1)
            self.progessFrame.grid_rowconfigure(1, weight=1)
            self.progessFrame.grid_rowconfigure(2, weight=1)
            self.PBscrap=customtkinter.CTkProgressBar(self.progessFrame,orient="horizontal")
            self.PBscrap.grid(row=0,column=0,columnspan=2,sticky="ew", padx=15, pady=15)
            self.btnPauseScrapping = customtkinter.CTkButton(master=self.progessFrame,text="PAUSE",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 16))
            self.btnPauseScrapping.grid(row=1, column=0,sticky="e")
            self.btnEndScraping = customtkinter.CTkButton(master=self.progessFrame,text="END",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 16))
            self.btnEndScraping.grid(row=1, column=1,sticky="w")
    def close(self):
       #win.destroy()
        self.quit()
    def scrapData1(self):
        scrapData()

if __name__ == "__main__":
    app = App()
    app.mainloop()
    

