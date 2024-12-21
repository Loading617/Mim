import customtkinter


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        
        self.add("Grid Browser")
        self.add("Channel Browser")
        self.add("Favourites")
        self.add("Preferences")
        self.add("Search")
        self.add("Remote")
        self.add("About")

        
class App(customtkinter.Mim):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()
