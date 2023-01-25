from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def choice(op):
    if(op=="yes"):
        window.destroy()
    else:
        pop.destroy()
    

def close():
    global pop
    pop=Toplevel(window)

    sw=window.winfo_screenwidth()
    sh=window.winfo_screenheight()
    w=220
    h=100
    x=(sw/2)-(w/2)
    y=(sh/2)-(h/2)

    pop.title("Exit")
    pop.geometry(f'{w}x{h}+{int(x)}+{int(y)}')
    pop.config(bg='#6d7872')

    pop_lbl=Label(pop, text="Are you sure you want to exit?",font='Helvetica',bg='#6d7872')
    pop_lbl.pack(pady=10)

    frm=Frame(pop,bg='#6d7872')
    frm.pack(pady=5)
    
    yes=Button(frm,text="Yes",font=12,command=lambda: choice("yes"),bg='#6d7872',activeforeground='black',activebackground='#545c57',borderwidth=0)
    yes.grid(row=0,column=1,padx=20)

    no=Button(frm,text="No",font=12,command=lambda: choice("no"),bg='#6d7872',activeforeground='black',activebackground='#545c57',borderwidth=0)
    no.grid(row=0,column=2,padx=20)
    
def scrap_btn_hover(e):
    scrap_btn["bg"]="#545c57"

def exit_btn_hover(e):
    exit_btn["bg"]="#545c57"

def dashboard_btn_hover(e):
    dashboard_btn["bg"]="#545c57"

def scrap_btn_hover_leave(e):
    scrap_btn["bg"]='#5a635f'

def exit_btn_hover_leave(e):
    exit_btn["bg"]='#5a635f'

def dashboard_btn_hover_leave(e):
    dashboard_btn["bg"]='#5a635f'

def scrp_btn_hover(e):
    scrp_btn["bg"]="#5a635f"

def scrp_btn_hover_leave(e):
    scrap_btn["bg"]='#5a635f'

def scrp_btn2_hover(e):
    scrp_btn2["bg"]="#5a635f"

def scrp_btn2_hover_leave(e):
    scrp_btn2["bg"]='#5a635f'

def scrp_btn3_hover(e):
    scrp_btn3["bg"]="#5a635f"

def scrp_btn3_hover_leave(e):
    scrp_btn3["bg"]='#5a635f'

def scrp_btn4_hover(e):
    scrp_btn4["bg"]="#5a635f"

def scrp_btn4_hover_leave(e):
    scrp_btn4["bg"]='#6d7872'






def scrapwindow():
    pass

def dashboard_window():
    pass




window=Tk()

header=Frame(window,bg='#5a635f')
header.place(x=0,y=0, width=1600,height=110)

scrap_frm1=Frame(window,bg='#6d7872')
scrap_frm1.place(x=10,y=110, width=792,height=500)

scrap_frm2=Frame(window,bg='#6d7872')
scrap_frm2.place(x=800,y=110, width=800,height=500)

scrap_frm3=Frame(window,bg='#6d7872')
scrap_frm3.place(x=10,y=610, width=1600,height=250)

menu_frm=Frame(window,bg='#5a635f')
menu_frm.place(x=0,y=0, width=165,height=900)

logo=PhotoImage(file='icons\\icon4_resized.png')
sample_graph=PhotoImage(file='E:\\Semester 3\\graph.png')
logo_lbl=Label(image=logo,bg='#5a635f',padx=15,pady=15)
logo_lbl.place(x=18,y=-2)

#centering the screen
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
w=1920
h=1080
x=(sw/2)-(w/2)
y=(sh/2)-(h/2)



#lbl=Label(window, text=f'Width:{sw} Height{sh}')
#lbl.pack(pady=20)

scrp_lbl=Label(scrap_frm1,text="Scrap from URL",font=('Helvetica',18),fg='black',bg='#6d7872',pady=20)
#scrp_lbl.pack()
scrp_lbl.place(x=320,y=10)

scrp_entry=Entry(scrap_frm1,font=('Helvetica',10))
scrp_entry.insert(END,"URL for scrapping")
#scrp_entry.pack()
scrp_entry.place(x=325,y=70)

scrp_btn_x=scrp_entry.winfo_rootx()
scrp_btn_y=scrp_entry.winfo_rooty()
scrp_btn_y+=10

