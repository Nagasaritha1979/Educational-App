from tkinter import *
from PIL import Image,ImageTk

win=Tk()
win.geometry('400x600')
win.title("EDUCATOR")
win.config(bg='#b6d7a8')
win.resizable(False,False)

list1=['Astrophysics','Productivity','Psychology','Leadership','History']

count=0
running_text=''


def click():
    
    def show_less():
        
        etc_btn.config(text='and more ......',fg='green')
        subject6_btn.place_forget()
        subject7_btn.place_forget()
        show_less_btn.place_forget()
        
        
    etc_btn.config(text='Physics',fg='black')
    
    subject6_btn=Button(win,text='Chemistry',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
    subject6_btn.place(x=5,y=200)
    
    subject7_btn=Button(win,text='Biology',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
    subject7_btn.place(x=5,y=220)
    
    show_less_btn=Button(win, text='Show Less',cursor='hand2',command=show_less,activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='green')
    show_less_btn.place(x=5,y=240)

title1_label=Label(win,text="The Best Way",bg='#b6d7a8', font=("Calibri",15,'bold'),fg='black')
title1_label.place(x=5,y=10)

title2_label=Label(win,text='to Learn',bg='#b6d7a8',font=("Calibri",15,'bold'),fg='black')
title2_label.place(x=5,y=40)

subject1_btn=Button(win,text='Philosophy',activebackground='#b6d7a8',font=("Calibri",10),cursor='hand2',bd=0,bg='#b6d7a8',fg='black')
subject1_btn.place(x=5,y=80)

subject2_btn=Button(win,text='Psychology',activebackground='#b6d7a8',cursor='hand2',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
subject2_btn.place(x=5,y=100)

subject3_btn=Button(win,text='Personal Development',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
subject3_btn.place(x=5,y=120)

subject4_btn=Button(win,text='Economics',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
subject4_btn.place(x=5,y=140)

subject5_btn=Button(win,text='History',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
subject5_btn.place(x=5,y=160)

etc_btn=Button(win,text='and more ......',cursor='hand2',command=click,activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='green')
etc_btn.place(x=5,y=180)

photo=Image.open('imprint.png')
photo1=photo.resize((200,500))
photo_img=ImageTk.PhotoImage(photo1,master=win)

label1=Label(win,image=photo_img)
label1.place(x=175,y=50)

footer_label=Label(win,text='EDUCATOR - Learn Visually',bg='#b6d7a8',font=("Calibri",15,'bold'),fg='black')
footer_label.place(x=5,y=575)

label1_text=Label(win,text='See',bg='#b6d7a8')
label1_text.place(x=5,y=280)

label2_text=Label(win,font=("Arial",10),fg='dark blue',bg='#b6d7a8')
label2_text.place(x=5,y=300)


label3_text=Label(win,text='in a whole new',bg='#b6d7a8')
label3_text.place(x=5,y=320)

label4_text=Label(win,text='way',bg='#b6d7a8')
label4_text.place(x=5,y=340)

def run_text(val):
    global count,running_text
    
    if count==len(val):
        print(count)
        count=0
        running_text=''
        return()
    
    else:
        running_text+=val[count]
        print(running_text)
        
        win.update()
        label2_text.config(text=running_text)
        
        print('value=',val)
        count+=1
        label2_text.after(150,run_text(val))
        win.update()

while True:
    for text1 in list1:
        run_text(text1)
win.mainloop()

