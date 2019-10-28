from tkinter import *
import tkinter.messagebox as msg
def click():
        global c1
        global c
        try:
                e=entry1.get()
                e=e.upper()
                if len(e)==4 and e.isalpha():
                        c=0
                        c1=['A','C','D','G']
                        t=True
                        for i in e:
                                if i not in ['A','B','C','D','E','F','G']:
                                        msg.showinfo("ALERT","PLEASE INPUT IN CORRECT FORMAT")
                                        t=False        
                                        break
                                else:
                                        while t:
                                        
                                                for j in e:
                                                        if j in c1:
                                                                c=c+1
                                                                c1[c1.index(j)]="123"
                                                if c==4:
                                                        msg.showinfo("WELL DONE","WELL DONE BRAINIAC")
                                                        t=False
                                                        moon.destroy()
                                                        exit()
                                                else:
                                                        t=False
                                                        msg.showinfo("GAME OVER","GAMEOVER TRY AGAIN")

                else:
                     msg.showinfo("ALERT","PLEASE INPUT IN CORRECT FORMAT")
        except:
                msg.showinfo("ALERT","PLEASE INPUT IN CORRECT FORMAT") 
                
                
moon=Tk()
moon.title("COMMON SENSE TEST")
moonimage=PhotoImage(file="moon.gif")
Label(moon,image=moonimage).grid(row=0)
#
Label(moon,text="""\nIt is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants\n
You have just landed,Out of the items below, which four do you bring? \n""",bg="pink",fg="black",font="none 12 bold").grid(row=1)
#
#
Label(moon,text='''A: 3 litres of water",\n
"B: An extra Spacesuit",\n
"C: A 10 day oxygen supply",\n
"D: Solar panels",\n
"E: The seeds for your mission",\n
"F: The soil for your mission",\n
"G: A 3 day food supply"\n''',bg="white",fg="black").grid(row=2,columnspan=4)
##
v=StringVar()
Label(moon,text="enter your four choices").grid(row=3,column=0)
entry1=Entry(moon)
entry1.grid(row=4,column=0)
def exit_window():
        moon.destroy()
        exit()
Button(moon,text="submit",command=click).grid(row=5,rowspan=2)
Button(moon,text="EXIT",fg="red",command=moon.destroy).grid(row=8)
moon.mainloop()
