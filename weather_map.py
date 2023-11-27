import tkinter as tk
import requests
from api import api_key2
window = tk.Tk()
window.title("Weather Status Map")
window.minsize(width=300,height=300)
location = tk.Label(window,text="Location : ",padx=10,pady=10,font=15)
location.grid(column=0,row=0)
search = tk.Entry(window,width=20)
search.grid(column=1,row=0,padx=10,pady=10)
def precipitation_to_percentage(precipitation_mm):
    # Define your own thresholds based on local conditions
    light_rain_threshold = 1.0
    moderate_rain_threshold = 5.0
    heavy_rain_threshold = 10.0

    if precipitation_mm == 0:
        return 0
    elif precipitation_mm <= light_rain_threshold:
        return 30
    elif precipitation_mm <= moderate_rain_threshold:
        return 60
    elif precipitation_mm <= heavy_rain_threshold:
        return 90
    else:
        return 100
def search_w():

    api_key = api_key2()
    city = search.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    temperature =round(((data["main"]["temp"])-273.15),2)
    temp_r.config(text=f'{temperature} °C')
    humidity_per =round((data["main"]["humidity"]),2)
    humidity_r.config(text=f'{humidity_per} %')
    pressure_hpa =round((data["main"]["pressure"]),2)
    pressure_r.config(text=f'{pressure_hpa} hPa')
    wind_sp =round(((data["wind"]["speed"])*3.6),2)
    windspeed_r.config(text=f'{wind_sp} Km/hr')
    rainpercip = data.get("rain", {}).get("1h", 0)
    precipitation_mm = round(int(rainpercip),2)
    precipitation_per = precipitation_to_percentage(precipitation_mm)
    precipitation_r.config(text=f'{precipitation_per} %')

button = tk.Button(window,text="Search",font=25,command=search_w)
button.grid(column=2,row=0)
frame = tk.Frame(window,relief="raised")
frame.grid(column=0,row=3)
temp_l = tk.Label(frame,text="Temperature : ",padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2")
temp_l.grid(column=0,row=3,sticky="ew")
humidity = tk.Label(frame,text="Humidity : ",padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2")
humidity.grid(column=0,row=4,sticky="ew")
windspeed = tk.Label(frame,text="Wind Speed : ",padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2")
windspeed.grid(column=0,row=5,sticky="ew")
pressure = tk.Label(frame,text="Pressure : ",padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2")
pressure.grid(column=0,row=6,sticky="ew")
precipitation = tk.Label(frame,text="Rain propability : ",padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2")
precipitation.grid(column=0,row=7,sticky="ew")
frame_r = tk.Frame(window,relief="raised",width=20)
frame_r.grid(column=1,row=3,sticky="ew")
temp_r = tk.Label(frame_r,padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2",width=20)
temp_r.grid(column=1,row=3,sticky="ew")
humidity_r = tk.Label(frame_r,padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2",width=20)
humidity_r.grid(column=1,row=4,sticky="ew")
windspeed_r = tk.Label(frame_r,padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2",width=20)
windspeed_r.grid(column=1,row=5,sticky="ew")
pressure_r = tk.Label(frame_r,padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2",width=20)
pressure_r.grid(column=1,row=6,sticky="ew")
precipitation_r = tk.Label(frame_r,padx=10,pady=10,font=25,highlightbackground="black",highlightthickness="2",width=20)
precipitation_r.grid(column=1,row=7,sticky="ew")




window.mainloop()
