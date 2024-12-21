import customtkinter as ctk

class TabViewApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mim")
        self.geometry("440x620")

self.tab_view = ctk.CTkTabView(self)
self.tab_view.pack(fill="both", expand=True, padx=20, pady=20)

self.tab_view.add("Grid Browser")
self.tab_view.add("Channel Browser")
self.tab_view.add("Favourites")
self.tab_view.add("Preferences")
self.tab_view.add("Search")
self.tab_view.add("Remote")
self.tab_view.add("About")

self.tab_view.set("Preferences")

def disable_fullscreen():
    app.attributes("-fullscreen", False)

app.bind("<Escape>", lambda event: disable_fullscreen())

if __name__ == "__main__":
    app = TabViewApp()
    app.mainloop()
