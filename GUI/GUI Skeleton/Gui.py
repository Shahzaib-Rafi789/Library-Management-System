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
    yes.bind("<Enter>",yes_btn_hover)
    yes.bind("<Leave>",yes_btn_hover_leave)
    yes.grid(row=0,column=1,padx=20)

    no=Button(frm,text="No",font=12,command=lambda: choice("no"),bg='#6d7872',activeforeground='black',activebackground='#545c57',borderwidth=0)
    no.bind("<Enter>",no_btn_hover)
    no.bind("<Leave>",no_btn_hover_leave)
    no.grid(row=0,column=2,padx=20)
    
def add_btn_hover(e):
    add_btn["bg"]="#434a47"

def add_btn_hover_leave(e):
    add_btn["bg"]="#5a635f"

def yes_btn_hover(e):
    yes["bg"]="#434a47"

def yes_btn_hover_leave(e):
    yes["bg"]="#6b7571"

def no_btn_hover(e):
    no["bg"]="#434a47"

def no_btn_hover_leave(e):
    no["bg"]="#6b7571"

def scrap_btn_hover(e):
    scrap_btn["bg"]="#6b7571"

def exit_btn_hover(e):
    exit_btn["bg"]="#6b7571"

def dashboard_btn_hover(e):
    dashboard_btn["bg"]="#6b7571"

def scrap_btn_hover_leave(e):
    scrap_btn["bg"]='#5a635f'

def exit_btn_hover_leave(e):
    exit_btn["bg"]='#5a635f'

def dashboard_btn_hover_leave(e):
    dashboard_btn["bg"]='#5a635f'

def scrp_btn_hover(e):
    scrp_btn["bg"]="#434a47"

def scrp_btn_hover_leave(e):
    scrp_btn["bg"]='#5a635f'

def scrp_btn2_hover(e):
    scrp_btn2["bg"]="#434a47"

def scrp_btn2_hover_leave(e):
    scrp_btn2["bg"]='#5a635f'

def scrp_btn3_hover(e):
    scrp_btn3["bg"]="#434a47"

def scrp_btn3_hover_leave(e):
    scrp_btn3["bg"]='#5a635f'

def scrp_btn4_hover(e):
    scrp_btn4["bg"]="#434a47"

def scrp_btn4_hover_leave(e):
    scrp_btn4["bg"]='#5a635f'

def edit():
    global pop
    pop=Toplevel(window)

    sw=window.winfo_screenwidth()
    sh=window.winfo_screenheight()
    w=600
    h=500
    x=(sw/2)-(w/2)
    y=(sh/2)-(h/2)

    pop.title("Update Book")
    pop.geometry(f'{w}x{h}+{int(x)}+{int(y)}')
    pop.config(bg='#6d7872')

    title_entry=Entry(pop,font=('Helvetica',10,'italic'))
    title_entry.insert(END,"Title")
    title_entry.config(background='#6d7872',border=2)
    title_entry.place(x=20,y=60)

    author_entry=Entry(pop,font=('Helvetica',10,'italic'))
    author_entry.insert(END,"Author Name")
    author_entry.config(background='#6d7872',border=2)
    author_entry.place(x=20,y=160)

    id_entry=Entry(pop,font=('Helvetica',10,'italic'))
    id_entry.insert(END,"Call No/ISBN")
    id_entry.config(background='#6d7872',border=2)
    id_entry.place(x=20,y=260)

    yr_entry=Entry(pop,font=('Helvetica',10,'italic'))
    yr_entry.insert(END,"Publish Year")
    yr_entry.config(background='#6d7872',border=2)
    yr_entry.place(x=20,y=360)

    price_entry=Entry(pop,font=('Helvetica',10,'italic'))
    price_entry.insert(END,"Price")
    price_entry.config(background='#6d7872',border=2)
    price_entry.place(x=370,y=60)

    rating_entry=Entry(pop,font=('Helvetica',10,'italic'))
    rating_entry.insert(END,"Rating")
    rating_entry.config(background='#6d7872',border=2)
    rating_entry.place(x=370,y=160)

    stock_combox=ttk.Combobox(pop,value=('In stock','Not in stock'),width=21)
    stock_combox.current(0)
    stock_combox.set("Stock Status")
    stock_combox.place(x=370,y=260)

    update_btn=Button(pop,text="Update",font=('Helvetica',10,'italic'),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)    
    update_btn.place(x=370,y=360)

    title_lbl=Label(pop,text="Title:",font=('Helvetica',10,'bold','underline'),fg='black',bg='#6d7872',padx=15,pady=15)
    title_lbl.place(x=5,y=10)

    author_lbl=Label(pop,text="Author Name:",font=('Helvetica',10,'bold','underline'),fg='black',bg='#6d7872',padx=15,pady=15)
    author_lbl.place(x=5,y=110)

    id_lbl=Label(pop,text="Call No/ID:",font=('Helvetica',10,'bold','underline'),fg='black',bg='#6d7872',padx=15,pady=15)
    id_lbl.place(x=5,y=210)

    yr_lbl=Label(pop,text="Publish Year:",font=('Helvetica',10,'bold','underline'),fg='black',bg='#6d7872',padx=15,pady=15)
    yr_lbl.place(x=5,y=310)

    price_lbl=Label(pop,text="Price:",font=('Helvetica',10,'bold','underline'),fg='black',bg='#6d7872',padx=15,pady=15)
    price_lbl.place(x=353,y=10)

    rating_lbl=Label(pop,text="Rating:",font=('Helvetica',10,'bold','underline'),fg='black',bg='#6d7872',padx=15,pady=15)
    rating_lbl.place(x=353,y=110)

    stock_lbl=Label(pop,text="Stock Status:",font=('Helvetica',10,'bold','underline'),fg='black',bg='#6d7872',padx=15,pady=15)
    stock_lbl.place(x=353,y=210)




