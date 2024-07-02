import requests
from tkinter import *
import calendar

# api_key = "7d750ebd913cf7cb56de1fcb44f4822b"
api_key = "6ed0da5e1b9c52f082fb69c8ac03b4ca"
API_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
BACKGROUND_BLUE = "#97DEFF"
FRONT_BLUE = "#C9EEFF"
OTHER_BLUE = "#62CDFF"

weather_params = {
    "lat": 31.3256,
    "lon": 75.5792,
    "appid": api_key,
    # "lat": 26.449923,
    # "lon": 80.331871,
    # "exclude": "current,minutely,daily",
}

response = requests.get(API_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data["list"][:6]

will_rain = False

weather_code = []
weather_status = []
weather_description = []
date_and_time = []

for hour_3_data in weather_slice:
    weather_code.append(int(hour_3_data["weather"][0]["id"]))
    weather_status.append(hour_3_data["weather"][0]["main"])
    weather_description.append(hour_3_data["weather"][0]["description"])
    date_and_time.append(hour_3_data["dt_txt"])

time = []
date = []
hour = []
for n in date_and_time:
    m = n.split(" ")
    date.append(m[0])
    time.append(m[1])

for n in time:
    m = n[1].split(":")
    hour.append(m[0])

day = []
month = []
p = []
for n in date:
    m = n.split("-")
    if int(m[1]) < 10:
        p = m[1].split("0")
    day.append(m[2])
    month.append(p[1])

name_of_month = []
for n in month:
    m = calendar.month_name[int(n)]
    name_of_month.append(m)

is_night = None
for n in hour:
    if 0 <= int(n) <= 6 and 18 <= int(n) <= 23:
        is_night = True
        break
    else:
        is_night = False


window = Tk()
window.title("Weather Report")
window.config(padx=50, pady=50, bg=BACKGROUND_BLUE)

title_text = Label(text="Weather Forcast", fg="white", bg=BACKGROUND_BLUE, font=("Arial", 30, "bold"))
title_text.config(pady=10)
title_text.grid(row=0, column=0)

canvas = Canvas(height=500, width=1200, bg=FRONT_BLUE, highlightthickness=0)
clear_sky_d_image = PhotoImage(file="images/01d@2x.png")
clear_sky_n_image = PhotoImage(file="images/01n@2x.png")
few_clouds_d_image = PhotoImage(file="images/02d@2x.png")
few_clouds_n_image = PhotoImage(file="images/02n@2x.png")
scattered_clouds_image = PhotoImage(file="images/03d@2x.png")
broken_clouds_image = PhotoImage(file="images/04d@2x.png")
shower_rain_image = PhotoImage(file="images/09d@2x.png")
rain_d_image = PhotoImage(file="images/10d@2x.png")
rain_n_image = PhotoImage(file="images/10n@2x.png")
thunderstorm_image = PhotoImage(file="images/11d@2x.png")
snow_image = PhotoImage(file="images/13d@2x.png")
mist_image = PhotoImage(file="images/50d@2x.png")

image = []

for code in weather_code:
    if is_night:
        if 200 <= code <= 232:
            image.append(thunderstorm_image)
        elif 300 <= code <= 321:
            image.append(shower_rain_image)
        elif 500 <= code <= 504:
            image.append(rain_n_image)
        elif code == 511:
            image.append(snow_image)
        elif 520 <= code <= 531:
            image.append(shower_rain_image)
        elif 600 <= code <= 622:
            image.append(snow_image)
        elif 701 <= code <= 781:
            image.append(mist_image)
        elif code == 800:
            image.append(clear_sky_n_image)
        elif code == 801:
            image.append(few_clouds_n_image)
        elif code == 802:
            image.append(scattered_clouds_image)
        elif code == 803:
            image.append(broken_clouds_image)
        elif code == 804:
            image.append(broken_clouds_image)
    else:
        if 200 <= code <= 232:
            image.append(thunderstorm_image)
        elif 300 <= code <= 321:
            image.append(shower_rain_image)
        elif 500 <= code <= 504:
            image.append(rain_d_image)
        elif code == 511:
            image.append(snow_image)
        elif 520 <= code <= 531:
            image.append(shower_rain_image)
        elif 600 <= code <= 622:
            image.append(snow_image)
        elif 701 <= code <= 781:
            image.append(mist_image)
        elif code == 800:
            image.append(clear_sky_d_image)
        elif code == 801:
            image.append(few_clouds_d_image)
        elif code == 802:
            image.append(scattered_clouds_image)
        elif code == 803:
            image.append(broken_clouds_image)
        elif code == 804:
            image.append(broken_clouds_image)

x_position_text = [100, 300, 500, 700, 900, 1100]
x_position_line = [200, 400, 600, 800, 1000]

for n in day:
    for m in name_of_month:
        for x in x_position_text:
            text = canvas.create_text(x, 100, text=f"{m}, {n}", fill="blue", font=("Arial", 15, "normal"))

for x in x_position_line:
    canvas.create_line(x, 50, x, 450, fill=BACKGROUND_BLUE)

weather_image_list = []
for x in x_position_text:
    weather_image = canvas.create_image(x, 200)
    weather_image_list.append(weather_image)

counter = 0
for image_val in image:
    canvas.itemconfig(weather_image_list[counter], image=image_val)
    counter += 1

canvas.grid(row=1, column=0)
window.mainloop()
