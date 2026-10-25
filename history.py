# ==========================================================
# CASEQUEST
# Protection History Module
# File: history.py
# ==========================================================

import customtkinter as ctk
import json
import os
from datetime import datetime
from tkinter import messagebox

# ==========================================================
# HISTORY FILE
# ==========================================================

HISTORY_FILE = "history.json"

# ==========================================================
# CASEQUEST THEME
# ==========================================================

BACKGROUND = "#050816"

SURFACE = "#0B1224"

SURFACE_LIGHT = "#111C35"

CYAN = "#00E5FF"

GREEN = "#00FF9D"

BLUE = "#4DA6FF"

RED = "#FF3B4D"

TEXT = "#B8C7D9"

WHITE = "#F2F7FF"

# ==========================================================
# FONTS
# ==========================================================

TITLE_FONT = (
    "Segoe UI",
    28,
    "bold"
)

HEADER_FONT = (
    "Segoe UI",
    20,
    "bold"
)

NORMAL_FONT = (
    "Segoe UI",
    14
)

BUTTON_FONT = (
    "Segoe UI",
    14,
    "bold"
)

# ==========================================================
# CREATE HISTORY FILE
# ==========================================================

def initialize_history():

    if not os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "w"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )

# ==========================================================
# LOAD HISTORY
# ==========================================================

def load_history():

    initialize_history()

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return []

# ==========================================================
# SAVE HISTORY
# ==========================================================

def write_history(history):

    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )

# ==========================================================
# SAVE NEW RECORD
# ==========================================================

def save_history(

    case_reference,

    information_type,

    cipher,

    operation,

    output

):

    history = load_history()

    record = {

        "case_reference": case_reference,

        "information_type": information_type,

        "cipher": cipher,

        "operation": operation,

        "output": output,

        "date": datetime.now().strftime(
            "%d %B %Y"
        ),

        "time": datetime.now().strftime(
            "%I:%M:%S %p"
        )

    }
    
    if len(history) >= 100:

     history.pop(0)

    history.append(record)

    write_history(history)

# ==========================================================
# HISTORY STATISTICS
# ==========================================================

def history_statistics():

    history = load_history()

    total = len(history)

    encryptions = 0

    decryptions = 0

    for record in history:

        if record["operation"] == "Encryption":

            encryptions += 1

        else:

            decryptions += 1

    return (

        total,

        encryptions,

        decryptions

    )

# ==========================================================
# PLACEHOLDERS
# ==========================================================

history_window = None

history_table = None

selected_record = None


# ==========================================================
# CLOSE HISTORY
# ==========================================================

def close_history():

    global history_window

    if history_window is not None:

        history_window.destroy()

        history_window = None


# ==========================================================
# CLEAR HISTORY
# ==========================================================

def clear_history():

    answer = messagebox.askyesno(

        "Clear History",

        "Delete every protection record?"

    )

    if not answer:

        return

    write_history([])

    messagebox.showinfo(

        "History",

        "Protection history cleared successfully."

    )

    close_history()
    
# ==========================================================
# VIEW RECORD
# ==========================================================

def view_record():

    history = load_history()

    value = selected_record.get().strip()

    if value == "":

        messagebox.showerror(

            "Missing Record",

            "Enter a record number."

        )

        return

    try:

        index = int(value) - 1

    except ValueError:

        messagebox.showerror(

            "Invalid Record",

            "Record number must be numeric."

        )

        return

    if index < 0 or index >= len(history):

        messagebox.showerror(

            "Record Not Found",

            "That record does not exist."

        )

        return

    record = history[index]

    details = ctk.CTkToplevel(history_window)

    details.title(

        "Protection Record"

    )

    details.geometry(

        "650x520"

    )

    details.resizable(

        False,

        False

    )

    details.configure(

        fg_color=BACKGROUND

    )

    frame = ctk.CTkFrame(

        details,

        fg_color=SURFACE,

        corner_radius=25

    )

    frame.pack(

        padx=25,

        pady=25,

        fill="both",

        expand=True

    )

    ctk.CTkLabel(

        frame,

        text="✔ PROTECTION RECORD",

        font=TITLE_FONT,

        text_color=CYAN

    ).pack(

        pady=20

    )

    info = (

        f"Case Reference:\n{record['case_reference']}\n\n"

        f"Information Type:\n{record['information_type']}\n\n"

        f"Cipher Method:\n{record['cipher']}\n\n"

        f"Operation:\n{record['operation']}\n\n"

        f"Date:\n{record['date']}\n\n"

        f"Time:\n{record['time']}\n\n"

        f"Protected Output:\n\n{record['output']}"

    )

    textbox = ctk.CTkTextbox(

        frame,

        height=300,

        font=NORMAL_FONT

    )

    textbox.pack(

        padx=20,

        pady=10,

        fill="both",

        expand=True

    )

    textbox.insert(

        "1.0",

        info

    )

    textbox.configure(

        state="disabled"

    )
    
    textbox.configure(
    cursor="arrow"
)

    ctk.CTkButton(

        frame,

        text="CLOSE",

        width=170,

        fg_color=GREEN,

        text_color=BACKGROUND,

        font=BUTTON_FONT,

        command=details.destroy

    ).pack(

        pady=15

    )

     
# ==========================================================
# OPEN HISTORY WINDOW
# ==========================================================

