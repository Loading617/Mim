import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Mim")
        self.geometry("730x620")

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=20, pady=20)

        self.tab1 = self.tabview.add("Grid Browser")
        self.tab2 = self.tabview.add("Channel Browser")
        self.tab3 = self.tabview.add("Favourites")
        self.tab4 = self.tabview.add("Preferences")
        self.tab5 = self.tabview.add("Search")
        self.tab6 = self.tabview.add("Remote")
        self.tab7 = self.tabview.add("About")
        
        ctk.CTkButton(self.tab4, text="Reset Preferences").pack()

        
        self.tabview.set("Preferences")  

if __name__ == "__main__":
    app = App()
    app.mainloop()
