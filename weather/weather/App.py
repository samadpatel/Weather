

import json
import requests
from tkinter import *
from PIL import ImageTk,Image

# Required Details
root = Tk()

#Geometry of the window
root.geometry("320x320")

#Title of the Window app
root.title("Weather App")

#Set background color
root.configure(bg='yellow')

#Label to display the Header
lable_0 = Label(root,text="Weather App",width = 20,bg='yellow',font=("bold",20),fg='black')
lable_0.place(x=0,y=20)



#Declare city names as string and take the entry
city_names = StringVar()
entry_1 = Entry(root,textvariable=city_names)
entry_1.place(x=95,y=140)
#label to accept city entry
lable_city = Label(root,text="City :",width = 10,bg='yellow',font=("bold",10),fg='black')
lable_city.place(x=9,y=140)


# api config
def getTemp():

    api_key = "c4e430e7cffeaea0ae2f36a02fd5550b"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = entry_1.get()
    complete_url = base_url+"q="+city_name+"&APPID="+api_key

# module response get
    response = requests.get(complete_url)
    x=response.json()

    if["cod"] !='404':
        y = x["main"]
        current_temperature = y["temp"]
        current_temp=round((current_temperature-273.15),2)
        lable_2 = Label(root,text="Temperature for "+city_name+" is:",width = 25,bg='yellow',font=("bold",10),fg='black')
        lable_2.place(x=40,y=220)
        lable_temp = Label(root,text="...",width = 5,bg='yellow',font=("bold",10),fg='black')
        lable_temp.place(x=100,y=250)
        lable_temp.configure(text=str(current_temp)+"°C")
        farenhiet = round((current_temp * 9/5) + 32 ,2)
        lable_temp2 = Label(root,text="...",width = 5,bg='yellow',font=("bold",10),fg='black')
        lable_temp2.place(x=100,y=280)
        lable_temp2.configure(text=str(farenhiet)+"F")
       
    else:
        
        lable_temp.configure(text="Err")
      
#Submit button specifications
Button(root,text="Submit",width=10,bg='brown',fg='white',command=getTemp).place(x=95,y=170)
Button.pack

mainloop()