# Python GUI Auto-Connect Monitor
This script monitors a GUI-based application (like a VPN client) and automatically performs an action when a specific visual state is detected. Its primary use case is to monitor a VPN connection and automatically click the "Connect" button if the VPN is found to be disconnected.

However, the script is generic enough to be adapted for other UI automation tasks by simply changing the target image.

## Features
- Detects a target button or element on the screen using image recognition.
- Automatically clicks the target element when it appears.
- Configurable check interval and image-matching confidence level.
- Includes a simple Tkinter-based VPN GUI mockup for demonstration and testing purposes.

## Getting Started
Follow these steps to get the monitor up and running.

### 1. Prerequisites
   - Python 3.8+
   - Access to a terminal or command prompt.
   - Git (optional, for cloning).

### 2. Installation
First, clone the repository to your local machine (or download the source code).

```bash
git clone https://github.com/asepscareer/python-autoconnect.git
cd python-autoconnect
```

Next, it is highly recommended to create a virtual environment to keep dependencies isolated.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

Finally, install the required Python packages.
pip install -r requirements.txt

### 3. Configuration
   - Place a screenshot of the target "Connect" button from your VPN application inside the assets/ folder.
   - Rename the screenshot to connect_button.png.

### 4. Usage
To run the application, you'll need two terminal windows.

Terminal 1: Run the Mockup VPN GUI (Optional, for testing)

This will launch the simple Tkinter GUI.

```bash
python -m src.gui.vpn_gui
```

Terminal 2: Run the Monitor Script

This script will start monitoring your screen. Make sure the VPN application (either the mockup or your real one) is visible.

```bash
python -m src.main
```

The script will now check the screen at a set interval. If the connect_button.png image is found, it will automatically click it.

Folder Structure
The project uses a clean and organized structure to separate source code from assets.

```text
python-autoconnect/
├── .github/
│   └── FUNDING.yml
├── assets/
│   ├── connect_button.png
│   └── disconnect_button.png
├── src/
│   ├── __init__.py
│   ├── gui/
│   │   └── vpn_gui.py
│   └── main.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Notes
- This script relies on the pyautogui library for screen detection and automated clicks.
- For best results, ensure your screen resolution and the appearance of the target button remain consistent.
- On some operating systems, you may need to grant accessibility or screen recording permissions to your terminal or code editor for pyautogui to function correctly.

**License**: This project is licensed under the MIT License. See the `LICENSE` file for details.