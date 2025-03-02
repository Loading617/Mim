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
    print("Show Window on Top:", check_var_top.get())
    print("Start Mim with Remote:", check_var_remote.get())

def reset_preferences():
    entry_player_location.delete(0, ctk.END)
    entry_player_parameters.delete(0, ctk.END)
    entry_list_hierarchy.delete(0, ctk.END)
    check_var_top.set(0)
    check_var_remote.set(0)

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

check_var_top = ctk.IntVar()
checkbox_top = ctk.CTkCheckBox(preferences_tab, text="Show Window on Top", variable=check_var_top)
checkbox_top.grid(row=6, column=0, columnspan=3, padx=10, pady=5, sticky="w")

check_var_remote = ctk.IntVar()
checkbox_remote = ctk.CTkCheckBox(preferences_tab, text="Start Mim with Remote", variable=check_var_remote)
checkbox_remote.grid(row=7, column=0, columnspan=3, padx=10, pady=5, sticky="w")

preferences_tab.rowconfigure(8, weight=1)

reset_button = ctk.CTkButton(preferences_tab, text="Reset All Preferences", fg_color="red", hover_color="darkred", command=reset_preferences)
reset_button.grid(row=9, column=0, columnspan=3, padx=10, pady=15, sticky="ew")

class ChannelFavoritesRemote(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        
        self.channel_list = []
        
        self.channel_label = ctk.CTkLabel(self, text="Current Channel: None", font=("Arial", 16))
        self.channel_label.pack(pady=10)
        
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter Channel Name")
        self.entry.pack(pady=5)
        
        self.add_button = ctk.CTkButton(self, text="Add to Favorites", command=self.add_channel)
        self.add_button.pack(pady=5)
        
        self.listbox = ctk.CTkComboBox(self, values=self.channel_list, command=self.change_channel)
        self.listbox.pack(pady=5)
        
        self.remove_button = ctk.CTkButton(self, text="Remove Selected", command=self.remove_channel)
        self.remove_button.pack(pady=5)
    
    def add_channel(self):
        channel = self.entry.get()
        if channel and channel not in self.channel_list:
            self.channel_list.append(channel)
            self.listbox.configure(values=self.channel_list)
            self.entry.delete(0, 'end')
    
    def change_channel(self, selection):
        self.channel_label.configure(text=f"Current Channel: {selection}")
    
    def remove_channel(self):
        selected = self.listbox.get()
        if selected in self.channel_list:
            self.channel_list.remove(selected)
            self.listbox.configure(values=self.channel_list)
            if self.channel_list:
                self.channel_label.configure(text=f"Current Channel: {self.channel_list[0]}")
            else:
                self.channel_label.configure(text="Current Channel: None")

remote_tab = tabview.tab("Remote")
ChannelFavoritesRemote(remote_tab)

root.mainloop()
