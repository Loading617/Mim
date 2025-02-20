import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.resizable(False, False)
        self.title("Mim")
        self.geometry("440x620")
        

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.tab1 = self.tabview.add("Grid Browser")
        self.tab2 = self.tabview.add("Channel Browser")
        self.tab3 = self.tabview.add("Favourites")
        self.tab4 = self.tabview.add("Preferences")
        self.tab5 = self.tabview.add("Search")
        self.tab6 = self.tabview.add("Remote")
        self.tab7 = self.tabview.add("About")
        
        self.tabview.set("Preferences")
        
        for tab in self.tabview.tabs.values():
            tab.grid_rowconfigure(0, weight=1)
            tab.grid_columnconfigure(0, weight=1)
        
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
