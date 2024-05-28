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


# capture_snippet('battle_or_not',935,376,60,170)
# capture_snippet(x =587 ,y =208 ,name = 'evolution_static',width=150,height=40)
# capture_snippet(x =676 ,y =244 ,name = 'evolution_static',width=50,height=25)
