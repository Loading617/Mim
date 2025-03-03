import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("440x620")import customtkinter as ctk
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
    for switch in switch_list:
        print(f"{switch.cget('text')}: {'ON' if switch.get() else 'OFF'}")

def reset_preferences():
    entry_player_location.delete(0, ctk.END)
    entry_player_parameters.delete(0, ctk.END)
    entry_list_hierarchy.delete(0, ctk.END)
    entry_list_url.delete(0, ctk.END)
    check_var_top.set(0)
    check_var_remote.set(0)
    for switch in switch_list:
        switch.destroy()
    switch_list.clear()

def add_url():
    url = entry_list_url.get().strip()
    if url:
        new_switch = ctk.CTkSwitch(switch_frame, text=url)
        new_switch.pack(pady=2, padx=5, anchor="w")
        switch_list.append(new_switch)
        entry_list_url.delete(0, ctk.END)

def on_paste(event):
    root.after(100, add_url)

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

label_list_url = ctk.CTkLabel(preferences_tab, text="List URL:")
label_list_url.grid(row=6, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")
entry_list_url = ctk.CTkEntry(preferences_tab)
entry_list_url.grid(row=7, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
add_button = ctk.CTkButton(preferences_tab, text="Add", command=add_url)
add_button.grid(row=7, column=2, padx=10, pady=5, sticky="ew")

entry_list_url.bind("<Control-v>", on_paste)
entry_list_url.bind("<Button-2>", on_paste)

label_switches = ctk.CTkLabel(preferences_tab, text="Toggle URL List:")
label_switches.grid(row=8, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")

switch_frame = ctk.CTkFrame(preferences_tab, fg_color="transparent")
switch_frame.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

switch_list = []

check_var_top = ctk.IntVar()
checkbox_top = ctk.CTkCheckBox(preferences_tab, text="Show Window on Top", variable=check_var_top)
checkbox_top.grid(row=10, column=0, columnspan=3, padx=10, pady=5, sticky="w")

check_var_remote = ctk.IntVar()
checkbox_remote = ctk.CTkCheckBox(preferences_tab, text="Start Mim with Remote", variable=check_var_remote)
checkbox_remote.grid(row=11, column=0, columnspan=3, padx=10, pady=5, sticky="w")

preferences_tab.rowconfigure(12, weight=1)

reset_button = ctk.CTkButton(preferences_tab, text="Reset All Preferences", fg_color="red", hover_color="darkred", command=reset_preferences)
reset_button.grid(row=13, column=0, columnspan=3, padx=10, pady=15, sticky="ew")

root.mainloop()

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
    for switch in switch_list:
        print(f"{switch.cget('text')}: {'ON' if switch.get() else 'OFF'}")

def reset_preferences():
    entry_player_location.delete(0, ctk.END)
    entry_player_parameters.delete(0, ctk.END)
    entry_list_hierarchy.delete(0, ctk.END)
    entry_list_url.delete(0, ctk.END)
    check_var_top.set(0)
    check_var_remote.set(0)
    for switch in switch_list:
        switch.destroy()
    switch_list.clear()

def add_url():
    url = entry_list_url.get()
    if url:
        new_switch = ctk.CTkSwitch(switch_frame, text=url)
        new_switch.pack(pady=2, padx=5, anchor="w")
        switch_list.append(new_switch)
        entry_list_url.delete(0, ctk.END)

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

label_list_url = ctk.CTkLabel(preferences_tab, text="List URL:")
label_list_url.grid(row=6, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")
entry_list_url = ctk.CTkEntry(preferences_tab)
entry_list_url.grid(row=7, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
add_button = ctk.CTkButton(preferences_tab, text="Add", command=add_url)
add_button.grid(row=7, column=2, padx=10, pady=5, sticky="ew")

label_switches = ctk.CTkLabel(preferences_tab, text="Toggle URL List:")
label_switches.grid(row=8, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="w")

switch_frame = ctk.CTkFrame(preferences_tab, fg_color="transparent")
switch_frame.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

switch_list = []

check_var_top = ctk.IntVar()
checkbox_top = ctk.CTkCheckBox(preferences_tab, text="Show Window on Top", variable=check_var_top)
checkbox_top.grid(row=10, column=0, columnspan=3, padx=10, pady=5, sticky="w")

check_var_remote = ctk.IntVar()
checkbox_remote = ctk.CTkCheckBox(preferences_tab, text="Start Mim with Remote", variable=check_var_remote)
checkbox_remote.grid(row=11, column=0, columnspan=3, padx=10, pady=5, sticky="w")

preferences_tab.rowconfigure(12, weight=1)

reset_button = ctk.CTkButton(preferences_tab, text="Reset All Preferences", fg_color="red", hover_color="darkred", command=reset_preferences)
reset_button.grid(row=13, column=0, columnspan=3, padx=10, pady=15, sticky="ew")

root.mainloop()
