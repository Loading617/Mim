import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.resizable(False, False)
        self.title("Mim")
        self.geometry("440x620")
        

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=10, pady=10, fill="both", expand=True)

        self.tab1 = self.tabview.add("Grid Browser")
        self.tab2 = self.tabview.add("Channel Browser")
        self.tab3 = self.tabview.add("Favourites")
        self.tab4 = self.tabview.add("Preferences")
        self.tab5 = self.tabview.add("Search")
        self.tab6 = self.tabview.add("Remote")
        self.tab7 = self.tabview.add("About")
        
        self.tabview.set("Preferences")
        
        for button in self.tabview._segmented_button._buttons_dict.values():
            button.configure(width=100, height=50)
        self.tab1_frame = self.tabview.tab("Grid Browser")
        self.tab2_frame = self.tabview.tab("Channel Browser")
        self.tab3_frame = self.tabview.tab("Favourites")
        self.tab4_frame = self.tabview.tab("Preferences")
        self.tab5_frame = self.tabview.tab("Search")
        self.tab6_frame = self.tabview.tab("Remote")
        self.tab7_frame = self.tabview.tab("About")
        
        self.tab1_frame.pack(padx=20, pady=20)
        self.tab2_frame.pack(padx=20, pady=20)
        self.tab3_frame.pack(padx=20, pady=20)
        self.tab4_frame.pack(padx=20, pady=20)
        self.tab5_frame.pack(padx=20, pady=20)
        self.tab6_frame.pack(padx=20, pady=20)
        self.tab7_frame.pack(padx=20, pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
