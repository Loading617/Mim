import customtkinter as ctk

root = ctk.CTk()
root.title("Mim")

def disable_fullscreen():
    app.attributes("-fullscreen", False)

root.geometry("440x620")

tabView = ctk.CTkTabview(app, width=500, height=400)
tabView.pack(pady=20, padx=20, fill="both", expand=True)

tab.add("Grid Browser")
tab.add("Channel Browser")
tab.add("Favourites")
tab.add("Preferences")
tab.add("Search")
tab.add("Remote")
tab.add("About")

tabview.set("Preferences")

app.bind("<Escape>", lambda event: disable_fullscreen())

root.mainloop()
