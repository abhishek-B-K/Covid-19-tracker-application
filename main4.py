from datetime import time
from turtledemo import clock
from twilio.rest import Client
import covid
import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import ttk
from tkinter import *
import time
from tkinter import messagebox,filedialog
from PIL import Image,ImageTk
import webbrowser as wb

import random
account_sid = ""

auth_token  = ""

def callback(url):
    wb.open_new(url)

def open_window():
    top = Toplevel()
    top.geometry("100x100+350+250")
    wb.open_new(r"COVID.pdf")

def send_sms(number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=number,
        from_="+19285998314",
        body=message)
    print(message.sid)

def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(1000,tick)

colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(1000,IntroLabelColorTick)
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(300,IntroLabelTick)

def show_data():
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

    data = covid.Covid()
    country_name = e1.get()

    #status = data.get_status_by_country_name(country_name)
    status = data.get_status_by_country_name(country_name)
    active = status['active']
    e2.insert(0,active)
    death = status['deaths']
    e3.insert(0, death)
    confirm = status['confirmed']
    e4.insert(0, confirm)
    recover = status['recovered']
    e5.insert(0, recover)
    print(status)
    # intialise data of lists.
    data = {'id': status['id'],
            'Country': status['country'],
            'Confirmed': status['confirmed'],
            'Active': status['active'],
            'Deaths': status['deaths'],
            'Recovered': status['recovered'],
            'Latitude': status['latitude'],
            'Longitude': status['longitude'],
            'Last_Updated': status['last_update']
            }

    # Create DataFrame
    df = pd.DataFrame(data, index=[0])

    # Print the output.
    print(df)
    cadr = {

        key:status[key]
        for key in status.keys() & {"confirmed","active","deaths","recovered"}
    }
    n = list(cadr.keys())
    v = list(cadr.values())
    plt.title("Country")
    plt.bar(range(len(cadr)),v,tick_label=n,label=('active'))
    plt.xlabel('x-labels')
    plt.ylabel('data')

    plt.plot(range(len(cadr)))


    plt.show()

master = tk.Tk()
master.geometry("1174x700+200+50")
master.title("COVID - 19 INFORMATION SYSTEM")
master.iconbitmap('cc.ico')
master.resizable(False,False)
master.config(bg='LightSkyBlue1')

image = Image.open("bb.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(master,image=photo,bg='white')
label.pack(side='bottom',fill='both',expand='yes')

ss = 'COVID - 19 INFORMATION SYSTEM'
count = 0
text = ''

clock = Label(master,font=('Times new roman',14,'bold'),relief=RIDGE,borderwidth=4,bg='LightSkyBlue1')
clock.place(x=0,y=0)
tick()

SliderLabel = Label(master,text=ss,font=('Times new roman',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='LightSkyBlue1')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()



lab1 = tk.Label(master,text="COVID-19 COUNTRY STATUS" ,padx=50,font=('Times new roman',15,'bold'), bg='pink')
lab1.place(x=20,y=100)


lab2 = tk.Label(master,text="Enter Country Name : ",padx=50,font=('Times new roman',13,'bold'))
lab2.place(x=15,y=140)
lab2.config(bg='LightSkyBlue1')

n = tk.StringVar()
e1 = ttk.Combobox(master,width=20,textvariable=n)
e1.place(x=320,y=143)

e1['values'] = ('India','Russia','Canada','Brazil','Peru', 'Mexico','South Africa','France','Italy','China','Poland','Spain','iran','United Kingdom')

btn1 = tk.Button(master,text='Show', command=show_data,width=15,font=('Times New Roman',10,'bold'),bd=4,bg='thistle1',activebackground='thistle2',relief=RIDGE,fg='orangered2')
btn1.place(x=320,y=180)

lb3 = tk.Label(master, text="Active Cases : -",font=('Times new roman',12,'bold'))
lb3.place(x=15,y=180)
e2 = tk.Entry(master,bd=3)
e2.place(x=165,y=182)

lb4=tk.Label(master, text="Death Cases : -",font=('Times new roman',12,'bold'))
lb4.place(x=15,y=220)
e3 = tk.Entry(master,bd=3)
e3.place(x=165,y=222)

lb5=tk.Label(master, text="Confirmed Cases : -",font=('Times new roman',12,'bold'))
lb5.place(x=15,y=260)
e4 = tk.Entry(master,bd=3)
e4.place(x=165,y=262)

lb6=tk.Label(master, text="Recovered Cases : -",font=('Times new roman',12,'bold'))
lb6.place(x=15,y=300)
e5 = tk.Entry(master,bd=3)
e5.place(x=165,y=302)

lab7 = tk.Label(master,text="SEND MESSAGE TO WELL WISHERS" ,padx=50,font=('Times new roman',15,'bold'), bg='pink')
lab7.place(x=600,y=100)

lab8 = tk.Label(master,text="Enter Mo. Number",font=('Times new roman',12,'bold'))
lab8.place(x=600,y=180)
font = ("Helvetica", 13, "bold")
textNumber = Entry(master, font=font,bd=3)
textNumber.place(x=600,y=220)

lab9 = tk.Label(master,text="Enter message",font=('Times new roman',12,'bold'))
lab9.place(x=600,y=260)

textMsg = Text(master,height=5,width=60,bd=4)
textMsg.place(x=600,y=300)

sendBtn = Button(master, text="SEND SMS", command=btn_click,width=15,font=('Times New Roman',13,'bold'),bd=4,bg='thistle1',activebackground='thistle2',relief=RIDGE,fg='orangered2')
sendBtn.place(x=780,y=400)

bachao = Button(master,text='covid 19 precautions',command=open_window,width=18,font=('Artifex',13,'bold'),bd=4,bg='thistle1',activebackground='thistle2',relief=RIDGE,fg='orangered2')
bachao.place(x=15,y=350)


lab10 = tk.Label(master,text="WHO Website" ,padx=50,font=('Artifex',12,'bold'), width=14)
lab10.place(x=15,y=400)

link1 = Label(master, text="world health organization(WHO)", fg="blue", cursor="hand2")
link1.place(x=15,y=440)
link1.bind("<Button-1>", lambda e: callback("https://www.who.int/"))

lab11 = tk.Label(master,text="Government of India" ,padx=50,font=('Artifex',12,'bold'), width=14)
lab11.place(x=15,y=470)

link2 = Label(master, text="Ministry of Health Family Welfare Government of India", fg="blue", cursor="hand2")
link2.place(x=15,y=510)
link2.bind("<Button-1>", lambda e: callback("https://www.mohfw.gov.in/#"))

lab12 = tk.Label(master,text="Inspiring Stories" ,padx=50,font=('Artifex',12,'bold'), width=14)
lab12.place(x=15,y=540)

link3 = Label(master, text="Inspiring stories of volunteers during the coronavirus lockdown", fg="blue", cursor="hand2")
link3.place(x=15,y=580)
link3.bind("<Button-1>", lambda e: callback("https://www.artofliving.org/in-en/projects/disaster-relief/7-inspiring-stories-of-volunteer-during-coronavirus"))



lab14 = tk.Label(master,text="Made by,\nAbishek B. Kurkute (CSE)\nBhushan D. mandlik (CSE)" ,padx=50,font=('Artifex',7,'bold'), width=5,bg='lavender')
lab14.place(x=1040,y=660)

lab15 = tk.Label(master,text="The comeback is always stronger than the setback." ,font=('Book Antiqua',14,'bold'), width=38,bg='lightsteelblue1')
lab15.place(x=360,y=670)

master.mainloop()







