from tkinter import *

def calculate():
    print("Calculated miles to kilometers")
    float_miles = float(miles_input.get())
    result = round(float_miles * 1.609344, 2)
    total_label.config(text=result)

#Window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

#Label
miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)

equals_to_label = Label(text="is equal to", font=("Arial", 16))
equals_to_label.grid(column= 0, row=1)

total_label = Label(text="0", font=("Aerial", 16))
total_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Aerial", 16))
km_label.grid(column=2, row=1)

#Buttons
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()