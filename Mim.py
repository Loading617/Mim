import customtkinter as ctk
import requests
import re
import os
import webbrowser
from tkinter import filedialog

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

tabs = ["Grid Browser", "Channel Browser", "Favourites", "Preferences", "Search", "Remote", "About"]
for tab_name in tabs:
    tabview.add(tab_name)

tabview.set("Preferences")
tabview._segmented_button.configure(font=("Verdana", 8))

grid_browser_tab = tabview.tab("Grid Browser")
channel_browser_tab = tabview.tab("Channel Browser")
favourites_tab = tabview.tab("Favourites")
preferences_tab = tabview.tab("Preferences")
search_tab = tabview.tab("Search")
remote_tab = tabview.tab("Remote")
about_tab = tabview.tab("About")

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

def update_grid_browser(channels):
    """Update Grid Browser with channel names."""
    for widget in grid_browser_frame.winfo_children():
        widget.destroy()
    
    row, col = 0, 0
    for name, url in channels:
        label = ctk.CTkLabel(grid_browser_frame, text=name, padx=10, pady=5, fg_color="gray30")
        label.grid(row=row, column=col, padx=5, pady=5)
        
        col += 1
        if col >= 3:
            col = 0
            row += 1

def add_url(url):
    """Handles adding an M3U/M3U8 URL."""
    content = fetch_m3u(url)
    if content:
        channels = parse_m3u(content)
        update_grid_browser(channels)
        
def browse_folder():
    file_path = filedialog.askopenfilename(filetypes=[("M3U Playlist", "*.m3u"), ("M3U8 Playlist", "*.m3u8")])
    if file_path:
        entry_list_hierarchy.delete(0, ctk.END)
        entry_list_hierarchy.insert(0, file_path)
        load_m3u_channels(file_path)

def load_m3u_channels(file_path):
    """Read M3U/M3U8 file and display URLs in the grid view."""
    for widget in grid_browser_frame.winfo_children():
        widget.destroy()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        urls = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

        row, col = 0, 0
        for url in urls:
            label = ctk.CTkLabel(grid_browser_frame, text=url, padx=5, pady=5, fg_color="gray30", corner_radius=5)
            label.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            col += 1
            if col >= 3:
                col = 0
                row += 1

    except Exception as e:
        print("Error loading M3U file:", e)

def add_url():
    """Handles adding an M3U/M3U8 URL with a checkbox to enable/disable channels."""
    url = entry_list_url.get().strip()
    if not url:
        return

    check_var = ctk.IntVar()

    def toggle_channels():
        """Add or remove channels based on the checkbox state."""
        if check_var.get():
            content = fetch_m3u(url)
            if content:
                channels = parse_m3u(content)
                update_grid_browser(channels)
        else:
            for widget in grid_browser_frame.winfo_children():
                widget.destroy()

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

mim_folder = os.path.join(downloads_path, "MimData")

if not os.path.exists(mim_folder):
    os.makedirs(mim_folder)

favourites_file = os.path.join(mim_folder, "favourites.mim")

if not os.path.exists(favourites_file):
    with open(favourites_file, "w", encoding="utf-8") as file:
        file.write("# Favourites List\n")

print(f"Favourites file created at: {favourites_file}")

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

label_remote = ctk.CTkLabel(remote_tab, text="You can open the Remote by pressing the button below, by pressing Open Remote, a remote window will open. When it opens, you click the icon to return to the main window. And the remote, you are presented favorite channel buttons from 1 to 10.", font=("Verdana", 12, "bold"), padx=10, pady=10)

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

app.mainloop()
