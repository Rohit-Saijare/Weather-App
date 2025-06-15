from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk

# Function to fetch weather data
def data_get():
    city = city_name.get()
    try:
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b1e67e3c984f0144d7e92279b32bd5d6"
        ).json()

        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"].title())
        temp_label1.config(text=f"{int(data['main']['temp'] - 273.15)} °C")
        per_label1.config(text=f"{data['main']['pressure']} hPa")
        hum_label1.config(text=f"{data['main']['humidity']} %")
        wd_label1.config(text=f"{data['wind']['speed']} m/s")
        v_label1.config(text=f"{data['visibility']} m")
    except Exception as e:
        w_label1.config(text="Error")
        wb_label1.config(text="City not found")
        temp_label1.config(text="")
        per_label1.config(text="")
        hum_label1.config(text="")
        wd_label1.config(text="")
        v_label1.config(text="")

# Main window setup
win = Tk()
win.title("Weather App")
win.geometry("500x700")
win.resizable(False, False)

# Create a canvas for background and weather info
canvas = Canvas(win, width=11111100, height=100)
canvas.pack(fill=BOTH, expand=True)

# Load and display the background image

bg_image = Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\PYTHON\improved weather app 2.0\be338477aca78d7b54c16419df7f9075.png")
  # Replace with your background image path
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0,0, anchor=NW, image=bg_photo)

# Header Frame (for app title)
header_frame = Frame(win, bg="#4682B4")
header_frame.place(x=0, y=0, relwidth=1, height=70)
header_label = Label(header_frame, text="Weather App", font=("Arial", 24, "bold"), fg="white", bg="#4682B4")
header_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# City Dropdown Menu
city_name = StringVar()
states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

combo_frame = Frame(win, bg="#A9D1F5")
combo_frame.place(x=25, y=80, width=450, height=60)

city_combo = ttk.Combobox(combo_frame, values=states, textvariable=city_name, font=("Arial", 14), width=40)
city_combo.set("Select your state")
city_combo.pack(pady=10)

# Button (styled with hover effect)
def on_enter(e):
    get_button.config(bg="#357ABD", fg="white")

def on_leave(e):
    get_button.config(bg="#4682B4", fg="white")

get_button = Button(win, text="Get Weather", font=("Arial", 16, "bold"), bg="#4682B4", fg="white", command=data_get, bd=0, padx=10, pady=10, relief=SOLID)
get_button.place(x=180, y=150, width=140, height=50)
get_button.bind("<Enter>", on_enter)
get_button.bind("<Leave>", on_leave)

# Weather Info Card (grouping labels)
info_frame = Frame(win, bg="#FFFFFF", padx=20, pady=20, bd=2, relief=SOLID)
info_frame.place(x=25, y=220, width=450, height=450)

# Add rows in the info card
def create_row(parent, row, text, label):
    Label(parent, text=text, font=("Arial", 14), bg="#FFFFFF", anchor="w").grid(row=row, column=0, sticky="w", pady=8)
    label.config(font=("Arial", 14, "bold"), bg="#FFFFFF", anchor="e")
    label.grid(row=row, column=1, sticky="e", pady=8)

# Value labels for weather data
w_label1 = Label(info_frame)
wb_label1 = Label(info_frame)
temp_label1 = Label(info_frame)
per_label1 = Label(info_frame)
hum_label1 = Label(info_frame)
wd_label1 = Label(info_frame)
v_label1 = Label(info_frame)

create_row(info_frame, 0, "Condition:", w_label1)
create_row(info_frame, 1, "Description:", wb_label1)
create_row(info_frame, 2, "Temperature:", temp_label1)
create_row(info_frame, 3, "Pressure:", per_label1)
create_row(info_frame, 4, "Humidity:", hum_label1)
create_row(info_frame, 5, "Wind Speed:", wd_label1)
create_row(info_frame, 6, "Visibility:", v_label1)

# Footer
footer = Label(win, text="Made by Rohit Saijare", bg="#A9D1F5", font=("Arial", 10), fg="gray")
footer.place(x=0, y=670, relwidth=1, height=30)

# Run the main window
win.mainloop()
