# ==========================================================
# CASEQUEST
# CONFIDENTIAL INFORMATION PROTECTION SYSTEM
# GUI FOUNDATION
# ==========================================================


import customtkinter as ctk
from tkinter import messagebox
from ciphers import (
    caesar_encrypt,
    caesar_decrypt,
    additive_encrypt,
    additive_decrypt,
    vigenere_encrypt,
    vigenere_decrypt,
    affine_encrypt,
    affine_decrypt
)
from history import save_history, open_history
workspace = None
source_box = None
current_mode = None
input_label = None
cipher_menu = None
key_entry = None
mode_label = None
output_box = None
status_label = None
case_type = None
case_reference_entry = None

encrypted_available =False

# Your cipher engine will be connected later
# Keep this separate while we build the interface.

# ==========================================================
# PROTECTION WORKSPACE
# ==========================================================


def open_protection_workspace():

    global workspace
    global source_box
    global input_label
    global status_label
    global case_type
    global case_reference_entry



    for widget in app.winfo_children():

        widget.destroy()



    workspace = ctk.CTkFrame(
        app,
        fg_color=BACKGROUND
    )


    workspace.pack(
        fill="both",
        expand=True
    )



    # ======================================================
    # HEADER
    # ======================================================


    header = ctk.CTkFrame(
        workspace,
        fg_color=SURFACE,
        corner_radius=25
    )


    header.pack(
        padx=40,
        pady=20,
        fill="x"
    )


    ctk.CTkLabel(
    header,
    text="🔐 CASEQUEST",
    font=TITLE_FONT,
    text_color=CYAN
).pack(
    pady=(6,3)
)

    ctk.CTkLabel(
    header,
    text="Confidential Information Protection System",
    font=HEADER_FONT,
    text_color="#8FA8C7"
).pack()



    # ======================================================
    # CASE INFORMATION
    # ======================================================


    case_frame = ctk.CTkFrame(
        workspace,
        fg_color=SURFACE,
        corner_radius=20
    )


    case_frame.pack(
        padx=40,
        pady=10,
        fill="x"
    )


    ctk.CTkLabel(
        case_frame,
        text="CASE & EVIDENCE DETAILS",
        font=HEADER_FONT,
        text_color=CYAN
    ).grid(
        row=0,
        column=0,
        padx=20,
        pady=15
    )



    case_type = ctk.CTkComboBox(
        case_frame,
        width=250,
        values=[
            "Witness Statement",
            "Digital Evidence Record",
            "Legal Document",
            "Investigation Report",
            "Confidential Notes"
        ]
    )


    case_type.set(   
        "Select Information Type"
    )


    case_type.grid(
        row=0,
        column=1,
        padx=20
    )



    case_reference_entry = ctk.CTkEntry(
        case_frame,
        width=250,
        placeholder_text="Reference ID ( Example: CASE-2026-001 )"
    )


    case_reference_entry.grid(
        row=0,
        column=2,
        padx=20
    )



    # ======================================================
    # SOURCE INFORMATION
    # ======================================================


    source_frame = ctk.CTkFrame(
        workspace,
        fg_color=SURFACE,
        corner_radius=25
    )


    source_frame.pack(
        padx=40,
        pady=15,
        fill="x"
    )

    input_label = ctk.CTkLabel(
    source_frame,
    text="CONFIDENTIAL SOURCE INFORMATION",
    font=HEADER_FONT,
    text_color=CYAN
)

    input_label.pack(
    pady=10
)


    source_box = ctk.CTkTextbox(
        source_frame,
        height=100,
        font=NORMAL_FONT
    )


    source_box.pack(
        padx=25,
        pady=10,
        fill="x"
    )
   
    add_protection_controls(workspace)
    
    status_label = ctk.CTkLabel(
    workspace,
    text="● SYSTEM READY",
    font=NORMAL_FONT,
    text_color=GREEN
)

    status_label.pack(
    pady=8
) 

# ==========================================================
# APPLICATION THEME
# ==========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



# ==========================================================
# COLORS
# ==========================================================

BACKGROUND = "#050816"

SURFACE = "#0B1224"

SURFACE_LIGHT = "#111C35"

CYAN = "#00E5FF"

GREEN = "#00FF9D"

BLUE = "#007BFF"

TEAL = "#00B8B8"

RED = "#FF3B4D"

WHITE = "#F2F7FF"

TEXT = "#B8C7D9"



