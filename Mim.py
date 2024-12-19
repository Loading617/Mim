import customtkinter as ctk

root = ctk.CTk()
root.title("Mim")

app.resizable(False, False)

app.attributes('-fullscreen', False)

root.geometry("440x620")

tabView = ctk.CTkTabview(app)
tabView.pack(padx=20, pady=20)

tab1.add("Grid Browser")
tab2.add("Channel Browser")
tab3.add("Favourites")
tab4.add("Preferences")
tab5.add("Search")
tab6.add("Remote")
tab7.add("About")

root.mainloop()
