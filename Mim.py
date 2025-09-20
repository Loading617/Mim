import customtkinter as ctk
import requests
import os
import re
import sys
import subprocess
import webbrowser
from tkinter import filedialog
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def open_link():
    webbrowser.open("https://www.mim.com")

app = ctk.CTk()
app.title("Mim")
app.geometry("440x620")
app.resizable(False, False)

tabview = ctk.CTkTabview(app, width=420, height=580)
tabview.pack(pady=10, padx=10, fill="both", expand=True)

tabs = ["Grid Browser", "Channel Browser", "Favourites", "Preferences", "Search", "About"]
for tab_name in tabs:
    tabview.add(tab_name)

tabview.set("Preferences")
tabview._segmented_button.configure(font=("Verdana", 8))

grid_browser_tab = tabview.tab("Grid Browser")
channel_browser_tab = tabview.tab("Channel Browser")
favourites_tab = tabview.tab("Favourites")
preferences_tab = tabview.tab("Preferences")
search_tab = tabview.tab("Search")
about_tab = tabview.tab("About")

def browse_application():
    file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe"), ("All Files", "*.*")])
    if file_path:
        entry_player_location.delete(0, ctk.END)
        entry_player_location.insert(0, file_path)

def browse_folder():
    file_path = filedialog.askopenfilename(
        filetypes=[("M3U Playlist", "*.m3u"), ("M3U8 Playlist", "*.m3u8"), ("XSPF Playlist", "*.xspf")]
    )
    if file_path:
        entry_list_url.delete(0, ctk.END)
        entry_list_url.insert(0, file_path)
        load_m3u_channels(file_path)
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_list_hierarchy.delete(0, ctk.END)
        entry_list_hierarchy.insert(0, folder_path)

def load_m3u_channels(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        channels = parse_m3u(content)
        update_grid_browser(channels)
        
    except Exception as e:
        print("Error loading M3U file:", e)
        
def update_grid_browser(channels):
    global all_channels
    all_channels = channels
    
    for widget in grid_browser_frame.winfo_children():
        widget.destroy()
    
    row, col = 0, 0
    for name, url in channels:
        btn = ctk.Button(
            grid_browser_frame, 
            text=name, 
            command=lambda u=url: launch_channel(u),
            width=120,
            height=40
            )
        btn.grid(row=row, column=col, padx=5, pady=5)

        btn.bind("<Button-1>", lambda e, url=url: launch_channel(u))
        btn.bind("<Button-3>", lambda e, name=n, url=url: channel_menu(e, n, u))
        
        col += 1
        if col >= 3:
            col = 0
            row += 1

def save_preferences():
    print("Preferences Saved!")
    print("Player Location:", entry_player_location.get())
    print("Player Parameters:", entry_player_parameters.get())
    print("File Hierarchy:", entry_list_hierarchy.get())
    print("List URL:", entry_list_url.get())
    print("Show Window on Top:", check_var_top.get())

def reset_preferences():
    entry_player_location.delete(0, ctk.END)
    entry_player_parameters.delete(0, ctk.END)
    entry_list_hierarchy.delete(0, ctk.END)
    entry_list_url.delete(0, ctk.END)
    check_var_top.set(0)
    
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

def confirm_reset_preferences():
    """Show a confirmation dialog before resetting preferences."""
    if (entry_player_location.get() or entry_player_parameters.get() or 
        entry_list_hierarchy.get() or entry_list_url.get()):
        warning = messagebox.askquestion("Confirm Reset", "⚠️ Are you sure?", icon="warning")
        if warning == "yes":
            reset_preferences()
    else:
        reset_preferences()

def add_url():
    url = entry_list_url.get().strip()
    if url:
        new_checkbox = ctk.CTkCheckBox(scrollable_frame, text=url)
        new_checkbox.pack(anchor="w", padx=5, pady=2)
        entry_list_url.delete(0, ctk.END)

def fetch_m3u(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch M3U file: {e}")
        return None

def parse_m3u(content):
    """Extracts channel names and URLs from M3U content."""
    channels = []
    lines = content.splitlines()
    current_name = None

    for line in lines:
        line = line.strip()
        if line.startswith("#EXTINF"):
            match = re.search(r'?,(.*)', line)
            if match:
                current_name = match.group(1)
        elif line and not line.startswith("#"):
            if current_name:
                channels.append((current_name, line))
                current_name = None
    
    return channels

def launch_channel(url):
    """Launch selected channel in external player."""
    player = entry_player_location.get().strip()
    params = entry_player_parameters.get().strip()

    if not player:
        messagebox.showerror("Player Not Set", "Please set your player location in Preferences.")
        return

    try:
        cmd = [player]
        if params:
            cmd.extend(params.split())
        cmd.append(url)
        subprocess.Popen(cmd)
        print(f"Launching: {' '.join(cmd)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch player:\n{e}")

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

mim_folder = os.path.join(downloads_path, "MimData")

if not os.path.exists(mim_folder):
    os.makedirs(mim_folder)

favourites_file = os.path.join(mim_folder, "favourites.mim")

if not os.path.exists(favourites_file):
    with open(favourites_file, "w", encoding="utf-8") as file:
        file.write("# Favourites List\n")

print(f"Favourites file created at: {favourites_file}")

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

reset_button = ctk.CTkButton(preferences_tab, text="Reset All Preferences", fg_color="red", hover_color="darkred", command=reset_preferences)
reset_button.grid(row=11, column=0, columnspan=3, padx=10, pady=15, sticky="ew")

preferences_tab.rowconfigure(8, weight=1)

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

query_frame_channel = ctk.CTkFrame(channel_browser_tab)
query_frame_channel.pack(side="bottom", fill="x", padx=10, pady=10)
query_label_channel = ctk.CTkLabel(query_frame_channel, text="Query")
query_label_channel.pack(side="left", padx=5)
query_entry_channel = ctk.CTkEntry(query_frame_channel)
query_entry_channel.pack(side="left", padx=5, fill="x", expand=True)

query_frame_favourites = ctk.CTkFrame(favourites_tab)
query_frame_favourites.pack(side="bottom", fill="x", padx=10, pady=10)
query_label_favourites = ctk.CTkLabel(query_frame_favourites, text="Query")
query_label_favourites.pack(side="left", padx=5)
query_entry_favourites = ctk.CTkEntry(query_frame_favourites)
query_entry_favourites.pack(side="left", padx=5, fill="x", expand=True)

label = ctk.CTkLabel(about_tab, text="Mim", font=("Verdana", 16))
label.pack(pady=10)

textbox = ctk.CTkTextbox(about_tab, width=300, height=100)
textbox.insert("0.0", "")
textbox.pack(pady=10)

link = ctk.CTkLabel(about_tab, text="Mim.com", text_color="blue", cursor="hand2")
link.pack(pady=5)
link.bind("<Button-1>", lambda e: open_link())

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app.mainloop()