# ==========================================================
# FONTS
# ==========================================================

TITLE_FONT = (
    "Segoe UI",
    38,
    "bold"
)


SUBTITLE_FONT = (
    "Segoe UI",
    18
)


HEADER_FONT = (
    "Segoe UI",
    22,
    "bold"
)


NORMAL_FONT = (
    "Segoe UI",
    14
)


BUTTON_FONT = (
    "Segoe UI",
    15,
    "bold"
)



# ==========================================================
# MAIN WINDOW
# ==========================================================

app = ctk.CTk()


app.title(
    "CASEQUEST - Confidential Information Protection System"
)


app.geometry(
    "1200x750"
)


app.resizable(
    False,
    False
)


app.configure(
    fg_color=BACKGROUND
)

# ==========================================================
# STARTUP SECURITY INITIALIZATION
# ==========================================================


def security_startup_animation():

    startup_frame = ctk.CTkFrame(
        app,
        fg_color=BACKGROUND
    )

    startup_frame.pack(
        fill="both",
        expand=True
    )


    title = ctk.CTkLabel(
        startup_frame,
        text="🔐 CASEQUEST",
        font=TITLE_FONT,
        text_color=CYAN
    )

    title.pack(
        pady=(80, 10)
    )


    status = ctk.CTkLabel(
        startup_frame,
        text="Initializing secure environment...",
        font=NORMAL_FONT,
        text_color=TEXT
    )

    status.pack(
        pady=10
    )


    progress = ctk.CTkProgressBar(
        startup_frame,
        width=400
    )

    progress.pack(
        pady=20
    )

    progress.set(0)



    steps = [
        "Loading security modules...",
        "Preparing protection environment...",
        "Checking cipher systems...",
        "System initialization complete."
    ]


    def run_steps(index=0):

        if index < len(steps):

            status.configure(
                text=steps[index]
            )

            progress.set(
                (index + 1) / len(steps)
            )


            app.after(
                700,
                lambda: run_steps(index + 1)
            )


        else:

            startup_frame.destroy()

            create_welcome_screen()



    run_steps()

# ==========================================================
# WELCOME SCREEN
# ==========================================================


def create_welcome_screen():


    welcome_frame = ctk.CTkFrame(
        app,
        fg_color=SURFACE,
        corner_radius=35
    )


    welcome_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
        relwidth=0.55,
        relheight=0.65
    )



    ctk.CTkLabel(
        welcome_frame,
        text="🔐 CASEQUEST",
        font=TITLE_FONT,
        text_color=CYAN
    ).pack(
        pady=(60,5)
    )



    ctk.CTkLabel(
        welcome_frame,
        text="Confidential Information Protection System",
        font=HEADER_FONT,
        text_color="#8FA8C7"
    ).pack()



    ctk.CTkLabel(
        welcome_frame,
        text="Secure protection environment for sensitive records,\n"
             "digital evidence, witness information and legal documents.",
        font=NORMAL_FONT,
        text_color=TEXT
    ).pack(
        pady=25
    )



    status = ctk.CTkLabel(
        welcome_frame,
        text="● SECURITY SYSTEM ONLINE",
        font=NORMAL_FONT,
        text_color=GREEN
    )


    status.pack(
        pady=10
    )



    enter_button = ctk.CTkButton(
        welcome_frame,
        text="ENTER SECURE SYSTEM",
        width=300,
        height=55,
        fg_color=CYAN,
        hover_color=GREEN,
        text_color=BACKGROUND,
        font=BUTTON_FONT,
        command=open_protection_workspace
    ) 


    enter_button.pack(
        pady=35
    )



# ==========================================================
# PROTECTION CONTROLS AND OUTPUT
# ==========================================================

def set_encrypt_mode():

    global current_mode

    current_mode = "encrypt"
    status_label.configure(
    text="● ENCRYPTION MODULE READY",
    text_color=CYAN
)


    mode_label.configure(
        text="OPERATION: ENCRYPTION READY",
        text_color=CYAN
    )


    key_entry.configure(
        placeholder_text="Enter encryption key"
    )


    input_label.configure(
        text="CONFIDENTIAL SOURCE INFORMATION"
    )





