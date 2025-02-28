import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("440x620")
root.title("Mim")
root.resizable(False, False)

tabview = ctk.CTkTabview(root, width=420, height=580)
tabview.pack(pady=10, padx=10, fill="both", expand=True)

tabs = ["Grid Browser", "Channel Browser", "Favourites", "Preferences", "Search", "Remote", "About"]
for tab_name in tabs:
    tabview.add(tab_name)
    label = ctk.CTkLabel(tabview.tab(tab_name), text=f"Content for {tab_name}", font=("Arial", 16))
    label.pack(pady=20)


tabview.set("Preferences")

tabview._segmented_button.configure(font=("Verdana", 8))

root.mainloop()
