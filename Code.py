from tkinter import*
import random
window=Tk()
window.title("Rock,Paper,Scissor Game")
window.geometry("750x450")
window.iconbitmap("./rock.ico")
l=LabelFrame(window,text="Rock,Paper,Scissor",font=("Arial 20 bold"),fg="blue",bg="#FFCBA4",width=600,height=400)
l.pack(expand=YES,fill=BOTH)
t=Label(l,text="Lets start the game...",font=("Arial 16"),fg="green")
t.pack()
l1=Label(l,text="Player",font=("Helvetica 18 bold"),fg="Black",bg="white")
l1.place(relx= .18, rely= .1)
l2=Label(l,text="VS",font=("Helvetica 18 bold"),fg="Black",bg="white")
l2.place(relx= .45, rely= .1)
l3=Label(l,text="Computer",font=("Helvetica 18 bold"),fg="Black",bg="white")
l3.place(relx= .65, rely= .1)
computer_value={"0":"Rock","1":"Paper","2":"Scissor"}
label= Label(l, text="", font=('Coveat', 25,'bold'), bg= "khaki3")
label.pack(pady=150)
l4=Label
player_choice_label=Label(l,text="",font=("Helvetica 18 bold"),fg="red",bg="white")
player_choice_label.place(relx= .18, rely= .3)
computer_value_label=Label(l,text="",font=("Helvetica 18 bold"),fg="red",bg="white")
computer_value_label.place(relx=.65,rely=.3)

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

def isrock():
    
    player_choice_label.config(text = 'Rock')
    cv=computer_value[str(random.randint(0,2))]
    computer_value_label.config(text=cv)
    if cv=="Rock":
        result="Match draws"
    elif cv=="Scissor":
       result="You Won!!!"
    elif cv=="Paper":
        result="Computer Won!!!"
    label.config(text=result)
    button_disable()

def ispaper():
    player_choice_label.config(text = 'Paper')
    cv=computer_value[str(random.randint(0,2))]
    computer_value_label.config(text=cv)
    if cv=="Rock":
        result="You Won!!!"
    elif cv=="Scissor":
        result="Computer Won!!!"
    elif cv=="Paper":
        result="Match draws"
    label.config(text=result)
    button_disable()

def isscissor():
    player_choice_label.config(text = 'Scissor')
    cv=computer_value[str(random.randint(0,2))]
    computer_value_label.config(text=cv)
    if cv=="Rock":
        result="Computer Won!!!"
    elif cv=="Scissor":
        result="Match draws"
    elif cv=="Paper":
        result="You won!!!"
    label.config(text=result)
    button_disable()
def reset():
   b1.config(state= "active")
   b2.config(state= "active")
   b3.config(state= "active")
   player_choice_label.config(text = "")
   computer_value_label.config(text = "")
   label.config(text = "")
b1= Button(l, text= "Rock", font= 10, width= 7,bg="#CBA3FF",command= lambda:isrock())
b1.place(relx=.25, rely= .62)
b2= Button(l, text= "Paper", font= 10, width= 7 ,bg="#CBA3FF",command=lambda:ispaper())
b2.place(relx= .41,rely= .62)
b3= Button(l, text= "Scissor", font= 10, width= 7,bg="#CBA3FF", command=lambda:isscissor())
b3.place(relx= .58, rely= .62)
b4= Button(l, text= "Reset", font= 10, width= 7,bg="Orange",command=lambda:reset())
b4.place(relx= .8, rely= .62)

window.mainloop()