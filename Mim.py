import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.resizable(False, False)
app.title("Mim")
app.iconbitmap("Mim.ico")
app.geometry("440x620")

tabview = ctk.CTkTabview(app)
tabview.pack(pady=20, padx=20, fill="both", expand=True)

tab1 = tabview.add("     Grid Browser     ")
tab2 = tabview.add("     Channel Browser     ")
tab3 = tabview.add("     Favourites      ")
tab4 = tabview.add("     Preferences     ")
tab5 = tabview.add("     Search   ")

app.mainloop()
