# Run tkinter code in another thread

import tkinter as ttk
import threading
import customtkinter
from PIL import Image,ImageTk 
from FINAL_SCRAPPING import scrapData,startScraping,stopScraping
import os

PATH = os.path.dirname(os.path.realpath(__file__))
class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = customtkinter.CTk()
        self.root.currentFrame="None";
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
        self.root.sideBar = customtkinter.CTkFrame(master=self.root,corner_radius=0, fg_color=("#686868", "#000000"), border_color=('#FFFFFF', '#FFFFFF'),highlightbackground="black", highlightthickness=2)
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
        # #023246
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
        #################### SIDE Bar Menu ################
        self.root.sideBar.grid_rowconfigure(0, minsize=10)
        self.root.sideBar.grid_rowconfigure(5, weight=1)
        self.root.sideBar.grid_rowconfigure(8, minsize=20)
        self.root.sideBar.grid_rowconfigure(11, minsize=10)
        
        self.root.txtLogo = customtkinter.CTkLabel(master=self.root.sideBar,text="L M S",text_font=("Century Gothic", 48))
        self.root.txtLogo.grid(row=1, column=0, pady=0, padx=0,sticky='s')

        self.root.menubtnScrap = customtkinter.CTkButton(master=self.root.sideBar,width=170, height=60,image=self.root.scrapingImg,text="SCRAP DATA",command=self.switchtoScrapping,fg_color=("#686868", "#000000"),corner_radius=0,text_font=("Century Gothic", 11))
        self.root.menubtnScrap.grid(row=2, column=0, pady=10, padx=20,sticky='s')
        # #023246
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
        # ===================================================================================================================================================== #
        self.root.mainloop()
    def switchtoScrapping(self):
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
            self.root.btnStart1 = customtkinter.CTkButton(master=self.root.scrapingFrame,text="Start",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 12))
            self.root.btnStart1.grid(row=2, column=1,sticky='w')
            # self.root.btnStart1.state=ttk.DISABLED
            self.root.lblScrapPrecoded = customtkinter.CTkLabel(master=self.root.scrapingFrame, text="SCRAP FROM  PRE-CODED WEBSITE:",text_font=("Century Gothic", 12))
            self.root.lblScrapPrecoded.grid(column=0, row=3,sticky="w") 
            self.root.btnStart2 = customtkinter.CTkButton(master=self.root.scrapingFrame,text="Start",command=startScraping,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 12))
            self.root.btnStart2.grid(row=3, column=1,sticky="w")
            # Add Tree#
                            ################# Progress Bar Frame  ################
            self.root.progessFrame.grid_columnconfigure(0, weight=1)
            self.root.progessFrame.grid_columnconfigure(1, weight=1)
            self.root.progessFrame.grid_rowconfigure(0, weight=1)
            self.root.progessFrame.grid_rowconfigure(1, weight=1)
            self.root.progessFrame.grid_rowconfigure(2, weight=1)
            self.root.PBscrap=customtkinter.CTkProgressBar(self.root.progessFrame,orient="horizontal")
            self.root.PBscrap.grid(row=0,column=0,columnspan=2,sticky="ew", padx=15, pady=15)
            self.root.btnPauseScrapping = customtkinter.CTkButton(master=self.root.progessFrame,text="PAUSE",command=self.btn,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 16))
            self.root.btnPauseScrapping.grid(row=1, column=0,sticky="e")
            self.root.btnEndScraping = customtkinter.CTkButton(master=self.root.progessFrame,text="END",command=stopScraping,fg_color=("#686868", "#000000"),corner_radius=10,text_font=("Century Gothic", 16))
            self.root.btnEndScraping.grid(row=1, column=1,sticky="w")
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
           #win.destroy()
        self.root.quit()

app = App()
while(True):
    scrapData()