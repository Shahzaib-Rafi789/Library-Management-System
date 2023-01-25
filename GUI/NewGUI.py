from doctest import master
from logging import PlaceHolder
import tkinter
from tkinter import ttk
import tkinter.messagebox
import customtkinter
from matplotlib.ft2font import HORIZONTAL
from pip import main
from pyscreeze import center
from sqlalchemy import column, true
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib import animation
from matplotlib import style
import os
from PIL import Image, ImageTk
########################################## MAIN WINDOW STARTS ##########################################
mainTK = tkinter.Tk()
PATH = os.path.dirname(os.path.realpath(__file__))
fig=None
fig = Figure(figsize = (5, 5),dpi = 100)
plot1 = fig.add_subplot(111)
def btn():
     plot()
def plot():
    y = [i**2 for i in range(101)]
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig, master=mainTK.statsFrame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    fig.destroy()
def scrapingWindow():
    global mainTK
    ################### Main Scrapping Window  ################
    mainTK.ScrappingWindow = customtkinter.CTkFrame(master=mainTK,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
    mainTK.ScrappingWindow.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
    mainTK.ScrappingWindow.grid_columnconfigure(0, weight=1)
    mainTK.ScrappingWindow.grid_columnconfigure(1, weight=5)
    mainTK.ScrappingWindow.grid_rowconfigure(0, weight=5)
    mainTK.ScrappingWindow.grid_rowconfigure(1, weight=1)
    mainTK.scrapingFrame=customtkinter.CTkFrame(master=mainTK.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
    mainTK.scrapingFrame.grid(row=0, column=0, sticky="wens",padx=10,pady=10)
    mainTK.statsFrame=customtkinter.CTkFrame(master=mainTK.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
    mainTK.statsFrame.grid(row=0, column=1, sticky="wens",padx=10,pady=10)
    mainTK.progessFrame=customtkinter.CTkFrame(master=mainTK.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
    mainTK.progessFrame.grid(row=1, column=0,columnspan=2, sticky="wens",padx=10,pady=10)
                    ################# Scraping Frame  ################
    mainTK.scrapingFrame.grid_columnconfigure(0, weight=1)
    mainTK.scrapingFrame.grid_columnconfigure(1, weight=1)
    mainTK.scrapingFrame.grid_rowconfigure(0, weight=1)
    mainTK.scrapingFrame.grid_rowconfigure(1, weight=1)
    mainTK.scrapingFrame.grid_rowconfigure(2, weight=1)
    mainTK.scrapingFrame.grid_rowconfigure(3, weight=1)
    mainTK.scrapingFrame.grid_rowconfigure(4, weight=30)
    mainTK.lblScrapWebsite = customtkinter.CTkLabel(master=mainTK.scrapingFrame, text="SCRAP TAB",text_font=("Century Gothic", 16))
    mainTK.lblScrapWebsite.grid(column=0, row=0,sticky="nesw",columnspan=2)
    mainTK.lblScrapWebsite = customtkinter.CTkLabel(master=mainTK.scrapingFrame, text="SCRAP FROM URL:",text_font=("Century Gothic", 12))
    mainTK.lblScrapWebsite.grid(column=0, row=1,sticky="w")
    mainTK.entURl = customtkinter.CTkEntry(master=mainTK.scrapingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="example https://archive.org/")
    mainTK.entURl.grid(column=1, row=1,pady=0,padx=0,sticky="w")
    mainTK.btnStart1 = customtkinter.CTkButton(master=mainTK.scrapingFrame,text="Start",command=btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 12))
    mainTK.btnStart1.grid(row=2, column=1,sticky='w')
    mainTK.lblScrapPrecoded = customtkinter.CTkLabel(master=mainTK.scrapingFrame, text="SCRAP FROM  PRE-CODED WEBSITE:",text_font=("Century Gothic", 12))
    mainTK.lblScrapPrecoded.grid(column=0, row=3,sticky="w") 
    mainTK.btnStart2 = customtkinter.CTkButton(master=mainTK.scrapingFrame,text="Start",command=btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 12))
    mainTK.btnStart2.grid(row=3, column=1,sticky="w")
    lstFailAttribs=["pa","pb"]
    rows = len(lstFailAttribs)
    mainTK.treeOfFailAttributes = ttk.Treeview(mainTK.scrapingFrame, columns=(1, 2), height=rows, show="headings")
    mainTK.treeOfFailAttributes.grid(row=4, column=0,columnspan=2,sticky="nesw")
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
    style.map("Treeview",background=[('selected', 'green')])
    mainTK.treeOfFailAttributes.heading("#1", text="ATTRIBUTES", anchor='center')
    mainTK.treeOfFailAttributes.heading("#2", text="STATUS", anchor='center')
    mainTK.treeOfFailAttributes.column("#1", width=150, minwidth=25, anchor='w')
    mainTK.treeOfFailAttributes.column("#2", width=150, minwidth=25, anchor='center')
    scroll = ttk.Scrollbar(mainTK.scrapingFrame, orient="vertical", command=mainTK.treeOfFailAttributes.yview)
    mainTK.treeOfFailAttributes.configure(yscrollcommand=scroll.set)
                    ################# Progress Bar Frame  ################
    mainTK.progessFrame.grid_columnconfigure(0, weight=1)
    mainTK.progessFrame.grid_columnconfigure(1, weight=1)
    mainTK.progessFrame.grid_rowconfigure(0, weight=1)
    mainTK.progessFrame.grid_rowconfigure(1, weight=1)
    mainTK.progessFrame.grid_rowconfigure(2, weight=1)
    mainTK.PBscrap=customtkinter.CTkProgressBar(mainTK.progessFrame,orient="horizontal")
    mainTK.PBscrap.grid(row=0,column=0,columnspan=2,sticky="ew", padx=15, pady=15)
    mainTK.btnPauseScrapping = customtkinter.CTkButton(master=mainTK.progessFrame,text="PAUSE",command=btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 16))
    mainTK.btnPauseScrapping.grid(row=1, column=0,sticky="e")
    mainTK.btnEndScraping = customtkinter.CTkButton(master=mainTK.progessFrame,text="END",command=btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 16))
    mainTK.btnEndScraping.grid(row=1, column=1,sticky="w")
