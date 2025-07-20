
import customtkinter as ctk

# ✅ Custom Button
class AppButton(ctk.CTkButton):
    def __init__(self, parent, text, command=None):
        super().__init__(
            master=parent,
            text=text,
            command=command,
            fg_color="#1f538d",      # Dark Blue
            hover_color="#144870",   # Slightly darker blue
            text_color="white",
            corner_radius=8,
            font=("Arial", 14, "bold")
        )

# ✅ Custom Entry
class AppEntry(ctk.CTkEntry):
    def __init__(self, parent, placeholder=""):
        super().__init__(
            master=parent,
            placeholder_text=placeholder,
            width=200,
            height=35,
            fg_color="#1a1a1a",      # Dark background
            border_color="#1f538d",  # Blue border
            text_color="white",
            corner_radius=6,
            font=("Arial", 13)
        )

def center_window(window, width=None, height=None):
    window.update_idletasks()  # Ensure window size is calculated

    if width is None or height is None:
        width = window.winfo_width()
        height = window.winfo_height()

    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