def set_decrypt_mode():

    global current_mode

    current_mode = "decrypt"
    status_label.configure(
    text="● DECRYPTION MODULE READY",
    text_color=TEAL
)


    mode_label.configure(
        text="OPERATION: DECRYPTION READY",
        text_color=TEAL
    )


    key_entry.configure(
        placeholder_text="Enter decryption key"
    )


    input_label.configure(
        text="ENCRYPTED INFORMATION TO RESTORE"
    )

def show_result_popup():

    popup = ctk.CTkToplevel(app)
    popup.title("Protection Complete")
    popup.geometry("420x350")
    popup.resizable(False, False)
    popup.configure(fg_color=SURFACE)

    operation = "Encryption" if current_mode == "encrypt" else "Decryption"

    status = (
        "Protected Successfully"
        if current_mode == "encrypt"
        else "Information Successfully Restored"
    )

    ctk.CTkLabel(
        popup,
        text="✔ PROTECTION COMPLETE",
        font=HEADER_FONT,
        text_color=GREEN
    ).pack(pady=(20,15))

    ctk.CTkLabel(
        popup,
        text=f"Operation: {operation}",
        font=NORMAL_FONT,
        text_color=TEXT
    ).pack(pady=4)

    ctk.CTkLabel(
        popup,
        text=f"Cipher: {cipher_menu.get()}",
        font=NORMAL_FONT,
        text_color=TEXT
    ).pack(pady=4)

    ctk.CTkLabel(
        popup,
        text=f"Status: {status}",
        font=NORMAL_FONT,
        text_color=CYAN
    ).pack(pady=10)

    ctk.CTkButton(
        popup,
        text="VIEW OUTPUT",
        fg_color=CYAN,
        text_color=BACKGROUND,
        command=popup.destroy
    ).pack(pady=10)

    ctk.CTkButton(
        popup,
        text="CLOSE",
        fg_color=GREEN,
        text_color=BACKGROUND,
        command=popup.destroy
    ).pack()

def execute_protection():

    global current_mode
    global encrypted_available


    message = source_box.get(
        "1.0",
        "end"
    ).strip()

    
    cipher = cipher_menu.get()
    key = key_entry.get().strip()
    reference = case_reference_entry.get().strip()


    # ==========================
    # VALIDATION
    # ==========================
        
    if reference == "":
            
            messagebox.showerror(
                "Missing Reference",
                "Enter a Case Reference."
            )
            
            return
    

    if not message:

        messagebox.showerror(
            "Missing Information",
            "Enter confidential source information first."
        )

        return



    if cipher == "Select Cipher Method":

        messagebox.showerror(
            "Missing Cipher",
            "Select a cipher method first."
        )

        return



    if current_mode is None:

        messagebox.showerror(
            "Operation Required",
            "Choose Encrypt or Decrypt first."
        )

        return



    if not key:

        messagebox.showerror(
            "Missing Key",
            "Enter the required security key."
        )

        return



    if current_mode == "decrypt" and encrypted_available is False:

        messagebox.showerror(
            "No Encrypted Data",
            "Decryption requires previously protected encrypted information."
        )

        return



    # ==========================
    # ENCRYPTION / DECRYPTION
    # ==========================


    try:


        if cipher == "Caesar Cipher":


            if current_mode == "encrypt":

                result = caesar_encrypt(
                    message,
                    int(key)
                )

                encrypted_available = True


            else:

                result = caesar_decrypt(
                    message,
                    int(key)
                )



        elif cipher == "Additive Cipher":


            if current_mode == "encrypt":

                result = additive_encrypt(
                    message,
                    int(key)
                )

                encrypted_available = True


            else:

                result = additive_decrypt(
                    message,
                    int(key)
                )



        elif cipher == "Affine Cipher":


            values = key.split(",")


            if len(values) != 2:

                messagebox.showerror(
                    "Invalid Key",
                    "Affine requires two values: a,b"
                )

                return



            a = int(values[0].strip())

            b = int(values[1].strip())



            if current_mode == "encrypt":

                result = affine_encrypt(
                    message,
                    a,
                    b
                )

                encrypted_available = True


            else:

                result = affine_decrypt(
                    message,
                    a,
                    b
                )



        elif cipher == "Vigenere Cipher":

            if not key.isalpha():
             messagebox.showerror(
            "Invalid Key",
            "Vigenere key must contain letters only."
            )
            
    
            if current_mode == "encrypt":

                result = vigenere_encrypt(
                    message,
                    key
                )

                encrypted_available = True


            else:

                result = vigenere_decrypt(
                    message,
                    key
                )



        else:

            messagebox.showerror(
                "Unavailable Cipher",
                "Selected cipher is not connected."
            )

            return



        output_box.delete(
            "1.0",
            "end"
        )


        output_box.insert(
            "end",
            result
        )
        
        
        operation = "Encryption" if current_mode == "encrypt" else "Decryption"

        save_history(

        case_reference_entry.get().strip(),

        case_type.get(),

        cipher,

        operation,

    result

)
        
        show_result_popup()
        
    
        if current_mode == "encrypt":

           status_label.configure(
           text="● PROTECTION PROCESS COMPLETE",
           text_color=GREEN
        )

        else:

          status_label.configure(
          text="● RESTORATION PROCESS COMPLETE",
          text_color=GREEN
        )
    
    except ValueError:


        messagebox.showerror(
            "Invalid Key",
            "Key format is invalid for this cipher."
        )



