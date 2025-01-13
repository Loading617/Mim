import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.resizable(False, False)
        self.title("Mim")
        self.geometry("440x620")
        

        self.tabview = ctk.CTkTabview(master=self, width=400)
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.tab1 = self.tabview.add("Grid Browser")
        self.tab2 = self.tabview.add("Channel Browser")
        self.tab3 = self.tabview.add("Favourites")
        self.tab4 = self.tabview.add("Preferences")
        self.tab5 = self.tabview.add("Search")
        self.tab6 = self.tabview.add("Remote")
        self.tab7 = self.tabview.add("About")
        
        self.tabview.set("Preferences")
        
        self.tabview.tab("Grid Browser").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Grid Browser").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Channel Browser").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Channel Browser").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Favourites").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Favourites").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Preferences").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Preferences").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Search").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Search").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Remote").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Remote").grid_rowconfigure(0, weight=1)
        self.tabview.tab("About").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About").grid_rowconfigure(0, weight=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()
