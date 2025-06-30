import pyautogui
import time
import os

# --- CONFIGURATION ---
CONNECT_BUTTON_IMAGE = 'connect_button.png'
CHECK_INTERVAL = 10
CONFIDENCE_LEVEL = 0.98 
POST_CLICK_DELAY = 15
# ---------------------


def main():    
    script_dir = os.path.dirname(__file__) 
    image_path = os.path.join(os.path.dirname(script_dir), 'assets', CONNECT_BUTTON_IMAGE)

    print("✅ VPN Monitor Script Started.")
    print(f"   - Will check every {CHECK_INTERVAL} seconds.")
    print(f"   - Looking for image: {CONNECT_BUTTON_IMAGE} with confidence {CONFIDENCE_LEVEL}")
    print("   - Press Ctrl+C in this terminal to stop the script.")

    if not os.path.exists(image_path):
        print(f"🔴 FATAL ERROR: Image file not found at '{image_path}'")
        return

    while True:
        print(f"\n--- [{time.ctime()}] Checking VPN status...")

        try:
            # STEP 1: Try to find the 'Connect' button
            print("   Searching for 'Connect' button on the screen...")
            connect_button_location = pyautogui.locateOnScreen(image_path, confidence=CONFIDENCE_LEVEL, grayscale=True)
            
            # If the above line succeeds without error, the button is FOUND.
            # We can click it directly without an 'if'.
            print("   ⚠️  Status: Disconnected! 'Connect' button found.")
            print("   Attempting to reconnect...")
            
            pyautogui.click(connect_button_location)
            
            print(f"   ✅ 'Connect' button clicked successfully!")
            print(f"   Waiting {POST_CLICK_DELAY} seconds for connection process to complete...")
            time.sleep(POST_CLICK_DELAY)

        except pyautogui.ImageNotFoundException:
            # THIS BLOCK IS WHAT WE WANT IF THE BUTTON IS NOT FOUND.
            # This is not an error, but a normal condition when VPN is connected.
            print("   👍 Status: Connected ('Connect' button not found).")
        
        except Exception as e:
            # This block catches any other unexpected errors
            print(f"🔴 Unexpected error occurred during checking: {e}")
        
        finally:
            # This block will always be executed, error or not.
            # A good place to put the wait time.
            print(f"   Waiting {CHECK_INTERVAL} seconds for the next check...")
            time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Program stopped by user. Goodbye!")