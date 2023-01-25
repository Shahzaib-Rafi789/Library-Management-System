import tkinter 
from tkinter import ttk
import threading
import customtkinter
from PIL import Image,ImageTk
from FINAL_SCRAPPING import scrapData,startScraping,stopScraping,pauseScraping,csvtoList,booksScrapped
import os
import time
from enum import Enum
from SortLogic import SortHandler,AllSortFunc
check=True
disableFlag=True
PATH = os.path.dirname(os.path.realpath(__file__))
class my_Treeview():
    def __init__(self,parent,grid_row,grid_column,Headings,isVertical,isHorizontal,entryLimit):
        self.limit=entryLimit;
        self.counter=1
        self.trv=ttk.Treeview(parent,selectmode='browse')
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 11, "bold"))
        style.map("Treeview",background=[('selected', 'red')])
        self.trv.grid(row=0,column=0,sticky="nesw")
        self.trv["columns"]=Headings
        self.trv['show']='headings'
        for i in range(0,len(Headings)):
            self.trv.column(str(i),anchor='c',stretch=0)
            self.trv.heading(str(i),text=str(Headings[i]))
        if(isVertical==True):
            self.trv.yscrollbar = ttk.Scrollbar(parent, orient='vertical', command=self.trv.yview)
            self.trv.yscrollbar.grid(row=0, column=0, sticky='nse')
            self.trv.configure(yscrollcommand=self.trv.yscrollbar.set)
            self.trv.yscrollbar.configure(command=self.trv.yview)
        if(isHorizontal==True):
            # self.trv.configure()
            self.trv.hscrollbar = ttk.Scrollbar(parent, orient='horizontal', command=self.trv.xview)
            self.trv.hscrollbar.grid(row=1,column=0, sticky='new')
            self.trv.configure(xscrollcommand=self.trv.hscrollbar.set)
            self.trv.hscrollbar.configure(command=self.trv.xview)
    def addEntry(self,data): 
        if(type(data)==str):
            data=[data]
        data.insert(0,self.counter)
        if(type(self.limit)==int):
            if(self.limit>=self.counter):
                self.trv.insert("",'end',values=(data))
                self.counter+=1;
        else:
            self.trv.insert("",'end',values=(data))
            self.counter+=1;
    def deleteEntry(self):
        selected_item = self.trv.selection() ## get selected item
        self.trv.delete(selected_item)
        self.counter-=1
        i=1
        for j in self.trv.get_children():
            self.trv.set(j, '#1', i)
            i+=1
    def ClearTable(self):
        for i in self.trv.get_children():
            self.trv.delete(i)
        self.counter=1
    def getAllData(self):
        lst=[]
        for i in self.trv.get_children():
            lst.append(list(i))
        return lst
    def addList(self,lstofData):
        for j in range(len(lstofData)):
            self.addEntry(lstofData[j])
            # self.trv.insert("",'end',values=(lstofData[j]))
            # self.counter+=1
class Columns(Enum):
    # columns = ('TITLE', 'AUTHOR(S)', 'LANGUAGE','PUBLISHER',"PUBLISH YEAR","FILE FORMAT","FILE SIZE")
    Option1 = "TITLE"
    Option2 = "AUTHOR(S)"
    Option3='LANGUAGE'
    Option4='PUBLISHER'
    Option5="PUBLISH YEAR"
    Option6="FILE FORMAT"
    Option7="FILE SIZE"
typeDic={
    "TITLE":"string",
    "AUTHOR(S)":"string",
    'LANGUAGE':"string",
    'PUBLISHER':"string",
    "PUBLISH YEAR":"int",
    "FILE FORMAT":"string",
    "FILE SIZE":"string",
    "Select a Column":"string"
}
class Order(Enum):
    Option1="Ascending"
    Option2="Descending"
    
