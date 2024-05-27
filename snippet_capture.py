import pyautogui
import time
import os

def capture_snippet(name,x,y, width, height):
    # Capture the screen
    
    screenshot = pyautogui.screenshot()

    # Crop the captured image to the specified region
    snippet = screenshot.crop((x, y, x + width, y + height))
    
    time.sleep(1)
    file_path = os.path.join('enemy_checks', f'{name}.png')

    # Save the snippet as an image file
    snippet.save(file_path)


# capture_snippet('battle_or_not',851,344,225,225)
