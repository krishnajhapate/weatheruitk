from tkinter import *
import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image
import requests
from tkinter import messagebox


class Weather():

    def weather_report(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?q="
        self.cityname = self.loc.get(1.0, END)
        self.api_key = 'bf4764269a6343d9021dd620a5ddf903'
        self.data = requests.get(
            self.url + self.cityname + '&appid='+ self.api_key
        ).json()

        if self.data['cod'] == '404':
            messagebox.showerror("Error", 'City not found !!')

        else:
            self.location['text'] = self.data['name'] + ","+self.data['sys']['country']
            self.c = self.data['main']['temp_max'] - 273.15
            self.f = self.c*9/5 + 35
            self.weather['text'] = self.data['weather'][0]['main']
            self.weather['font'] = ('veranda', 10, 'bold')
            self.temprature['text'] = f'{round(self.c,2)}°C/{round(self.f)}°F'
            self.temprature['font'] = ('veranda', 10, 'bold')
            self.humidity['text'] = self.data['main']['humidity']
            self.humidity['font'] = ('veranda', 10, 'bold')
            self.pressure['text'] = self.data['main']['pressure']
            self.pressure['font'] = ('veranda', 10, 'bold')

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title("Weather Application")
        self.root.maxsize(500, 300)
        self.root.minsize(500, 300)
        self.header = Label(self.root, width=100, height=2, bg="midnight blue")
        self.header.place(x=0, y=0)
        self.font = ('veranda', 10, 'bold')
        self.date = Label(self.root, text=datetime.now().date(),bg="midnight blue",fg='white',font=self.font)
        self.date.place(x=420,y=7)
        self.heading = Label(self.root,text="Weather Report",bg="midnight blue",font=self.font,fg="white")
        self.heading.place(x=180,y=5)
        self.location = Label(self.root,text="",bg="midnight blue",fg="white",font=self.font)
        self.location.place(x=10,y=5)
        self.img = ImageTk.PhotoImage(Image.open('Weather.png').resize((140, 140)))
        self.image = Label(self.root,image=self.img)
        self.image.place(x=7,y=40)
        self.name = Label(self.root,text="City or Country Name",fg="midnight blue",font=self.font)
        self.name.place(x=145,y=50)
        self.loc =Text(self.root,width=25,height=1.2,font=5)
        self.loc.place(x=140,y=70)
        self.button = Button(self.root,text="Search",bg="midnight blue",fg='white',font=self.font,relief=RAISED,borderwidth=3,command=self.weather_report)
        self.button.place(x=350,y=70)
        self.line1=Label(self.root,bg="midnight blue",width=20,height=0)
        self.line1.place(x=0,y=150)
        self.line2 = Label(self.root,bg="midnight blue",width=20,height=0)
        self.line2.place(x=360,y=150)
        self.report = Label(self.root,text="Weather Report",fg="midnight blue",font=self.font,padx=10)
        self.report.place(x=180,y=150)

        self.img2= ImageTk.PhotoImage(Image.open('23648-2-weather-picture-thumb.png').resize((100,100)))
        self.image2=Label(self.root,image=self.img2)
        self.image2.place(x=23,y=180)
        self.weather = Label(self.root,text="",fg="midnight blue",font=self.font)
        self.weather.place(x=40,y=270)
        self.img3 = ImageTk.PhotoImage(Image.open('1035618.png').resize((80,80)))
        self.image3 = Label(self.root,image=self.img3)
        self.image3.place(x=140,y=180)
        self.temprature = Label(self.root,text="",fg="midnight blue",font=self.font)
        self.temprature.place(x=150,y=270)


        
        self.img4= ImageTk.PhotoImage(Image.open('humidity-25-781162.webp').resize((80,80)))
        self.image4=Label(self.root,image=self.img4)
        self.image4.place(x=260,y=180)
        self.humidity = Label(self.root,text="",fg="midnight blue",font=self.font)
        self.humidity.place(x=290,y=270)
        self.img5 = ImageTk.PhotoImage(Image.open('1839341.png').resize((80,80)))
        self.image5 = Label(self.root,image=self.img5)
        self.image5.place(x=380,y=180)
        self.pressure = Label(self.root,text="",fg="midnight blue",font=self.font)
        self.pressure.place(x=410,y=270)



        self.root.mainloop()



if __name__ == "__main__":
    Weather()
