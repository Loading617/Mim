import customtkinter as ctk

app = ctk.CTk()

app.title("Mim")
app.geometry("440x620")

tab_frame = ctk.CTkFrame(app)
tab_frame.pack(side="top", fill="x")

tab1_btn = ctk.CTkButton(tab_frame, text="Grid Browser") 
tab2_btn = ctk.CTkButton(tab_frame, text="Channel Browser") 
tab3_btn = ctk.CTkButton(tab_frame, text="Favorites")
tab4_btn = ctk.CTkButton(tab_frame, text="Preferences")
tab5_btn = ctk.CTkButton(tab_frame, text="Search")
tab6_btn = ctk.CTkButton(tab_frame, text="Remote")
tab7_btn = ctk.CTkButton(tab_frame, text="About")

tab1_btn.pack(side="left", padx=10, pady=5)
tab2_btn.pack(side="left", padx=10, pady=5)
tab3_btn.pack(side="left", padx=10, pady=5)
tab4_btn.pack(side="left", padx=10, pady=5)
tab5_btn.pack(side="left", padx=10, pady=5)
tab6_btn.pack(side="left", padx=10, pady=5)
tab7_btn.pack(side="left", padx=10, pady=5)

tab1_frame = ctk.CTkFrame(app)
tab2_frame = ctk.CTkFrame(app)
tab3_frame = ctk.CTkFrame(app)
tab4_frame = ctk.CTkFrame(app)
tab5_frame = ctk.CTkFrame(app)
tab6_frame = ctk.CTkFrame(app)
tab7_frame = ctk.CTkFrame(app)

tab1_frame.pack(fill="both", expand="true")
tab2_frame.pack(fill="both", expand="true")
tab3_frame.pack(fill="both", expand="true")
tab4_frame.pack(fill="both", expand="true")
tab5_frame.pack(fill="both", expand="true")
tab6_frame.pack(fill="both", expand="true")
tab7_frame.pack(fill="both", expand="true")

def switch_tab(tab): tab1_frame.pack_forget()
tab2_frame.pack_forget()
tab3_frame.pack_forget()
tab4_frame.pack_forget()
tab5_frame.pack_forget()
tab6_frame.pack_forget()
tab7_frame.pack_forget()

if tab == 1: tab1_frame.pack(fill="both", expand=True)
elif tab == 2: tab2_frame.pack(fill="both", expand=True)
elif tab == 3: tab3_frame.pack(fill="both", expand=True)
elif tab == 4: tab4_frame.pack(fill="both", expand=True)
elif tab == 5: tab5_frame.pack(fill="both", expand=True)
elif tab == 6: tab6_frame.pack(fill="both", expand=True)
elif tab == 7: tab7_frame.pack(fill="both", expand=True)

tab1_btn.configure(command=lambda: switch_tab(1))
tab2_btn.configure(command=lambda: switch_tab(2))
tab3_btn.configure(command=lambda: switch_tab(3))
tab4_btn.configure(command=lambda: switch_tab(4))
tab5_btn.configure(command=lambda: switch_tab(5))
tab6_btn.configure(command=lambda: switch_tab(6))
tab7_btn.configure(command=lambda: switch_tab(7))

def disable_fullscreen():
    app.attributes("-fullscreen", False)

tabview.set("Preferences")

app.bind("<Escape>", lambda event: disable_fullscreen())

app.mainloop()
