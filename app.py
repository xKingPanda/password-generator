import tkinter as tk
from tkinter import ttk

#This is the function to generate a passwored
def generate_password():
    password_output.set("Password will go here")


#This sets the variables for the window
def main():
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("500x400")
    
#Stores the password in a string
    global password_output
    password_output = tk.StringVar()

#Frame to hold all the buttons and outputs
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill="both", expand=True)



    title_label = ttk.Label(
        main_frame,
        text="Password Generator",
        font=("Segoe UI", 20, "bold")
    )
    title_label.pack(anchor="w")


    subtitle_label = ttk.Label(
        main_frame,
        text="Create a strong random password"
    )
    subtitle_label.pack(anchor="w", pady=(0, 20))


#PASSWORD BOX
    password_entry = ttk.Entry(
        main_frame,
        textvariable=password_output,
        font=("Consolas", 14),
        state="readonly"
    )
    password_entry.pack(fill="x", padx=(0, 12))


#GENERATE BOTTON
    generate_button = ttk.Button(
        main_frame,
        text="Generate Password",
        command=generate_password
    )
    generate_button.pack(fill="x")





    root.mainloop()

if __name__ == "__main__":
    main()