def open_history(app):

    global history_window
    global history_table
    global selected_record

    if history_window is not None:

        try:

            history_window.focus()

            return

        except:

            history_window = None

    history_window = ctk.CTkToplevel(app)

    history_window.title(
        "CASEQUEST Protection History"
    )
    
    history_window.geometry(
    "1050x680"
    )
    
    history_window.resizable(
        False,
        False
    )

    history_window.configure(
        fg_color=BACKGROUND
    )

    history_window.protocol(
        "WM_DELETE_WINDOW",
        lambda: close_history()
    )



    # ======================================================
    # HEADER
    # ======================================================

    header = ctk.CTkFrame(

    history_window,

    fg_color=SURFACE,

    corner_radius=25

    )

    header.pack(

    padx=25,

    pady=20,

    fill="x"

    )



    ctk.CTkLabel(

        header,

        text="📜 CASEQUEST PROTECTION HISTORY",

        font=TITLE_FONT,

        text_color=CYAN

    ).pack(

        pady=(15,5)

    )



    ctk.CTkLabel(

        header,

        text="Activity Log of Protected Information",

        font=NORMAL_FONT,

        text_color=TEXT

    ).pack(

        pady=(0,15)

    )



    # ======================================================
    # STATISTICS
    # ======================================================

    total, encryptions, decryptions = history_statistics()



    statistics_frame = ctk.CTkFrame(

        history_window,

        fg_color=BACKGROUND

    )

    statistics_frame.pack(

        pady=10,

        fill="x"

    )



    def statistic_card(title,value,color):

        card = ctk.CTkFrame(

            statistics_frame,

            width=250,

            height=95,

            fg_color=SURFACE,

            corner_radius=18

        )

        card.pack(

            side="left",

            padx=15,

            expand=True

        )



        ctk.CTkLabel(

            card,

            text=str(value),

            font=("Segoe UI",30,"bold"),

            text_color=color

        ).pack(

            pady=(15,0)

        )



        ctk.CTkLabel(

            card,

            text=title,

            font=NORMAL_FONT,

            text_color=TEXT

        ).pack(

            pady=(0,12)

        )



    statistic_card(

        "TOTAL OPERATIONS",

        total,

        CYAN

    )



    statistic_card(

        "ENCRYPTIONS",

        encryptions,

        GREEN

    )



    statistic_card(

        "DECRYPTIONS",

        decryptions,

        BLUE

    )



    # ======================================================
    # HISTORY TABLE
    # ======================================================

    table_frame = ctk.CTkFrame(

        history_window,

        fg_color=SURFACE,

        corner_radius=25

    )

    table_frame.pack(

        padx=25,

        pady=20,

        fill="both",

        expand=True

    )



    ctk.CTkLabel(

        table_frame,

        text="RECENT PROTECTION OPERATIONS",

        font=HEADER_FONT,

        text_color=CYAN

    ).pack(

        pady=12

    )



    history_table = ctk.CTkTextbox(

        table_frame,

        height=200,

        font=("Consolas",13),

        fg_color=SURFACE_LIGHT,

        text_color=WHITE

    )



    history_table.pack(

        padx=20,

        pady=10,

        fill="both",

        expand=True

    )



    history_table.delete(

        "1.0",

        "end"

    )



    history = load_history()



    if len(history) == 0:

        history_table.insert(

            "end",

            "\n\nNo protection history available."

        )



    else:

        header_text = (

            f"{'No.':<5}"

            f"{'Reference':<18}"

            f"{'Type':<22}"

            f"{'Cipher':<18}"

            f"{'Operation'}\n"

        )



        history_table.insert(

            "end",

            header_text

        )



        history_table.insert(

            "end",

            "-"*90+"\n"

        )



        for index,record in enumerate(history,start=1):

            history_table.insert(

                "end",

                f"{index:<5}"

                f"{record['case_reference'][:16]:<18}"

                f"{record['information_type'][:20]:<22}"

                f"{record['cipher'][:16]:<18}"

                f"{record['operation']}\n"

            )



    history_table.configure(

        state="disabled"

    )



    selected_record = ctk.CTkEntry(

        history_window,

        width=220,

        placeholder_text="Enter record number"

    )


    selected_record.pack(

      pady=(5,12)

)

    # ======================================================
    # BUTTONS
    # ======================================================

    button_frame = ctk.CTkFrame(

    history_window,

    fg_color=BACKGROUND

)

    button_frame.pack(

        pady=15

)



    ctk.CTkButton(

    button_frame,

    text="👁 VIEW DETAILS",

    width=170,

    height=40,

    fg_color=BLUE,

    hover_color=CYAN,

    text_color=BACKGROUND,

    font=BUTTON_FONT,

    command=view_record

).grid(

    row=0,

    column=0,

    padx=12

)



    ctk.CTkButton(

    button_frame,

    text="🗑 CLEAR HISTORY",

    width=170,

    height=40,

    fg_color=RED,

    hover_color="#FF5E6C",

    text_color=WHITE,

    font=BUTTON_FONT,

    command=clear_history

).grid(

    row=0,

    column=1,

    padx=12

)



    ctk.CTkButton(

    button_frame,

    text="✖ CLOSE",

    width=150,

    height=40,

    fg_color=GREEN,

    hover_color=CYAN,

    text_color=BACKGROUND,

    font=BUTTON_FONT,

    command=close_history

).grid(

    row=0,

    column=2,

    padx=12

)


# ==========================================================
# REFRESH HISTORY WINDOW
# ==========================================================

def refresh_history(app):

    global history_window

    if history_window is not None:

        try:

            history_window.destroy()

        except:

            pass

        history_window = None

    open_history(app)


# ==========================================================
# HISTORY AVAILABLE
# ==========================================================

def history_count():

    return len(load_history())


# ==========================================================
# MODULE TEST
# ==========================================================

if __name__ == "__main__":

    root = ctk.CTk()

    root.geometry("300x150")

    root.withdraw()

    open_history(root)

    root.mainloop()