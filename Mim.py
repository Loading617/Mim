import customtkinter as ctk

app = ctk.CTk()

app.title("Mim")
app.geometry("440x620")

tabview = ctk.CTkTabView(app)

tabview.addTab("Grid Browser")
tabview.addTab("Channel Browser")
tabview.addTab("Favourites")
tabview.addTab("Settings")
tabview.addTab("Search")
tabview.addTab("Remote")
tabview.addTab("About")

def disable_fullscreen():
    app.attributes("-fullscreen", False)

tabview.set("Preferences")

app.bind("<Escape>", lambda event: disable_fullscreen())

app.mainloop()
