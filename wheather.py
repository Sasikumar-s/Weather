import tkinter as tk
from tkinter import font
import requests
from distutils import command

HEIGHT = 500
WIDTH = 600

#57a1f3ee6c80a75accbae9304a3d073d (its my code)  use your code for weather
#api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml

def test_function(entry):
    print("This is an entry:",entry)

def format_response(weather):  
    
    try:  
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']
        wind=weather['wind']['speed']
        pressure=weather['main']['pressure']
        visibility=weather['visibility']


        final_str='City          :%s \nCondition     : %s \nTemperature   :%s\nWind          :%s\nPressure      :%s\nVisibility    :%s'%(name,desc,temp-273.15,wind,pressure,visibility)
    except:
        final_str='There was an problem to get an Data'

    return final_str

def get_weather(city):
    weather_key='57a1f3ee6c80a75accbae9304a3d073d'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city, 'units':'inperial'}
    response=requests.get(url,params=params)
    weather=response.json()

    label['text']=format_response(weather)

root = tk.Tk()

root.iconbitmap('D:/Project/Python Projects/iconhigh.ico')

canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()

background_image=tk.PhotoImage(file='landscape.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='#ff0066',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=('Courier',12))
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text="Get Weather",font=('GHOST RIDER MOVIE',12), command=lambda:get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame= tk.Frame(root,bg='#ff0066',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame,font=('Courier',18),anchor='nw', justify='left',bd=4)
label.place(relwidth=1,relheight=1)


root.mainloop()