scrp_btn=Button(window,text="Start",font=('Helvetica',14),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)
scrp_btn.bind("<Enter>",scrp_btn_hover)
scrp_btn.bind("<Leave>",scrp_btn_hover_leave)
scrp_btn.place(x=380,y=220)

scrp_lbl2=Label(scrap_frm1,text="Scrap from Pre-Coded Website",font=('Helvetica',18),fg='black',bg='#6d7872',pady=20)
scrp_lbl2.place(x=260,y=150)

scrp_btn2=Button(window,text="Start",font=('Helvetica',14),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)
scrp_btn2.bind("<Enter>",scrp_btn2_hover)
scrp_btn2.bind("<Leave>",scrp_btn2_hover_leave)
scrp_btn2.place(x=380,y=320)

scrp_listb=Listbox(scrap_frm1,bg='#5a635f',width=55)
#scrp_listb.config(height=scrp_listb.size()) #for changing the height dynamically
scrp_listb.place(x=260,y=280)

scrp_lbl3=Label(scrap_frm2,text="Statistics: ",font=('Helvetica',18),fg='black',bg='#6d7872',pady=20)
#scrp_lbl.pack()
scrp_lbl3.place(x=430,y=10)

scrp_graph=Label(image=sample_graph,bg='#5a635f')
scrp_graph.place(x=1150,y=200)

scrp_lbl4=Label(scrap_frm2,text="Number of Books Scrapped: ",font=('Helvetica',18),fg='black',bg='#6d7872',pady=20)
#scrp_lbl.pack()
scrp_lbl4.place(x=350,y=400)

scrp_prog= ttk.Progressbar(scrap_frm3, orient = HORIZONTAL,length = 500, mode = 'indeterminate')
scrp_prog.pack(pady=120)

scrp_btn3=Button(window,text="Pause",font=('Helvetica',14),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)
scrp_btn3.bind("<Enter>",scrp_btn3_hover)
scrp_btn3.bind("<Leave>",scrp_btn3_hover_leave)
scrp_btn3.place(x=420,y=750)

scrp_btn4=Button(window,text="End",font=('Helvetica',14),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)
scrp_btn4.bind("<Enter>",scrp_btn4_hover)
scrp_btn4.bind("<Leave>",scrp_btn4_hover_leave)
scrp_btn4.place(x=1130,y=750)




window.geometry(f'{w}x{h}')
window.title("Library Management System")
pic=PhotoImage(file='E:\\Semester 3\\icon.png')
window.iconphoto(True,pic)
Scrap=Label(window,text="Scrapping",font=('Helvetica',45,'bold'),fg='black',bg='#5a635f',padx=15,pady=15)
Scrap.place(y=-2)
Scrap.pack()
title=Label(window,text="LMS",font=('Garamond',45,'bold'),fg='black',bg='#5a635f',padx=15,pady=15)
title.place(x=5,y=110)
groupnum=Label(window,text="Group 03",font=('Helvetica',15,'bold','italic'),fg='black',bg='#5a635f',padx=10,pady=10)
groupnum.place(x=27,y=180)


#icon pics not showing
scrap_btn=PhotoImage(file='E:\\Semester 3\\scrap.png')
dashboard_btn=PhotoImage(file='E:\\Semester 3\\dashboard.png')
exit_btn=PhotoImage(file='E:\\Semester 3\\exit.png')

scrap_btn=Button(window,text="Scrap-Data",font=('Helvetica',18),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0,command=scrapwindow)#,image=scrap_btn,compound='left')
scrap_btn.pack()
scrap_btn.bind("<Enter>",scrap_btn_hover)
scrap_btn.bind("<Leave>",scrap_btn_hover_leave)
scrap_btn.place(x=15,y=250)
dashboard_btn=Button(window,text="Dashboard ",font=('Helvetica',18),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0,command=dashboard_window)#,image=dashboard_btn,compound='left')
dashboard_btn.pack()
dashboard_btn.bind("<Enter>",dashboard_btn_hover)
dashboard_btn.bind("<Leave>",dashboard_btn_hover_leave)
dashboard_btn.place(x=15,y=300)
exit_btn=Button(window,text="Exit", font=('Helvetica',18),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0,command=close)#,image=exit_btn,compound='left')
exit_btn.pack()
exit_btn.bind("<Enter>",exit_btn_hover)
exit_btn.bind("<Leave>",exit_btn_hover_leave)
exit_btn.place(x=15,y=350)

window.config(background="#6d7872")
window.mainloop()