class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        global booksScrapped
        self.root = customtkinter.CTk()
        self.root.currentFrame="None";
        self.valueColumn="None";
        self.valueAlgorithm="None";
        self.valueOrder="None";
        self.level=0;
        self.root.treeOfAllLevels='None';
        # self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("LIBRARY MANAGMENT SYSTEM")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()  # HEIGHT and WIDTH of SCREEN
        self.root.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.root.state('zoomed')
        self.root.grid_columnconfigure(0, weight=10)
        self.root.grid_columnconfigure(1, weight=600)
        self.root.grid_rowconfigure(0, weight=10)
        self.root.grid_rowconfigure(1, weight=600)
        # =====================================Grids=========================================================================
        self.root.scrapingImg = self.load_image("/Resources/Images/scraping.png", (50,50))
        self.root.bookImg = self.load_image("/Resources/Images/book.png", (60,38))
        self.root.exitImg = self.load_image("/Resources/Images/exit.png", (50,50))
        self.root.sideBar = customtkinter.CTkFrame(master=self.root,corner_radius=0, fg_color=("#686868", "#000000"), border_color=('#FFFFFF', '#000000'),highlightbackground=("#000000"), highlightthickness=2)
        self.root.sideBar.grid(row=0, column=0,rowspan=2, sticky="wens")
        self.root.heading = customtkinter.CTkFrame(master=self.root,width=150,fg_color=("#686868", "#000000"),corner_radius=0,highlightbackground="black", highlightthickness=2)
        self.root.heading.grid(row=0, column=1, sticky="wens", padx=1, pady=1)
        self.root.mainArea1 = customtkinter.CTkFrame(master=self.root,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
        self.root.mainArea1.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
        #################### SIDE Bar Menu ################
        self.root.sideBar.grid_rowconfigure(0, minsize=10)
        self.root.sideBar.grid_rowconfigure(5, weight=1)
        self.root.sideBar.grid_rowconfigure(8, minsize=20)
        self.root.sideBar.grid_rowconfigure(11, minsize=10)
        
        self.root.txtLogo = customtkinter.CTkLabel(master=self.root.sideBar,text="L M S",text_font=("Century Gothic", 48))
        self.root.txtLogo.grid(row=1, column=0, pady=0, padx=0,sticky='s')

        self.root.menubtnScrap = customtkinter.CTkButton(master=self.root.sideBar,width=170, height=60,image=self.root.scrapingImg,text="SCRAP DATA",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.root.menubtnScrap.grid(row=2, column=0, pady=10, padx=20,sticky='s')
        # # #023246
        self.root.menubtndashBoard = customtkinter.CTkButton(master=self.root.sideBar,width=170, height=60,image=self.root.bookImg,text="DASHBOARD",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.root.menubtndashBoard.grid(row=3, column=0, pady=10, padx=20,sticky='s')
        self.root.menubtnExit = customtkinter.CTkButton(master=self.root.sideBar,width=170, height=60,image=self.root.exitImg,text="EXIT",command=self.close,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.root.menubtnExit.grid(row=4, column=0, pady=10, padx=20,sticky='s')

        self.root.lblMode = customtkinter.CTkLabel(master=self.root.sideBar, text="CHANGE THEME",text_font=("Century Gothic", 11))
        self.root.lblMode.grid(row=9, column=0, pady=0, padx=20, sticky="w")
        self.root.cmbTheme = customtkinter.CTkOptionMenu(master=self.root.sideBar,values=["LIGHT", "DARK", "SYSTEM"],command=self.change_appearance_mode,text_font=("Century Gothic", 11))
        self.root.cmbTheme.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        
        self.root.heading.grid_columnconfigure(0, weight=1)
        self.root.lblHeading = customtkinter.CTkLabel(master=self.root.heading, text="WELCOME",text_font=("Century Gothic", 48))
        self.root.lblHeading.grid(column=0, row=0)
        # #################### SIDE Bar Menu ################
        self.root.sideBar.grid_rowconfigure(0, minsize=10)
        self.root.sideBar.grid_rowconfigure(5, weight=1)
        self.root.sideBar.grid_rowconfigure(8, minsize=20)
        self.root.sideBar.grid_rowconfigure(11, minsize=10)
        
        self.root.txtLogo = customtkinter.CTkLabel(master=self.root.sideBar,text="L M S",text_font=("Century Gothic", 48))
        self.root.txtLogo.grid(row=1, column=0, pady=0, padx=0,sticky='s')

        self.root.menubtnScrap = customtkinter.CTkButton(master=self.root.sideBar,width=170, height=60,image=self.root.scrapingImg,text="SCRAP DATA",command=self.switchtoScrapping,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.root.menubtnScrap.grid(row=2, column=0, pady=10, padx=20,sticky='s')
        # # #023246
        self.root.menubtndashBoard = customtkinter.CTkButton(master=self.root.sideBar,width=170, height=60,image=self.root.bookImg,text="DASHBOARD",command=self.switchtoDashBoard,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.root.menubtndashBoard.grid(row=3, column=0, pady=10, padx=20,sticky='s')
        self.root.menubtnExit = customtkinter.CTkButton(master=self.root.sideBar,width=170, height=60,image=self.root.exitImg,text="EXIT",command=self.close,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.root.menubtnExit.grid(row=4, column=0, pady=10, padx=20,sticky='s')

        self.root.lblMode = customtkinter.CTkLabel(master=self.root.sideBar, text="CHANGE THEME",text_font=("Century Gothic", 11))
        self.root.lblMode.grid(row=9, column=0, pady=0, padx=20, sticky="w")
        self.root.cmbTheme = customtkinter.CTkOptionMenu(master=self.root.sideBar,values=["LIGHT", "DARK", "SYSTEM"],command=self.change_appearance_mode,text_font=("Century Gothic", 11))
        self.root.cmbTheme.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        
        self.root.heading.grid_columnconfigure(0, weight=1)
        self.root.lblHeading = customtkinter.CTkLabel(master=self.root.heading, text="WELCOME",text_font=("Century Gothic", 48))
        self.root.lblHeading.grid(column=0, row=0)
        # ===================================================================================================================================================== #
        self.root.mainloop()
    def switchtoScrapping(self):
         global disableFlag
         heading="SCRAPPING"
         if(self.root.currentFrame!=heading):
            self.clearFrame()
            self.root.currentFrame=heading
            self.root.ScrappingWindow = customtkinter.CTkFrame(master=self.root,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
            self.root.ScrappingWindow.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
            self.root.ScrappingWindow.grid_columnconfigure(0, weight=1)
            self.root.ScrappingWindow.grid_columnconfigure(1, weight=5)
            self.root.ScrappingWindow.grid_rowconfigure(0, weight=5)
            self.root.ScrappingWindow.grid_rowconfigure(1, weight=1)
            self.root.scrapingFrame=customtkinter.CTkFrame(master=self.root.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.root.scrapingFrame.grid(row=0, column=0, sticky="wens",padx=10,pady=10)
            self.root.statsFrame=customtkinter.CTkFrame(master=self.root.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.root.statsFrame.grid(row=0, column=1, sticky="wens",padx=10,pady=10)
            self.root.progessFrame=customtkinter.CTkFrame(master=self.root.ScrappingWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.root.progessFrame.grid(row=1, column=0,columnspan=2, sticky="wens",padx=10,pady=10)
                            ################# Scraping Frame  ################
            self.root.scrapingFrame.grid_columnconfigure(0, weight=1)
            self.root.scrapingFrame.grid_columnconfigure(1, weight=1)
            self.root.scrapingFrame.grid_rowconfigure(0, weight=1)
            self.root.scrapingFrame.grid_rowconfigure(1, weight=1)
            self.root.scrapingFrame.grid_rowconfigure(2, weight=1)
            self.root.scrapingFrame.grid_rowconfigure(3, weight=1)
            self.root.scrapingFrame.grid_rowconfigure(4, weight=30)
            self.root.lblScrapWebsite = customtkinter.CTkLabel(master=self.root.scrapingFrame, text="SCRAP TAB",text_font=("Century Gothic", 16))
            self.root.lblScrapWebsite.grid(column=0, row=0,sticky="nesw",columnspan=2)
            self.root.lblScrapWebsite = customtkinter.CTkLabel(master=self.root.scrapingFrame, text="SCRAP FROM URL:",text_font=("Century Gothic", 12))
            self.root.lblScrapWebsite.grid(column=0, row=1,sticky="w")
            self.root.entURl = customtkinter.CTkEntry(master=self.root.scrapingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="example https://archive.org/")
            self.root.entURl.grid(column=1, row=1,pady=0,padx=0,sticky="w")
            self.root.entURl.configure(state= "disabled")
            self.root.btnStart1 = customtkinter.CTkButton(master=self.root.scrapingFrame,text="Start",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 12))
            self.root.btnStart1.grid(row=2, column=1,sticky='w')
            self.root.btnStart1.configure(state= "disabled")
            # self.root.btnStart1.state=ttk.DISABLED
            self.root.lblScrapPrecoded = customtkinter.CTkLabel(master=self.root.scrapingFrame, text="SCRAP FROM  PRE-CODED WEBSITE:",text_font=("Century Gothic", 12))
            self.root.lblScrapPrecoded.grid(column=0, row=3,sticky="w") 
            self.root.btnStart2 = customtkinter.CTkButton(master=self.root.scrapingFrame,text="Start",command=startScraping,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 12))
            self.root.btnStart2.grid(row=3, column=1,sticky="w")
            lstFailAttribs=["pa","pb"]
            rows = len(lstFailAttribs)
            self.root.treeOfFailAttributes = ttk.Treeview(self.root.scrapingFrame, columns=(1, 2), height=rows, show="headings")
            self.root.treeOfFailAttributes.grid(row=4, column=0,columnspan=2,sticky="nesw")
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
            style.map("Treeview",background=[('selected', 'green')])
            self.root.treeOfFailAttributes.heading("#1", text="ATTRIBUTES", anchor='center')
            self.root.treeOfFailAttributes.heading("#2", text="STATUS", anchor='center')
            self.root.treeOfFailAttributes.column("#1", width=150, minwidth=25, anchor='w')
            self.root.treeOfFailAttributes.column("#2", width=150, minwidth=25, anchor='center')
            scroll = ttk.Scrollbar(self.root.scrapingFrame, orient="vertical", command=self.root.treeOfFailAttributes.yview)
            self.root.treeOfFailAttributes.configure(yscrollcommand=scroll.set)
                            ################# Progress Bar Frame  ################
            self.root.progessFrame.grid_columnconfigure(0, weight=1)
            self.root.progessFrame.grid_columnconfigure(1, weight=1)
            self.root.progessFrame.grid_rowconfigure(0, weight=1)
            self.root.progessFrame.grid_rowconfigure(1, weight=1)
            self.root.progessFrame.grid_rowconfigure(2, weight=1)
            self.root.PBscrap=customtkinter.CTkProgressBar(self.root.progessFrame,orient="horizontal",mode='determinate')
            self.root.PBscrap.grid(row=0,column=0,columnspan=2,sticky="ew", padx=15, pady=15)
            step1=booksScrapped/25
            self.root.PBscrap.set(0)
            self.root.PBscrap["value"]=step1
            os.system('cls')
            print(booksScrapped)
            self.root.btnPauseScrapping = customtkinter.CTkButton(master=self.root.progessFrame,text="PAUSE",command=pauseScraping,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 16))
            self.root.btnPauseScrapping.grid(row=1, column=0,sticky="e")
            self.root.btnEndScraping = customtkinter.CTkButton(master=self.root.progessFrame,text="END",command=stopScraping,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 16))
            self.root.btnEndScraping.grid(row=1, column=1,sticky="w")
            # if(disableFlag==True):
            #     self.root.btnEndScraping.configure(state= "disabled")
            #     self.root.btnPauseScrapping.configure(state= "disabled")
            # else:
            #     self.root.btnPauseScrapping.configure(state= "NORMAL")
            #     self.root.btnEndScraping.configure(state= "NORMAL")
                
    def switchtoDashBoard(self):
        heading="DASHBOARD"
        if(self.root.currentFrame!=heading):
            self.clearFrame()
            self.root.currentFrame=heading
            self.root.lblHeading.configure(text = heading)
            self.root.DashBoardWindow = customtkinter.CTkFrame(master=self.root,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
            self.root.DashBoardWindow.grid_columnconfigure(0, weight=1)
            self.root.DashBoardWindow.grid_columnconfigure(1, weight=10)
            self.root.DashBoardWindow.grid_rowconfigure(0, weight=1)
            self.root.DashBoardWindow.grid_rowconfigure(1, weight=1)
            self.root.SortingFrame=customtkinter.CTkFrame(master=self.root.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.root.SortingFrame.grid(row=0, column=0,rowspan=2, sticky="wens",padx=10,pady=10)
            self.root.SearchingFrame=customtkinter.CTkFrame(master=self.root.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.root.SearchingFrame.grid(row=0, column=1, sticky="wens",padx=10,pady=10)
            self.root.TableFrame=customtkinter.CTkFrame(master=self.root.DashBoardWindow,highlightbackground="#ffffff", highlightthickness=2)
            self.root.TableFrame.grid(row=1, column=1, sticky="wens",padx=10,pady=10)
            self.root.DashBoardWindow.grid(row=1, column=1, sticky="wens", padx=1, pady=1)
                        ################# Sorting Frame  ################
            self.root.SortingFrame.grid_columnconfigure(0, weight=1)
            self.root.SortingFrame.grid_columnconfigure(1, weight=1)
            self.root.SortingFrame.grid_rowconfigure(0, weight=1)
            self.root.SortingFrame.grid_rowconfigure(1, weight=1)
            self.root.SortingFrame.grid_rowconfigure(2, weight=1)
            self.root.SortingFrame.grid_rowconfigure(3, weight=1)
            self.root.SortingFrame.grid_rowconfigure(4, weight=1)
            self.root.SortingFrame.grid_rowconfigure(5, weight=1)
            self.root.SortingFrame.grid_rowconfigure(6, weight=15)
            self.root.SortingFrame.grid_rowconfigure(7, weight=15)
            self.root.lblSorting = customtkinter.CTkLabel(master=self.root.SortingFrame, text="Multi-Level Sorting",text_font=("Century Gothic", 16))
            self.root.lblSorting.grid(column=0, row=0,sticky="nesw")
            # Columns = ["Option 1", "Option 2", "Option 3", "Option 4"]
            self.valueColumn = tkinter.StringVar(self.root.SortingFrame)
            self.valueColumn.set("Select a Column")
            # Order = ["Option 1", "Option 2", "Option 3", "Option 4"]
            self.valueOrder = tkinter.StringVar(self.root.SortingFrame)
            self.valueOrder.set("Select Order")
            self.root.selectColumn = customtkinter.CTkOptionMenu(master=self.root.SortingFrame,width=200,values=[i.value for i in Columns],variable=self.valueColumn,text_font=("Century Gothic", 10))
            self.root.selectColumn.grid(column=0,row=1,sticky='new')
            Algorithms = AllSortFunc.GetListAccToType(typeDic[self.valueColumn.get()])
            self.valueAlgorithm = tkinter.StringVar(self.root.SortingFrame)
            self.valueAlgorithm.set("Select an Algorithm")
            self.root.selectAlgorithm = customtkinter.CTkOptionMenu(master=self.root.SortingFrame,width=200,values=Algorithms,variable=self.valueAlgorithm,text_font=("Century Gothic", 10))
            self.root.selectAlgorithm.grid(column=0,row=2,sticky='new')
            self.root.selectOrder = customtkinter.CTkOptionMenu(master=self.root.SortingFrame,width=200,values=[i.value for i in Order],variable=self.valueOrder,text_font=("Century Gothic", 10))
            self.root.selectOrder.grid(column=0,row=3,sticky='new')
            # self.root.btnAddLevel=customtkinter.CTkButton(master=self.root.SortingFrame,text="ADD",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
            # self.root.btnAddLevel.grid(row=4, column=0,sticky="e",columnspan=2,padx=5)
            # self.root.btnAddLevel=customtkinter.CTkButton(master=self.root.SortingFrame,text="DELTE",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
            # self.root.btnAddLevel.grid(row=4, column=0,sticky="e",columnspan=2,padx=5)
            lstofAllLevels=["pa","pb"]
            rows = len(lstofAllLevels)
            # self.treeOfAllLevels = ttk.Treeview(self.root.SortingFrame)
            # self.root.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.treeOfAllLevels.yview)
            # self.treeOfAllLevels.configure(yscrollcommand=self.yscrollbar.set)
            # self.treeOfAllLevels.grid(row=6, column=0, sticky="nsew")
            # self.yscrollbar.grid(row=0, column=1, sticky='nse')
            # self.root.yscrollbar.configure(command=self.treeOfAllLevels.yview)
            # self.root.grid_rowconfigure(0, weight=1)
            # self.root.grid_columnconfigure(0, weight=1)
            # self.yscrollbar.configure(command=self.treeOfAllLevels.yview)
            # self.root.treeOfAllLevels = ttk.Treeview(self.root.SortingFrame, columns=(1, 2), height=rows, show="headings")
            self.root.TreeofAllLevelsframe=customtkinter.CTkFrame(master=self.root.SortingFrame,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
            self.root.TreeofAllLevelsframe.grid(row=6, column=0, sticky="wens",padx=0,pady=0)
            self.root.treeOfAllLevels = my_Treeview(self.root.TreeofAllLevelsframe,0,0,["LEVEL","DETAILS"],True,True,8)
            
            self.root.treeOfLevelsTimesframe=customtkinter.CTkFrame(master=self.root.SortingFrame,width=150,corner_radius=0,highlightbackground="black", highlightthickness=2)
            self.root.treeOfLevelsTimesframe.grid(row=7, column=0, sticky="wens",padx=0,pady=0)
            self.root.treeOfAllLevelsTime = my_Treeview(self.root.treeOfLevelsTimesframe,0,0,["LEVEL","TIME"],True,True,8)
            
            
            self.root.btnAddLevel = customtkinter.CTkButton(master=self.root.SortingFrame,text="ADD",command=lambda:self.root.treeOfAllLevels.addEntry(self.OnclickAdd()),fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
            self.root.btnAddLevel.grid(row=4, column=0,columnspan=2,sticky="w",padx=5)
            self.root.btnDeleteLevel = customtkinter.CTkButton(master=self.root.SortingFrame,text="DELETE",command=lambda:self.root.treeOfAllLevels.deleteEntry(),fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
            self.root.btnDeleteLevel.grid(row=4, column=0,sticky="e",columnspan=2,padx=5)
            self.root.btnClearSortingFilters = customtkinter.CTkButton(master=self.root.SortingFrame,text="CLEAR",command=lambda:self.root.treeOfAllLevels.ClearTable(),fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
            self.root.btnClearSortingFilters.grid(row=5, column=0,columnspan=2,sticky="w",padx=5)
            self.root.btnStartSorting = customtkinter.CTkButton(master=self.root.SortingFrame,text="SORT",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 12))
            self.root.btnStartSorting.grid(row=5, column=0,sticky="e",columnspan=2,padx=5)
            # rows = len(lstofAllTimes)
            # self.root.treeOfLevelsTimes = ttk.Treeview(self.root.SortingFrame, columns=(1, 2), height=rows, show="headings")
            # self.root.treeOfLevelsTimes.grid(row=7, column=0,sticky="nesw",pady=5)
            # style = ttk.Style()
            # style.theme_use("clam")
            # style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
            # style.map("Treeview",background=[('selected', 'green')])
            # self.root.treeOfLevelsTimes.heading("#1", text="LEVEL", anchor='center')
            # self.root.treeOfLevelsTimes.heading("#2", text="Time", anchor='center')
            # self.root.treeOfLevelsTimes.column("#1", width=150, minwidth=25, anchor='w')
            # self.root.treeOfLevelsTimes.column("#2", width=150, minwidth=25, anchor='center')
            # scroll = ttk.Scrollbar(self.root.SortingFrame, orient="vertical", command=self.root.treeOfLevelsTimes.yview)
            # self.root.treeOfLevelsTimes.configure(yscrollcommand=scroll.set)
                        ################# Searching Frame  ################
            self.root.SearchingFrame.grid_columnconfigure(0, weight=1)
            self.root.SearchingFrame.grid_columnconfigure(1, weight=1)
            self.root.SearchingFrame.grid_columnconfigure(2, weight=1)
            self.root.SearchingFrame.grid_rowconfigure(0, weight=1)
            self.root.SearchingFrame.grid_rowconfigure(1, weight=1)
            self.root.SearchingFrame.grid_rowconfigure(2, weight=1)
            self.root.SearchingFrame.grid_rowconfigure(3, weight=1)
            Operators = ["Option 1", "Option 2", "Option 3", "Option 4"]
            valueOperator = tkinter.StringVar(self.root.SearchingFrame)
            valueOperator.set("Select Operator")
            self.root.lblSorting = customtkinter.CTkLabel(master=self.root.SearchingFrame, text="Multi-Level Searching",text_font=("Century Gothic", 16))
            self.root.lblSorting.grid(column=0, row=0,columnspan=3,sticky="nesw")
            self.root.search1 = customtkinter.CTkEntry(master=self.root.SearchingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="Harry Potter")
            self.root.search1.grid(column=0, row=1,pady=0,padx=0,sticky="w")
            self.root.selectOperater = customtkinter.CTkOptionMenu(master=self.root.SearchingFrame,width=200,values=Operators,variable=valueOperator)
            self.root.selectOperater.grid(column=0,row=2,sticky='w')
            self.root.search2 = customtkinter.CTkEntry(master=self.root.SearchingFrame,width=300,text_font=("Century Gothic", 12), placeholder_text="philospher's stone")
            self.root.search2.grid(column=0, row=3,pady=0,padx=0,sticky="w")
            self.root.selectOperater = customtkinter.CTkOptionMenu(master=self.root.SearchingFrame,width=200,values=Operators,variable=valueOperator)
            self.root.selectOperater.grid(column=1,row=1,sticky='w')
            self.root.selectOperater = customtkinter.CTkOptionMenu(master=self.root.SearchingFrame,width=200,values=Operators,variable=valueOperator)
            self.root.selectOperater.grid(column=1,row=2,sticky='w')
            self.root.selectOperater = customtkinter.CTkOptionMenu(master=self.root.SearchingFrame,width=200,values=Operators,variable=valueOperator)
            self.root.selectOperater.grid(column=1,row=3,sticky='w')
            columns = ("Index",'TITLE', 'AUTHOR(S)', 'LANGUAGE','PUBLISHER',"PUBLISH YEAR","FILE FORMAT","FILE SIZE")
            self.root.treeOfBooks=my_Treeview(self.root.TableFrame,0,0,columns,True,True,False)
            self.root.treeOfBooks.addList(csvtoList())
            # self.root.treeOfBooks = ttk.Treeview(self.root.TableFrame, columns=columns, height=rows, show="headings")
            # self.root.treeOfBooks.grid(row=0, column=0,sticky="nesw")
            # style = ttk.Style()
            # style.theme_use("clam")
            # style.configure("Treeview.Heading",background="silver",foreground="black",rowheight=55,fieldbackground="silver",font=("Century Gothic", 12, "bold"))
            # style.map("Treeview",background=[('selected', 'green')])
            # self.root.treeOfBooks.heading("#1", text="TITLE", anchor='center')
            # self.root.treeOfBooks.heading("#2", text="AUTHOR(S)", anchor='center')
            # self.root.treeOfBooks.heading("#3", text="LANGUAGE", anchor='center')
            # self.root.treeOfBooks.heading("#4", text="PUBLISH YEAR", anchor='center')
            # self.root.treeOfBooks.heading("#5", text="PUBLISHER", anchor='center')
            # self.root.treeOfBooks.heading("#6", text="FILE FORMAT", anchor='center')
            # self.root.treeOfBooks.heading("#7", text="FILE SIZE", anchor='center')
            # self.root.treeOfBooks.column("#1", width=150, minwidth=25, anchor='w')
            # self.root.treeOfBooks.column("#2", width=150, minwidth=25, anchor='center')
            # self.root.treeOfBooks.column("#3", width=150, minwidth=25, anchor='center')
            # self.root.treeOfBooks.column("#4", width=150, minwidth=25, anchor='center')
            # self.root.treeOfBooks.column("#5", width=150, minwidth=25, anchor='center')
            # self.root.treeOfBooks.column("#6", width=150, minwidth=25, anchor='center')
            # self.root.treeOfBooks.column("#7", width=150, minwidth=25, anchor='center')
            # scroll = ttk.Scrollbar(self.root.scrapingFrame, orient="vertical", command=self.root.treeOfBooks.yview)
            # self.root.treeOfBooks.configure(yscrollcommand=scroll.set)
    # def onClickStart(self):
    #         global disableFlag
    #         disableFlag=False
    #         self.root.btnStart2.configure(state= "disabled")
    #         self.root.btnPauseScrapping.configure(state= "NORMAL")
    #         self.root.btnEndScraping.configure(state= "NORMAL")
    #         startScraping()
    def change_appearance_mode(self,new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def clearFrame(self):
        for widget in self.root.mainArea1.winfo_children():
            widget.destroy()
    def load_image(self, path, image_size):
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size[0], image_size[1])))
    def btn(self):
        return
    def close(self):
        global check
        check=False
        self.root.quit()
    def OnclickAdd(self):
        Details=str(self.valueColumn.get()+" by "+self.valueAlgorithm.get()+" in "+self.valueOrder.get())
        return (Details)
    def onClickSort(self):
        lst=self.root.treeofAllLevels.getAllData()
app = App()
while(check==True):
        time.sleep(2)
        scrapData()