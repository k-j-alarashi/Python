from random import *
import tkinter as tk

# يجب تنزيل هذه المكتبة لأضافة الصورة
# يجب تنزيل المكتبة بهذا الاسم
from PIL import Image , ImageTk

game_list = ['rock' , 'paper', 'scissor']
win_Label=''
user_Label=''
computer_Label=''
user_point=0
computer_point=0

def computerChoice():
    cc = randint(0,2)
    return game_list[cc]

def winnerChoice(user , computer):
    global win_Label , user_Label , computer_Label , user_point , computer_point
    
    if user==computer:
        win_Label.config(text='Draw' , fg='black')
    elif (
        (user=='rock' and computer=='scissor') or
        (user=='scissor' and computer=='paper') or
        (user=='paper' and computer=='rock')
          ):
        user_point+=1
        win_Label.config(text='Win',fg='green')
    else:
        computer_point+=1
        win_Label.config(text='Lose',fg='red')
        
    user_Label.config(text=f'user :\n{user}\n{user_point}')
    computer_Label.config(text=f'Computer :\n{computer}\n{computer_point}')

root = tk.Tk()
root.geometry('1000x400')
title = tk.Label(root , text='Game' , font=('bold',30))
title.place(x=440 , y=0)

rock_img = Image.open('images\\rock.jpg')
rock_img = rock_img.resize([100,100])
rock_img = ImageTk.PhotoImage(rock_img)
rock_btn = tk.Button(root , image=rock_img , command=lambda:winnerChoice('rock' , computerChoice()))
rock_btn.place(x=200 , y=100)

paper_img = Image.open('images\\paper.png')
paper_img = paper_img.resize([100,100])
paper_img = ImageTk.PhotoImage(paper_img)
paper_btn = tk.Button(root , image=paper_img, command=lambda:winnerChoice('paper' , computerChoice()))
paper_btn.place(x=440 , y=100)

scissor_img = Image.open('images\\scissor.png')
scissor_img = scissor_img.resize([100,100])
scissor_img = ImageTk.PhotoImage(scissor_img)
scissor_btn = tk.Button(root , image=scissor_img, command=lambda:winnerChoice('scissor' , computerChoice()))
scissor_btn.place(x=670 , y=100)

win_Label = tk.Label(text='' , font=('bold',22))
win_Label.place(x=450,y=300)

user_Label = tk.Label(text=f'user\n{user_point}' , font=('bold',22))
user_Label.place(x=110,y=250)

computer_Label = tk.Label(text=f'computer\n{computer_point}' , font=('bold',22))
computer_Label.place(x=790,y=250)

root.mainloop()