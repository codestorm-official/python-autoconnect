# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import random

# --- UI Configuration ---
BACKGROUND_COLOR = "#f0f2f5"
FONT_FAMILY = "Segoe UI"
PRIMARY_COLOR = "#0078d4" # Blue
GREEN_COLOR = "#107c10"
RED_COLOR = "#d83b01" # Red
ORANGE_COLOR = "#f7630c"

# --- Main Application Class ---
class VPNApp:
    def __init__(self, root):
        """Initialize the application and all its components."""
        self.root = root
        self.state = "DISCONNECTED"  # Initial state
        self._setup_ui()
        self._update_ui()

    def _setup_ui(self):
        """Prepare all widgets and the main window layout."""
        self.root.title("Mockup VPN Client")
        self.root.geometry("380x420")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND_COLOR)

        # Style for ttk widgets
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure('TButton', font=(FONT_FAMILY, 14, 'bold'), padding=10)
        
        ### MODIFICATION STARTS HERE ###
        # --- NEW STYLE FOR COLORED BUTTONS ---
        
        # Style for Connect button (blue)
        style.configure('Connect.TButton', background=PRIMARY_COLOR, foreground='white')
        style.map('Connect.TButton',
            background=[('active', '#005a9e')]) # Hover color

        # Style for Disconnect button (red)
        style.configure('Disconnect.TButton', background=RED_COLOR, foreground='white')
        style.map('Disconnect.TButton',
            background=[('active', '#a82c00')]) # Hover color
        
        ### MODIFICATION ENDS ###

        style.configure('TLabel', font=(FONT_FAMILY, 12), background=BACKGROUND_COLOR)
        style.configure('Status.TLabel', font=(FONT_FAMILY, 16, 'bold'))
        style.configure('IP.TLabel', font=(FONT_FAMILY, 11), foreground="#555")

        # Main frame for padding
        main_frame = ttk.Frame(self.root, padding="20 20 20 20", style='TFrame')
        main_frame.pack(expand=True, fill='both')

        # Icon/Logo (as simple text)
        self.logo_label = ttk.Label(main_frame, text="Secure VPN", font=(FONT_FAMILY, 24, 'bold'))
        self.logo_label.pack(pady=10)
        
        # App Name Label
        self.app_name_label = ttk.Label(main_frame, text="SecureNet VPN", font=(FONT_FAMILY, 18, 'bold'))
        self.app_name_label.pack(pady=(0, 20))

        # Label to display connection status
        self.status_label = ttk.Label(main_frame, text="", style='Status.TLabel')
        self.status_label.pack(pady=10)
        
        # Label to display fake IP address when connected
        self.ip_label = ttk.Label(main_frame, text="", style='IP.TLabel')
        self.ip_label.pack(pady=5)

        # Progress bar to simulate connection process
        self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress_bar.pack(pady=10, fill='x', padx=20)

        # Main button for Connect/Disconnect
        self.connect_button = ttk.Button(main_frame, text="", command=self.toggle_connection)
        self.connect_button.pack(pady=20, fill='x', padx=20)

    def _update_ui(self):
        """Update all UI widgets based on the current application state."""
        if self.state == "DISCONNECTED":
            self.status_label.config(text="Status: Disconnected", foreground=RED_COLOR)
            self.ip_label.config(text="")
            self.connect_button.config(text="Connect", state="normal", style='Connect.TButton')
            self.progress_bar.stop()
            self.progress_bar.pack_forget()

        elif self.state == "CONNECTING":
            self.status_label.config(text="Status: Connecting...", foreground=ORANGE_COLOR)
            self.connect_button.config(text="Connecting...", state="disabled", style='TButton')
            self.progress_bar.pack(pady=10, fill='x', padx=20)
            self.progress_bar.start(10)

        elif self.state == "CONNECTED":
            self.status_label.config(text="Status: Connected", foreground=GREEN_COLOR)
            fake_ip = f"Your IP: 188.{random.randint(10, 255)}.{random.randint(10, 255)}.{random.randint(10, 255)}"
            self.ip_label.config(text=fake_ip)
            self.connect_button.config(text="Disconnect", state="normal", style='Disconnect.TButton')
            self.progress_bar.stop()
            self.progress_bar.pack_forget()

        elif self.state == "DISCONNECTING":
            self.status_label.config(text="Status: Disconnecting...", foreground=ORANGE_COLOR)
            self.connect_button.config(text="Disconnecting...", state="disabled", style='TButton')
            self.progress_bar.pack(pady=10, fill='x', padx=20)
            self.progress_bar.start(10)

    def toggle_connection(self):
        if self.state == "DISCONNECTED":
            self._connect()
        elif self.state == "CONNECTED":
            self._disconnect()

    def _connect(self):
        self.state = "CONNECTING"
        self._update_ui()
        self.root.after(2500, self._finish_connection)
        
    def _finish_connection(self):
        self.state = "CONNECTED"
        self._update_ui()

    def _disconnect(self):
        self.state = "DISCONNECTING"
        self._update_ui()
        self.root.after(1500, self._finish_disconnection)

    def _finish_disconnection(self):
        self.state = "DISCONNECTED"
        self._update_ui()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root_window = tk.Tk()
    app = VPNApp(root_window)
    app.run()