def dashBoard():
    ################### Main DashBoard  ################
    global mainTK
    mainTK.DashBoardWindow = customtkinter.CTkFrame(master=mainTK,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
    mainTK.DashBoardWindow.grid_columnconfigure(0, weight=1)
    mainTK.DashBoardWindow.grid_columnconfigure(1, weight=10)
    mainTK.DashBoardWindow.grid_rowconfigure(0, weight=1)
    mainTK.DashBoardWindow.grid_rowconfigure(1, weight=1)
    mainTK.SortingFrame=customtkinter.CTkFrame(master=mainTK.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
    mainTK.SortingFrame.grid(row=0, column=0,rowspan=2, sticky="wens",padx=10,pady=10)
    mainTK.SearchingFrame=customtkinter.CTkFrame(master=mainTK.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
    mainTK.SearchingFrame.grid(row=0, column=1, sticky="wens",padx=10,pady=10)
    mainTK.TableFrame=customtkinter.CTkFrame(master=mainTK.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
    mainTK.TableFrame.grid(row=1, column=1, sticky="wens",padx=10,pady=10)
    mainTK.DashBoardWindow.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
                   ################# Sorting Frame  ################
    mainTK.SortingFrame.grid_columnconfigure(0, weight=1)
    mainTK.SortingFrame.grid_columnconfigure(1, weight=1)
    mainTK.SortingFrame.grid_rowconfigure(0, weight=1)
    mainTK.SortingFrame.grid_rowconfigure(1, weight=1)
    mainTK.SortingFrame.grid_rowconfigure(2, weight=1)
    mainTK.SortingFrame.grid_rowconfigure(3, weight=1)
    mainTK.SortingFrame.grid_rowconfigure(4, weight=1)
    mainTK.SortingFrame.grid_rowconfigure(5, weight=15)
    mainTK.SortingFrame.grid_rowconfigure(6, weight=15)
    mainTK.lblSorting = customtkinter.CTkLabel(master=mainTK.SortingFrame, text="Multi-Level Sorting",text_font=("Century Gothic", 16))
    mainTK.lblSorting.grid(column=0, row=0,sticky="e")
    Columns = ["Option 1", "Option 2", "Option 3", "Option 4"]
    valueColumn = tkinter.StringVar(mainTK.SortingFrame)
    valueColumn.set("Select a Column")
    Algorithms = ["Option 1", "Option 2", "Option 3", "Option 4"]
    valueAlgorithm = tkinter.StringVar(mainTK.SortingFrame)
    valueAlgorithm.set("Select an Algorithm")
    Order = ["Option 1", "Option 2", "Option 3", "Option 4"]
    valueOrder = tkinter.StringVar(mainTK.SortingFrame)
    valueOrder.set("Select Order")
    mainTK.selectColumn = customtkinter.CTkOptionMenu(master=mainTK.SortingFrame,width=200,values=Columns,variable=valueColumn)
    mainTK.selectColumn.grid(column=0,row=1,sticky='e')
    mainTK.selectAlgorithm = customtkinter.CTkOptionMenu(master=mainTK.SortingFrame,width=200,values=Algorithms,variable=valueAlgorithm)
    mainTK.selectAlgorithm.grid(column=0,row=2,sticky='e')
    mainTK.selectOrder = customtkinter.CTkOptionMenu(master=mainTK.SortingFrame,width=200,values=Order,variable=valueOrder)
    mainTK.selectOrder.grid(column=0,row=3,sticky='e')
    mainTK.btnClearSortingFilters = customtkinter.CTkButton(master=mainTK.SortingFrame,text="CLEAR",command=btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
    mainTK.btnClearSortingFilters.grid(row=4, column=0,columnspan=2,sticky="w",padx=5)
    mainTK.btnStartSorting = customtkinter.CTkButton(master=mainTK.SortingFrame,text="START",command=btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
    mainTK.btnStartSorting.grid(row=4, column=0,sticky="e",columnspan=2,padx=5)
    lstofAllLevels=["pa","pb"]
    rows = len(lstofAllLevels)
    mainTK.treeOfAllLevels = ttk.Treeview(mainTK.SortingFrame, columns=(1, 2), height=rows, show="headings")
    mainTK.treeOfAllLevels.grid(row=5, column=0,columnspan=2,sticky="nesw",pady=5)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
    style.map("Treeview",background=[('selected', 'green')])
    mainTK.treeOfAllLevels.heading("#1", text="LEVEL", anchor='center')
    mainTK.treeOfAllLevels.heading("#2", text="DETAILS", anchor='center')
    mainTK.treeOfAllLevels.column("#1", width=150, minwidth=25, anchor='w')
    mainTK.treeOfAllLevels.column("#2", width=150, minwidth=25, anchor='center')
    scroll = ttk.Scrollbar(mainTK.SortingFrame, orient="vertical", command=mainTK.treeOfAllLevels.yview)
    mainTK.treeOfAllLevels.configure(yscrollcommand=scroll.set)
    lstofAllTimes=["pa","pb"]
    rows = len(lstofAllTimes)
    mainTK.treeOfLevelsTimes = ttk.Treeview(mainTK.SortingFrame, columns=(1, 2), height=rows, show="headings")
    mainTK.treeOfLevelsTimes.grid(row=6, column=0,columnspan=2,sticky="nesw",pady=5)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
    style.map("Treeview",background=[('selected', 'green')])
    mainTK.treeOfLevelsTimes.heading("#1", text="LEVEL", anchor='center')
    mainTK.treeOfLevelsTimes.heading("#2", text="Time", anchor='center')
    mainTK.treeOfLevelsTimes.column("#1", width=150, minwidth=25, anchor='w')
    mainTK.treeOfLevelsTimes.column("#2", width=150, minwidth=25, anchor='center')
    scroll = ttk.Scrollbar(mainTK.SortingFrame, orient="vertical", command=mainTK.treeOfLevelsTimes.yview)
    mainTK.treeOfLevelsTimes.configure(yscrollcommand=scroll.set)
                   ################# Searching Frame  ################
    mainTK.SearchingFrame.grid_columnconfigure(0, weight=1)
    mainTK.SearchingFrame.grid_columnconfigure(1, weight=1)
    mainTK.SearchingFrame.grid_columnconfigure(2, weight=1)
    mainTK.SearchingFrame.grid_rowconfigure(0, weight=1)
    mainTK.SearchingFrame.grid_rowconfigure(1, weight=1)
    mainTK.SearchingFrame.grid_rowconfigure(2, weight=1)
    mainTK.SearchingFrame.grid_rowconfigure(3, weight=1)
    Operators = ["Option 1", "Option 2", "Option 3", "Option 4"]
    valueOperator = tkinter.StringVar(mainTK.SearchingFrame)
    valueOperator.set("Select Operator")
    mainTK.lblSorting = customtkinter.CTkLabel(master=mainTK.SearchingFrame, text="Multi-Level Searching",text_font=("Century Gothic", 16))
    mainTK.lblSorting.grid(column=0, row=0,columnspan=3,sticky="nesw")
    mainTK.search1 = customtkinter.CTkEntry(master=mainTK.SearchingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="Harry Potter")
    mainTK.search1.grid(column=0, row=1,pady=0,padx=0,sticky="w")
    mainTK.selectOperater = customtkinter.CTkOptionMenu(master=mainTK.SearchingFrame,width=200,values=Operators,variable=valueOperator)
    mainTK.selectOperater.grid(column=0,row=2,sticky='w')
    mainTK.search2 = customtkinter.CTkEntry(master=mainTK.SearchingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="philospher's stone")
    mainTK.search2.grid(column=0, row=3,pady=0,padx=0,sticky="w")
    mainTK.selectOperater = customtkinter.CTkOptionMenu(master=mainTK.SearchingFrame,width=200,values=Operators,variable=valueOperator)
    mainTK.selectOperater.grid(column=1,row=1,sticky='w')
    mainTK.selectOperater = customtkinter.CTkOptionMenu(master=mainTK.SearchingFrame,width=200,values=Operators,variable=valueOperator)
    mainTK.selectOperater.grid(column=1,row=2,sticky='w')
    mainTK.selectOperater = customtkinter.CTkOptionMenu(master=mainTK.SearchingFrame,width=200,values=Operators,variable=valueOperator)
    mainTK.selectOperater.grid(column=1,row=3,sticky='w')
    mainTK.a = customtkinter.CTkButton(master=mainTK.SearchingFrame,width=170, height=60,text="DASHBOARD",command=btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
    mainTK.a.grid(row=0, column=3, pady=10, padx=20,sticky='nesw')
    mainTK.b = customtkinter.CTkButton(master=mainTK.SearchingFrame,width=170, height=60,text="EXIT",command=btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
    mainTK.b.grid(row=2, column=3, pady=10, padx=20,sticky='nesw')

mainTK.title("LIBRARY MANAGMENT SYSTEM")
width = mainTK.winfo_screenwidth()
height = mainTK.winfo_screenheight()  # HEIGHT and WIDTH of SCREEN
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
mainTK.state('zoomed')

# Grid layout of Main Window
mainTK.grid_columnconfigure(0, weight=10)
mainTK.grid_columnconfigure(1, weight=600)
mainTK.grid_rowconfigure(0, weight=10)
mainTK.grid_rowconfigure(1, weight=600)

mainTK.sideBar = customtkinter.CTkFrame(master=mainTK,corner_radius=0, fg_color=("#686868", "#000000"), border_color=('#FFFFFF', '#FFFFFF'),highlightbackground="black", highlightthickness=2)
mainTK.sideBar.grid(row=0, column=0,rowspan=2, sticky="wens")
mainTK.heading = customtkinter.CTkFrame(master=mainTK,width=150,fg_color=("#686868", "#000000"),corner_radius=0,highlightbackground="black", highlightthickness=2)
mainTK.heading.grid(row=0, column=1, sticky="wens", padx=1, pady=1)
mainTK.mainArea1 = customtkinter.CTkFrame(master=mainTK,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
mainTK.mainArea1.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
################### LOAD IMAGES ##############
def load_image(path, size):
    return ImageTk.PhotoImage(Image.open(PATH + path).resize((size[0], size[1])))
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)
mainTK.scrapingImg = load_image("/Resources/Images/scraping.png", (50,50))
mainTK.bookImg = load_image("/Resources/Images/book.png", (60,38))
mainTK.exitImg = load_image("/Resources/Images/exit.png", (50,50))
#################### SIDE Bar Menu ################
mainTK.sideBar.grid_rowconfigure(0, minsize=10)
mainTK.sideBar.grid_rowconfigure(5, weight=1)
mainTK.sideBar.grid_rowconfigure(8, minsize=20)
mainTK.sideBar.grid_rowconfigure(11, minsize=10)


mainTK.txtLogo = customtkinter.CTkLabel(master=mainTK.sideBar,text="L M S",text_font=("Century Gothic", 48))
mainTK.txtLogo.grid(row=1, column=0, pady=0, padx=0,sticky='s')

mainTK.menubtnScrap = customtkinter.CTkButton(master=mainTK.sideBar,width=170, height=60,image=mainTK.scrapingImg,text="SCRAP DATA",command=btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
mainTK.menubtnScrap.grid(row=2, column=0, pady=10, padx=20,sticky='s')
# #023246
mainTK.menubtndashBoard = customtkinter.CTkButton(master=mainTK.sideBar,width=170, height=60,image=mainTK.bookImg,text="DASHBOARD",command=dashBoard,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
mainTK.menubtndashBoard.grid(row=3, column=0, pady=10, padx=20,sticky='s')
mainTK.menubtnExit = customtkinter.CTkButton(master=mainTK.sideBar,width=170, height=60,image=mainTK.exitImg,text="EXIT",command=btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
mainTK.menubtnExit.grid(row=4, column=0, pady=10, padx=20,sticky='s')

mainTK.lblMode = customtkinter.CTkLabel(master=mainTK.sideBar, text="CHANGE THEME",text_font=("Century Gothic", 11))
mainTK.lblMode.grid(row=9, column=0, pady=0, padx=20, sticky="w")
mainTK.cmbTheme = customtkinter.CTkOptionMenu(master=mainTK.sideBar,values=["LIGHT", "DARK", "SYSTEM"],command=change_appearance_mode,text_font=("Century Gothic", 11))
mainTK.cmbTheme.grid(row=10, column=0, pady=10, padx=20, sticky="w")
################### Heading  ################
mainTK.heading.grid_columnconfigure(0, weight=1)
mainTK.lblHeading = customtkinter.CTkLabel(master=mainTK.heading, text="WELCOME",text_font=("Century Gothic", 48))
mainTK.lblHeading.grid(column=0, row=0)
############################################
scrapingWindow()

mainTK.mainloop()
