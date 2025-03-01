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

tabview.set("Preferences")

tabview._segmented_button.configure(font=("Verdana", 8))

for row in range(3):
    for col in range(3):
        label = ctk.CTkLabel(tab1)
        label.grid(row=row, column=col, padx=10, pady=10)

for row in range(2):
    for col in range(2):
        label = ctk.CTkLabel(tab2)
        label.grid(row=row, column=col, padx=10, pady=10)

for row in range(4):
    for col in range(2):
        label = ctk.CTkLabel(tab3)
        label.grid(row=row, column=col, padx=10, pady=10)

root.mainloop()
