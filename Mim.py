import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Mim")
app.geometry("440x620")
app.resizable(False, False)

tabview = ctk.CTkTabview(app, width=420, height=580)
tabview.pack(pady=10, padx=10, fill="both", expand=True)

tabs = ["Grid Browser", "Channel Browser", "Favourites", "Preferences", "Search", "Remote", "About"]
for tab_name in tabs:
    tabview.add(tab_name)

tabview.set("Preferences")
tabview._segmented_button.configure(font=("Verdana", 8))

preferences_tab = tabview.tab("Preferences")
remote_tab = tabview.tab("Remote")
search_tab = tabview.tab("Search")
grid_browser_tab = tabview.tab("Grid Browser")

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
    print("File Hierarchy:", entry_list_hierarchy.get())
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
entry_player_location = ctk.CTkEntry(preferences_tab, width=300)
entry_player_location.grid(row=1, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
browse_button1 = ctk.CTkButton(preferences_tab, text="Browse", command=browse_application)
browse_button1.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

label_player_parameters = ctk.CTkLabel(preferences_tab, text="Player Parameters:")
label_player_parameters.grid(row=2, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")
entry_player_parameters = ctk.CTkEntry(preferences_tab, width=300)
entry_player_parameters.grid(row=3, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
save_button = ctk.CTkButton(preferences_tab, text="Save", command=save_preferences)
save_button.grid(row=3, column=2, padx=10, pady=5, sticky="ew")

label_list_hierarchy = ctk.CTkLabel(preferences_tab, text="File Hierarchy:")
label_list_hierarchy.grid(row=4, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")
entry_list_hierarchy = ctk.CTkEntry(preferences_tab, width=300)
entry_list_hierarchy.grid(row=5, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
browse_button2 = ctk.CTkButton(preferences_tab, text="Browse", command=browse_folder)
browse_button2.grid(row=5, column=2, padx=10, pady=5, sticky="ew")

label_list_url = ctk.CTkLabel(preferences_tab, text="List URL:")
label_list_url.grid(row=6, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")
entry_list_url = ctk.CTkEntry(preferences_tab, width=300)
entry_list_url.grid(row=7, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
add_button = ctk.CTkButton(preferences_tab, text="Add", command=add_url)
add_button.grid(row=7, column=2, padx=10, pady=5, sticky="ew")

scrollable_frame = ctk.CTkScrollableFrame(preferences_tab, width=400, height=200)
scrollable_frame.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

check_var_top = ctk.IntVar()
checkbox_top = ctk.CTkCheckBox(preferences_tab, text="Show Window on Top", variable=check_var_top)
checkbox_top.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky="w")

check_var_remote = ctk.IntVar()
checkbox_remote = ctk.CTkCheckBox(preferences_tab, text="Start Mim with Remote", variable=check_var_remote)
checkbox_remote.grid(row=10, column=0, columnspan=3, padx=10, pady=5, sticky="w")

reset_button = ctk.CTkButton(preferences_tab, text="Reset All Preferences", fg_color="red", hover_color="darkred", command=reset_preferences)
reset_button.grid(row=11, column=0, columnspan=3, padx=10, pady=15, sticky="ew")

preferences_tab.rowconfigure(8, weight=1)

remote_tab.columnconfigure(0, weight=1)
open_remote_button = ctk.CTkButton(remote_tab, text="Open Remote", command=open_remote)
open_remote_button.pack(pady=20)

search_tab.columnconfigure(0, weight=1)

grid_frame = ctk.CTkFrame(search_tab)
grid_frame.pack(expand=True, fill="both", padx=10, pady=10)

search_frame = ctk.CTkFrame(search_tab)
search_frame.pack(side="bottom", fill="x", padx=10, pady=5)

search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search")
search_entry.pack(side="left", expand=True, fill="x", padx=5)

def search_action():
    query = search_entry.get()
    print(f"Searching for: {query}")

search_button = ctk.CTkButton(search_frame, text="Search", command=search_action)
search_button.pack(side="left", padx=5)

for row in range(6):
    for col in range(6):
        label = ctk.CTkLabel(grid_frame, text=f"", padx=10, pady=5)
        label.grid(row=row, column=col, padx=5, pady=5)

grid_browser_tab = tabview.tab("Grid Browser")

grid_browser_frame = ctk.CTkFrame(grid_browser_tab)
grid_browser_frame.pack(pady=10, padx=10, fill="both", expand=True)

bottom_frame = ctk.CTkFrame(grid_browser_tab)
bottom_frame.pack(pady=10, padx=10, fill="x", side="bottom")

query_label = ctk.CTkLabel(bottom_frame, text="Query")
query_label.pack(side="left", padx=5)

query_entry = ctk.CTkEntry(bottom_frame)
query_entry.pack(side="left", padx=5, fill="x", expand=True)

app.mainloop()
