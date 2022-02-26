from tkinter import *
import pygame
import random
import time
from pygame import mixer
from threading import Thread
import threading


pygame.mixer.init()
root=Tk()
root.title("Image button")
root.geometry("300x300")


cry=PhotoImage(file="c:\\Users\\vulon\\OneDrive\\Tài liệu\\python\\tkinter\\slide\\cry.png")
mute=PhotoImage(file="c:\\Users\\vulon\\OneDrive\\Tài liệu\\python\\tkinter\\mute.png")
back=PhotoImage(file="c:\\Users\\vulon\\OneDrive\\Tài liệu\\python\\tkinter\\back.png")
next=PhotoImage(file="c:\\Users\\vulon\\OneDrive\\Tài liệu\\python\\tkinter\\next.png")

diem=0
score=Canvas(root,width=300,height=100,bg="white")
score.create_text(150,50,text="Score: "+str(diem),fill="green",font=("Times",40))
score.place(x=600,y=0)
#timer
time_finish=Canvas(root,width=200,height=100,bg="Red")
thoi_gian=120
time_finish.create_text(100,50,text="Time: "+str(thoi_gian),fill="yellow",font=("Times",24))
time_finish.place(x=800,y=100)
#nut bat dau

def song():
    mixer.music.load('c:\\Users\\vulon\\OneDrive\\Tài liệu\\python\\tkinter\\slide\\Beach-Volley.wav')
    mixer.music.play()
da_a=0
da_b=0
da_c=0
da_d=0
first=0
second=0
answer=[]
def dap_an():
    global da_a,da_b,da_c,da_d,first,second,answer
    first=random.randint(10,100)
    second=random.randint(10,100)
    answer=[first+second,first+second+random.randint(1,10),first+second+random.randint(-10,-1),first-second+random.randint(1,5)]
    da_a=random.choice(answer)
    #da_b!=da_a
    da_b=random.choice(answer)
    while da_b==da_a:
        da_b=random.choice(answer)
    da_c=random.choice(answer)
    while da_c==da_b or da_c==da_a :
        da_c=random.choice(answer)
    da_d=random.choice(answer)
    while da_d==da_a or da_d==da_b or da_d==da_c:
        da_d=random.choice(answer)
dap_an()
root.update()
def stop_song():
    mixer.music.pause()
def turn_sound():
    mixer.music.unpause()
def play_song(a):
    global button1,button2,button3,button4,diem,cry,thoi_gian
    if a==answer[0]:
        if thoi_gian>=0:
                thoi_gian+=2
                diem+=1
                #tang diem
                score.delete("all")
                score.create_text(150,50,text="Score: "+str(diem),fill="green",font=("Times",40))
                dap_an()
                renew()
    elif a!=answer[0] and diem>=0 and thoi_gian>=0:
        diem-=1
        score.delete("all")
        score.create_text(150,50,text="Score: "+str(diem),fill="green",font=("Times",40))
        if diem==-1:
            khoc=Label(root,image=cry)
            khoc.place(x=250,y=250)
            #end root
            #root.after(500,root.destroy)
            
def renew():
        global button1,button2,button3,button4,da_a,da_b,da_c,da_d,first,second,answer,thoi_gian
        if thoi_gian!=0:
            board.delete(ALL)
            board.create_text(150,150,text=str(first)+"+"+str(second)+"=",fill="green",font=("Times",40))
            board.place(x=0,y=200)
            #delete button
            button1.destroy()
            button2.destroy()
            button3.destroy()
            button4.destroy()
            #create new button
            button1=Button(root,text=str(da_a),padx=40,pady=10,fg="Green",bg="orange",command=lambda:play_song(da_a))
            button2=Button(root,text=str(da_b),padx=40,pady=10,fg="Green",bg="orange",command=lambda:play_song(da_b))
            button3=Button(root,text=str(da_c),padx=40,pady=10,fg="Green",bg="orange",command=lambda:play_song(da_c))
            button4=Button(root,text=str(da_d),padx=40,pady=10,fg="Green",bg="orange",command=lambda:play_song(da_d))
            button1.place(x=0,y=530)
            button2.place(x=300,y=530)
            button3.place(x=600,y=530)
            button4.place(x=900,y=530)

            root.update()




button_quit=Button(root,text="Quit game",padx=20,pady=10,fg="black",bg="white",command=root.quit)
button_quit.place(x=200,y=0)
#create a board
board=Canvas(root,width=1500,height=300,bg="black")
#write a text on the board
board.create_text(150,150,text=str(first)+"+"+str(second)+"=",fill="green",font=("Times",40))
board.place(x=0,y=200)

back=back.subsample(2,2)
next=next.subsample(2,2)
mute=mute.subsample(3,3)#giam kich thuoc anh di 3x3
sound=PhotoImage(file="c:\\Users\\vulon\\OneDrive\\Tài liệu\\python\\tkinter\\sound.png")
sound=sound.subsample(3,3)#giam kich thuoc anh di 3x3
#create a button
button1=Button(root,text=str(da_a),padx=40,pady=10,fg="Green",bg="orange",command=lambda:play_song(da_a),state=DISABLED)
button2=Button(root,text=str(da_b),padx=40,pady=10,fg="Green",bg="orange",command=lambda:play_song(da_b),state=DISABLED)
button3=Button(root,text=str(da_c),padx=40,pady=10,fg="Green",bg="orange",command=lambda:play_song(da_c),state=DISABLED)
button4=Button(root,text=str(da_d),padx=40,pady=10,fg="Green",bg="orange",command=lambda:play_song(da_d),state=DISABLED)
#không cho chon đáp án trước khi tính thời gian
button1.place(x=0,y=530)
button2.place(x=300,y=530)
button3.place(x=600,y=530)
button4.place(x=900,y=530)
#when start game then botton enable


def test():
    global button1,button2,button3,button4
    threading.Thread(target=finish_game).start()
    #khi bắt đầu tính thời gian thì được chọn đáp án
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    return 0



#sound and mute
bt_mute=Button(root,image=mute,command=lambda:stop_song())
bt_sound=Button(root,image=sound,command=lambda:song())
bt_mute.grid(row=0,column=10)
bt_sound.grid(row=0,column=9)

def finish_game():
    global thoi_gian,diem
    while thoi_gian>0:
        thoi_gian-=1
        root.update()
        time.sleep(1)
        #sleep time 1 second
        time_finish.delete("all")
        time_finish.create_text(100,50,text="Time: "+str(thoi_gian),fill="yellow",font=("Times",24))
        time_finish.place(x=800,y=100)
    if thoi_gian==0:
        khoc=Label(root,image=cry)
        khoc.place(x=250,y=250)
        #dừng không cho chọn đáp án nữa
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)

    #end root
    '''root.after(500,root.destroy)'''
    return 0
#thread time
bat_dau=PhotoImage(file="c:\\Users\\vulon\\OneDrive\\Tài liệu\\python\\tkinter\\slide\\images.png")
bat_dau=bat_dau.subsample(2,2)
bt_batdau=Button(root,image=bat_dau,command=lambda:test())
bt_batdau.place(x=900,y=0)
#detect bt_batdau press
root.mainloop()