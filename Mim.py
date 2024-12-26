import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.resizable(False, False)
        self.title("Mim")
        self.geometry("440x620")
        

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=10, pady=10)

        self.tab1 = self.tabview.add("Grid Browser")
        self.tab2 = self.tabview.add("Channel Browser")
        self.tab3 = self.tabview.add("Favourites")
        self.tab4 = self.tabview.add("Preferences")
        self.tab5 = self.tabview.add("Search")
        self.tab6 = self.tabview.add("Remote")
        self.tab7 = self.tabview.add("About")
        
    
    def Browse(self):
        print("Browse")
    
    def Open(self):
        print("Open")
    
    def Save(self):
        print("Save")
        
    def Browse_Folder(self):
        print("Browse Folder")
        
    def Reset_Preferences(self):
        print("Reset Preferences")
        
        ctk.CTkButton(self.tab4, text="Browse", action="Open")
        ctk.CTkButton(self.tab4, text="Save", action="Save").pack()
        ctk.CTkButton(self.tab4, text="Browse", action="Browse for Folder").pack()
        ctk.CTkButton(self.tab4, text="Reset Preferences").pack()

        
        self.tabview.set("Preferences")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
