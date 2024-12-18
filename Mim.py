import customtkinter as ctk

root = ctk.CTk()
root.title("Mim")

root.geometry("440x620")

tabView = customtkinter.CTkTabView(app)
tabView.pack(padx=20, pady=20)

tabView.add("Grid Browser")
tabView.add("Channel Browser")
tabView.add("Favourites")
tabView.add("Preferences")
tabView.add("Search")
tabView.add("Remote")
tabView.add("About")

root.mainloop()
