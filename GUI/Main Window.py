from tkinter import *

def close():
    window.destroy()


window=Tk()
logo=PhotoImage(file=r'D:\BACHELOR OF COMPUTER SCIENCE\SECOND YEAR\3.THIRD SEMESTER\DSA\DSA LAB\MID PROJECT\dsa-mid-project\PNGS FOR GUI\cloud-mining.png')
logo_lbl=Label(image=logo,bg='#6d7872',padx=15,pady=15)
logo_lbl.place(x=18,y=-2)

window.geometry("1920x1080")
window.title("Library Management System")
pic=PhotoImage(file=r'D:\BACHELOR OF COMPUTER SCIENCE\SECOND YEAR\3.THIRD SEMESTER\DSA\DSA LAB\MID PROJECT\dsa-mid-project\PNGS FOR GUI\cloud-mining.png')
window.iconphoto(True,pic)
Scrap=Label(window,text="Scrapping",font=('Helvetica',45,'bold'),fg='black',bg='#6d7872',padx=15,pady=15)
Scrap.place(y=-2)
Scrap.pack()
title=Label(window,text="LMS",font=('Garamond',45,'bold'),fg='black',bg='#6d7872',padx=15,pady=15)
title.place(x=5,y=110)
groupnum=Label(window,text="Group 03",font=('Helvetica',15,'bold','italic'),fg='black',bg='#6d7872',padx=10,pady=10)
groupnum.place(x=27,y=180)


#icon pics not showing
scrap_btn=PhotoImage(file=r'D:\BACHELOR OF COMPUTER SCIENCE\SECOND YEAR\3.THIRD SEMESTER\DSA\DSA LAB\MID PROJECT\dsa-mid-project\PNGS FOR GUI\cloud-mining.png')
dashboard_btn=PhotoImage(file=r'D:\BACHELOR OF COMPUTER SCIENCE\SECOND YEAR\3.THIRD SEMESTER\DSA\DSA LAB\MID PROJECT\dsa-mid-project\PNGS FOR GUI\cloud-mining.png')
exit_btn=PhotoImage(file=r'D:\BACHELOR OF COMPUTER SCIENCE\SECOND YEAR\3.THIRD SEMESTER\DSA\DSA LAB\MID PROJECT\dsa-mid-project\PNGS FOR GUI\cloud-mining.png')

scrap_btn=Button(window,text="Scrap-Data",font=('Helvetica',18),fg='black',bg='#6d7872',activeforeground='black',activebackground='#545c57',borderwidth=0)#,image=scrap_btn,compound='left')
scrap_btn.pack()
scrap_btn.place(x=15,y=250)
dashboard_btn=Button(window,text="Dashboard ",font=('Helvetica',18),fg='black',bg='#6d7872',activeforeground='black',activebackground='#545c57',borderwidth=0)#,image=dashboard_btn,compound='left')
dashboard_btn.pack()
dashboard_btn.place(x=15,y=300)
exit_btn=Button(window,text="Exit",command=close, font=('Helvetica',18),fg='black',bg='#6d7872',activeforeground='black',activebackground='#545c57',borderwidth=0)#,image=exit_btn,compound='left')
exit_btn.pack()
exit_btn.place(x=15,y=350)

window.config(background="#6d7872")
window.mainloop()