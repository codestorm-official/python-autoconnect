# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import random

# --- Konfigurasi Tampilan ---
BACKGROUND_COLOR = "#f0f2f5"
FONT_FAMILY = "Segoe UI"
PRIMARY_COLOR = "#0078d4" # Biru
GREEN_COLOR = "#107c10"
RED_COLOR = "#d83b01" # Merah
ORANGE_COLOR = "#f7630c"

# --- Kelas Utama Aplikasi ---
class VPNApp:
    def __init__(self, root):
        """Inisialisasi aplikasi dan semua komponennya."""
        self.root = root
        self.state = "DISCONNECTED"  # State awal aplikasi
        self._setup_ui()
        self._update_ui()

    def _setup_ui(self):
        """Mempersiapkan semua widget dan tampilan jendela utama."""
        self.root.title("Mockup VPN Client")
        self.root.geometry("380x420")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND_COLOR)

        # Style untuk widget ttk
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure('TButton', font=(FONT_FAMILY, 14, 'bold'), padding=10)
        
        ### MODIFIKASI DIMULAI DI SINI ###
        # --- STYLE BARU UNTUK TOMBOL BERWARNA ---
        
        # Style untuk tombol Connect (biru)
        style.configure('Connect.TButton', background=PRIMARY_COLOR, foreground='white')
        style.map('Connect.TButton',
            background=[('active', '#005a9e')]) # Warna saat kursor mouse di atasnya (hover)

        # Style untuk tombol Disconnect (merah)
        style.configure('Disconnect.TButton', background=RED_COLOR, foreground='white')
        style.map('Disconnect.TButton',
            background=[('active', '#a82c00')]) # Warna saat hover
        
        ### MODIFIKASI SELESAI ###

        style.configure('TLabel', font=(FONT_FAMILY, 12), background=BACKGROUND_COLOR)
        style.configure('Status.TLabel', font=(FONT_FAMILY, 16, 'bold'))
        style.configure('IP.TLabel', font=(FONT_FAMILY, 11), foreground="#555")

        # Frame utama untuk padding
        main_frame = ttk.Frame(self.root, padding="20 20 20 20", style='TFrame')
        main_frame.pack(expand=True, fill='both')

        # Icon/Logo (sebagai teks sederhana)
        self.logo_label = ttk.Label(main_frame, text="Secure VPN", font=(FONT_FAMILY, 24, 'bold'))
        self.logo_label.pack(pady=10)
        
        # Label Nama Aplikasi
        self.app_name_label = ttk.Label(main_frame, text="SecureNet VPN", font=(FONT_FAMILY, 18, 'bold'))
        self.app_name_label.pack(pady=(0, 20))

        # Label untuk menampilkan status koneksi
        self.status_label = ttk.Label(main_frame, text="", style='Status.TLabel')
        self.status_label.pack(pady=10)
        
        # Label untuk menampilkan IP address palsu saat terhubung
        self.ip_label = ttk.Label(main_frame, text="", style='IP.TLabel')
        self.ip_label.pack(pady=5)

        # Progress bar untuk simulasi proses koneksi
        self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress_bar.pack(pady=10, fill='x', padx=20)

        # Tombol utama untuk Connect/Disconnect
        self.connect_button = ttk.Button(main_frame, text="", command=self.toggle_connection)
        self.connect_button.pack(pady=20, fill='x', padx=20)

    def _update_ui(self):
        """Memperbarui semua widget UI berdasarkan state aplikasi saat ini."""
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