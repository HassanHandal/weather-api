import tkinter as tk
import requests
from api import api_key2

def precipitation_to_percentage(precipitation_mm):
    thresholds = [1.0, 5.0, 10.0]
    if precipitation_mm == 0:
        return 0
    for i, threshold in enumerate(thresholds, start=1):
        if precipitation_mm <= threshold:
            return i * 30
    return 100

def search_weather():
    api_key = api_key2()
    city = search_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    temperature = round((data["main"]["temp"] - 273.15), 2)
    temp_label.config(text=f'{temperature} °C')

    humidity_percent = round(data["main"]["humidity"], 2)
    humidity_label.config(text=f'{humidity_percent} %')

    pressure_hpa = round(data["main"]["pressure"], 2)
    pressure_label.config(text=f'{pressure_hpa} hPa')

    wind_speed_kph = round((data["wind"]["speed"] * 3.6), 2)
    windspeed_label.config(text=f'{wind_speed_kph} Km/hr')

    rain_precipitation = data.get("rain", {}).get("1h", 0)
    precipitation_mm = round(int(rain_precipitation), 2)
    precipitation_percent = precipitation_to_percentage(precipitation_mm)
    precipitation_label.config(text=f'{precipitation_percent} %')

window = tk.Tk()
window.title("Weather Status Map")
window.minsize(width=300, height=300)

location_label = tk.Label(window, text="Location : ", padx=10, pady=10, font=15)
location_label.grid(column=0, row=0)

search_entry = tk.Entry(window, width=20)
search_entry.grid(column=1, row=0, padx=10, pady=10)

search_button = tk.Button(window, text="Search", font=25, command=search_weather)
search_button.grid(column=2, row=0)

labels_frame = tk.Frame(window, relief="raised")
labels_frame.grid(column=0, row=3)

labels_info = ["Temperature", "Humidity", "Wind Speed", "Pressure", "Rain Probability"]
for i, label_text in enumerate(labels_info, start=3):
    label = tk.Label(labels_frame, text=f"{label_text} : ", padx=10, pady=10, font=25, highlightbackground="black",
                     highlightthickness="2")
    label.grid(column=0, row=i, sticky="ew")

results_frame = tk.Frame(window, relief="raised", width=20)
results_frame.grid(column=1, row=3, sticky="ew")

result_labels = [
    tk.Label(results_frame, padx=10, pady=10, font=25, highlightbackground="black", highlightthickness="2", width=20)
    for _ in labels_info
]
for i, result_label in enumerate(result_labels, start=3):
    result_label.grid(column=1, row=i, sticky="ew")

temp_label, humidity_label, windspeed_label, pressure_label, precipitation_label = result_labels

window.mainloop()