def scrapwindow():
    pass

def dashboard_window():
    global window

    columns=['1','2','3','4','5']
    order=['1','2','3','4','5']
    algos=['1','2','3','4','5']

    db_header=Frame(window,bg='#5a635f')
    db_header.place(x=165,y=0, width=1600,height=110)    
        
    db_frm1=Frame(window,bg='#6d7872')
    db_frm1.place(x=165,y=110, width=500,height=730)   #f1

    db_frm2=Frame(window,bg='#6d7872')                  ##e5edbb
    db_frm2.place(x=640,y=300, width=1000,height=600)

    db_frm3=Frame(window,bg='#6d7872')
    db_frm3.place(x=665,y=110, width=1000,height=190)

    db_lbl=Label(db_header,text="Book Dashboard",font=('Helvetica',45,'bold'),fg='black',bg='#5a635f',padx=15,pady=15)
    db_lbl.place(x=470,y=0)

    
    #style = ttk.Style()
    #style.configure(background='#6d7872')

    
    col_combox=ttk.Combobox(db_frm1,value=columns, width=52)
    col_combox.current(0)
    col_combox.set("Select Column")
    col_combox.place(x=100,y=100)
 

    algo_combox=ttk.Combobox(db_frm1,value=algos, width=52)
    algo_combox.current(0)
    algo_combox.set("Select Algorithm")
    algo_combox.place(x=100,y=150)

    order_combox=ttk.Combobox(db_frm1,value=order, width=52)
    order_combox.current(0)
    order_combox.set("Select Order")
    order_combox.place(x=100,y=200)

    add_btn=Button(db_frm1,text="Add Level",font=('Helvetica',14),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)
    add_btn.bind("<Enter>",add_btn_hover)
    add_btn.bind("<Leave>",add_btn_hover_leave)
    add_btn.place(x=335,y=240)

    level_listb=Listbox(db_frm1,bg='#5a635f',width=55)
    #level_listb.config(height=scrp_listb.size()) #for changing the height dynamically
    level_listb.place(x=100,y=300)

    txt=Text(db_frm1,width=41,height=12,font=('Helvetica',11))
    txt.config(background='#5a635f')
    #txt.insert(0, "Time Analysis of all Levels")
    txt.place(x=100,y=500)

    op_combox=ttk.Combobox(db_frm3,value=columns, width=45)
    op_combox.current(0)
    op_combox.set("Operation(Is Equal etc)")
    op_combox.place(x=450,y=53)
 

    col2_combox=ttk.Combobox(db_frm3,value=algos, width=45)
    col2_combox.current(0)
    col2_combox.set("Column Check Boxes")
    col2_combox.place(x=450,y=103)

    operator_combox=ttk.Combobox(db_frm3,value=algos, width=45)
    operator_combox.current(0)
    operator_combox.set("Operator(Contains etc)")
    operator_combox.place(x=450,y=153)

    search_string=Entry(db_frm3,font=('Helvetica',10),width=35)
    search_string.insert(END,"Search String")
    search_string.config(background='#6d7872',border=2)
    search_string.place(x=150,y=153)

    search_string2=Entry(db_frm3,font=('Helvetica',10),width=35)
    search_string2.insert(END,"Search String")
    search_string2.config(background='#6d7872',border=2)
    search_string2.place(x=150,y=53)

    operator2_combox=ttk.Combobox(db_frm3,value=algos, width=38)
    operator2_combox.current(0)
    operator2_combox.set("Operator(AND OR NOT)")
    operator2_combox.place(x=150,y=103)

    clrflt_btn=Button(db_frm3,text="Clear Filter",font=('Helvetica',14),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)    
    clrflt_btn.place(x=780,y=70)

    search_btn=Button(db_frm3,text="Search",font=('Helvetica',14),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)    
    search_btn.place(x=795,y=120)

    lbl1=Label(db_frm3,text="Multi Level Searching :",font=('Helvetica',14,'underline'),fg='black',bg='#6d7872',pady=20)
    lbl1.place(x=350,y=-15)

    lbl2=Label(db_frm1,text="Multi Level Sorting :",font=('Helvetica',14,'underline'),fg='black',bg='#6d7872',pady=20)
    lbl2.place(x=100,y=-15)

    lbl3=Label(db_frm2,text="Delete",font=('Helvetica',10,),fg='black',bg='#6d7872',pady=20)
    lbl3.place(x=200,y=3)

    lbl3=Label(db_frm2,text="Update",font=('Helvetica',10,),fg='black',bg='#6d7872',pady=20)
    lbl3.place(x=100,y=3)

    del_btn=Button(db_frm2,text="Del",font=('Helvetica',10),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0)    
    del_btn.place(x=200,y=45)
    
    edit_btn=Button(db_frm2,text="Edit",font=('Helvetica',10),fg='black',bg='#5a635f',activeforeground='black',activebackground='#545c57',borderwidth=0,command=edit)    
    edit_btn.place(x=100,y=45)


    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",background='#6d7872',foreground="black",rowheight=25,fieldbackground="silver")
    style.map('Treeview',background=[('selected','silver')])


    table=ttk.Treeview(db_frm2,height=7)  #27 full
    table['columns']=("Title","Author","Year","Call No","Stock","Price","Rating")
    table.column("#0", width=0, stretch=NO)
    #table.column("Update",anchor=W, width=70)
    #table.column("Delete",anchor=W, width=70)
    table.column("Title",anchor=W, width=70)
    table.column("Author",anchor=W, width=70)
    table.column("Year",anchor=W, width=70)
    table.column("Call No",anchor=W, width=70)
    table.column("Stock",anchor=W, width=70)
    table.column("Price",anchor=W, width=70)
    table.column("Rating",anchor=W, width=70)


    #table.heading("Update",text="Update",anchor=W)
    #table.heading("Delete",text="Delete",anchor=W)
    table.heading("Title",text="Title",anchor=W)
    table.heading("Author",text="Author",anchor=W)
    table.heading("Year",text="Year",anchor=W)
    table.heading("Call No",text="Call No",anchor=W)
    table.heading("Stock",text="Stock",anchor=W)
    table.heading("Price",text="Price",anchor=W)
    table.heading("Rating",text="Rating",anchor=W)

    #table.insert(parent='',index='end',iid=0,text="",values=("content","content","content","content","content","content","content","content","content"))
    #table.insert(parent='',index='end',iid=1,text="",values=("content","content","content","content","content","content","content","content","content"))
    table.insert(parent='',index='end',iid=2,text="",values=("content","content","content","content","content","content","content"))
    table.insert(parent='',index='end',iid=3,text="",values=("content","content","content","content","content","content","content"))
    table.insert(parent='',index='end',iid=4,text="",values=("content","content","content","content","content","content","content"))
    table.insert(parent='',index='end',iid=5,text="",values=("content","content","content","content","content","content","content"))
    table.insert(parent='',index='end',iid=6,text="",values=("content","content","content","content","content","content","content"))
    table.place(x=275,y=20)
    #table.pack(side=TOP,fill=BOTH)
    













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

logo=PhotoImage(file='E:\\Semester 3\\icon4_resized.png')
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
scrp_entry.config(background='#6d7872',border=2)
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
Scrap=Label(header,text="Scrapping",font=('Helvetica',45,'bold'),fg='black',bg='#5a635f',padx=15,pady=15)
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