def add_protection_controls(workspace):

    global cipher_menu
    global key_entry
    global mode_label
    global output_box



    protection_frame = ctk.CTkFrame(
        workspace,
        fg_color=SURFACE,
        corner_radius=25
    )


    protection_frame.pack(
        padx=40,
        pady=10,
        fill="x"
    )



    ctk.CTkLabel(
        protection_frame,
        text="PROTECTION SETTINGS",
        font=HEADER_FONT,
        text_color=CYAN
    ).pack(
        pady=8
    )



    controls_row = ctk.CTkFrame(
        protection_frame,
        fg_color=SURFACE
    )


    controls_row.pack(
        pady=5
    )



    cipher_menu = ctk.CTkComboBox(
        controls_row,
        width=220,
        values=[
            "Caesar Cipher",
            "Additive Cipher",
            "Vigenere Cipher",
            "Affine Cipher"
        ]
    )


    cipher_menu.set(
        "Select Cipher Method"
    )


    cipher_menu.grid(
        row=0,
        column=0,
        padx=10
    )



    mode_label = ctk.CTkLabel(
        controls_row,
        text="OPERATION: WAITING",
        font=NORMAL_FONT,
        text_color=TEXT
    )


    mode_label.grid(
        row=0,
        column=1,
        padx=15
    )



    key_entry = ctk.CTkEntry(
        controls_row,
        width=240,
        placeholder_text="Select operation first"
    )


    key_entry.grid(
        row=0,
        column=2,
        padx=10
    )



    button_row = ctk.CTkFrame(
        protection_frame,
        fg_color=SURFACE
    )


    button_row.pack(
        pady=10
    )



    ctk.CTkButton(
        button_row,
        text="🔒 ENCRYPT",
        width=150,
        height=40,
        fg_color=BLUE,
        font=BUTTON_FONT,
        command=set_encrypt_mode
    ).grid(
        row=0,
        column=0,
        padx=10
    )



    ctk.CTkButton(
        button_row,
        text="🔓 DECRYPT",
        width=150,
        height=40,
        fg_color=TEAL,
        font=BUTTON_FONT,
        command=set_decrypt_mode
    ).grid(
        row=0,
        column=1,
        padx=10
    )



    ctk.CTkButton(
        button_row,
        text="▶ EXECUTE",
        width=180,
        height=40,
        fg_color=GREEN,
        text_color=BACKGROUND,
        font=BUTTON_FONT,
        command=execute_protection
    ).grid(
        row=0,
        column=2,
        padx=10
    )

    ctk.CTkButton(

    button_row,

    text="📜 HISTORY",

    width=180,

    height=40,

    fg_color=CYAN,

    text_color=BACKGROUND,

    font=BUTTON_FONT,

    command=lambda: open_history(app)

).grid(

    row=0,

    column=3,

    padx=10

)


    output_frame = ctk.CTkFrame(
        workspace,
        fg_color=SURFACE,
        corner_radius=25
    )


    output_frame.pack(
        padx=40,
        pady=10,
        fill="x"
    )



    ctk.CTkLabel(
        output_frame,
        text="PROTECTED OUTPUT",
        font=HEADER_FONT,
        text_color=CYAN
    ).pack(
        pady=5
    )



    output_box = ctk.CTkTextbox(
        output_frame,
        height=80,
        font=NORMAL_FONT
    )


    output_box.pack(
        padx=25,
        pady=5,
        fill="x"
    )



# ==========================================================
# START
# ==========================================================

security_startup_animation()

app.mainloop()