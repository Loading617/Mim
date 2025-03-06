import customtkinter as ctk 
from tkinter import filedialog

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

preferences_tab = tabview.tab("Preferences")
remote_tab = tabview.tab("Remote")
search_tab = tabview.tab("Search")

search_tab.columnconfigure(0, weight=1)
search_tab.rowconfigure(0, weight=1)

search_frame = ctk.CTkFrame(search_tab)
search_frame.pack(fill="both", expand=True, padx=10, pady=10)

grid_view = ctk.CTkFrame(search_frame)
grid_view.pack(fill="both", expand=True, pady=(0, 10))

search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search")
search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

search_button = ctk.CTkButton(search_frame, text="Search")
search_button.pack(side="right")

def browse_application():
    file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe"), ("All Files", "*.*")])
    if file_path:
        entry_player_location.delete(0, ctk.END)
        entry_player_location.insert(0, file_path)

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_list_hierarchy.delete(0, ctk.END)
        entry_list_hierarchy.insert(0, folder_path)

def save_preferences():
    print("Preferences Saved!")
    print("Player Location:", entry_player_location.get())
    print("Player Parameters:", entry_player_parameters.get())
    print("List Hierarchy:", entry_list_hierarchy.get())
    print("List URL:", entry_list_url.get())
    print("Show Window on Top:", check_var_top.get())
    print("Start Mim with Remote:", check_var_remote.get())

def reset_preferences():
    entry_player_location.delete(0, ctk.END)
    entry_player_parameters.delete(0, ctk.END)
    entry_list_hierarchy.delete(0, ctk.END)
    entry_list_url.delete(0, ctk.END)
    check_var_top.set(0)
    check_var_remote.set(0)
    
    
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

def add_url():
    url = entry_list_url.get().strip()
    if url:
        new_checkbox = ctk.CTkCheckBox(scrollable_frame, text=url)
        new_checkbox.pack(anchor="w", padx=5, pady=2)
        entry_list_url.delete(0, ctk.END)

def open_remote():
    print("Remote Opened!")

preferences_tab.columnconfigure(0, weight=1)
preferences_tab.columnconfigure(1, weight=1)
preferences_tab.columnconfigure(2, weight=1)

label_player_location = ctk.CTkLabel(preferences_tab, text="Player Location:")
label_player_location.grid(row=0, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")
entry_player_location = ctk.CTkEntry(preferences_tab)
entry_player_location.grid(row=1, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
browse_button1 = ctk.CTkButton(preferences_tab, text="Browse", command=browse_application)
browse_button1.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

label_player_parameters = ctk.CTkLabel(preferences_tab, text="Player Parameters:")
label_player_parameters.grid(row=2, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")
entry_player_parameters = ctk.CTkEntry(preferences_tab)
entry_player_parameters.grid(row=3, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
save_button = ctk.CTkButton(preferences_tab, text="Save", command=save_preferences)
save_button.grid(row=3, column=2, padx=10, pady=5, sticky="ew")

label_list_hierarchy = ctk.CTkLabel(preferences_tab, text="List Hierarchy:")
label_list_hierarchy.grid(row=4, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")
entry_list_hierarchy = ctk.CTkEntry(preferences_tab)
entry_list_hierarchy.grid(row=5, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
browse_button2 = ctk.CTkButton(preferences_tab, text="Browse", command=browse_folder)
browse_button2.grid(row=5, column=2, padx=10, pady=5, sticky="ew")

preferences_tab.rowconfigure(8, weight=1)

remote_tab.columnconfigure(0, weight=1)
open_remote_button = ctk.CTkButton(remote_tab, text="Open Remote", command=open_remote)
open_remote_button.pack(pady=20)

root.mainloop()
