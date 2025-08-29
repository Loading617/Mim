import customtkinter as ctk

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Mim Favorites Remote")
app.geometry("350x400")

favorites = {}

def assign_channel(num):
    favorites[num] = f"Channel {num}"
    print(f"Assigned {favorites[num]} to button {num}")

frame = ctk.CTkFrame(app)
frame.pack(expand=True)

number = 1
for r in range(3):   
    for c in range(3):  
        btn = ctk.CTkButton(
            frame,
            text=str(number),
            width=90,
            height=70,
            command=lambda n=number: assign_channel(n)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)
        number += 1
        if number > 9:
            break

btn10 = ctk.CTkButton(
    frame,
    text="10",
    width=90,
    height=70,
    command=lambda: assign_channel(10)
)
btn10.grid(row=3, column=1, pady=5)

app.mainloop()
