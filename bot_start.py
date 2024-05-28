import os
import pyautogui
import time
from snippet_capture import capture_snippet
from compare import compare_images
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Paths and coordinates from environment variables
image1_path = os.getenv('IMAGE1_PATH')
image2_path = os.getenv('IMAGE2_PATH')
x_enem = int(os.getenv('X_ENEM'))
y_enem = int(os.getenv('Y_ENEM'))
x_train = int(os.getenv('X_TRAIN'))
y_train = int(os.getenv('Y_TRAIN'))

# Points for automation
point2 = (584, 606)
point1 = (1296, 269)
intermediate_point1 = (660, 934)
intermediate_point2 = (873, 813)

# Path for battle image check
battle_or_not_path = 'enemy_checks/battle_or_not.png'

def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f'Deleted: {filepath}')
    else:
        print(f'File not found: {filepath}')

def move_and_click(point, duration=0):
    pyautogui.moveTo(point[0], point[1], duration=duration)
    pyautogui.click()

def capture_and_compare(x, y, name, width, height, static_image, threshold=0.7):
    capture_snippet(x=x, y=y, name=name, width=width, height=height)
    return compare_images(image1_name=static_image, image2_name=name, threshold_score=threshold)

def handle_battle():
    capture_snippet(x=1163, y=100, name='battle_or_not', width=125, height=25)
    return capture_and_compare(x=1163, y=100, name='battle_or_not', width=125, height=25, static_image='battle_static')

def handle_enemy_health():
    capture_snippet(x=x_enem, y=y_enem, name='enemy_health1', width=200, height=100)
    for _ in range(10):
        pyautogui.click()
        time.sleep(7)
        capture_snippet(x=x_enem, y=y_enem, name='enemy_health2', width=200, height=100)
        if not compare_images(image1_name='enemy_health1', image2_name='enemy_health2', threshold_score=0.6):
            print('Enemy Miscrit is dead')
            break

def handle_training():
    capture_snippet(x=x_train, y=y_train, name='is_training_complete', width=190, height=25)
    if compare_images(image1_name='is_training_complete', image2_name='training', threshold_score=0.7):
        perform_post_training_actions()
        return True
    return False

def close_action(final_point):
    move_and_click(final_point, duration=0.2)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)

def perform_actions_at_point(start_point, intermediate_point, final_point):
    move_and_click(start_point)
    print(f'Clicked at {start_point} to find miscrits')
    time.sleep(8)

    if not handle_battle():
        print(f'No battle at {start_point}, exiting method.')
        return

    time.sleep(5)
    handle_enemy_health()
    trained = handle_training()
    close_action(final_point)
    
    if trained:
        print('Training complete, performing post-training actions.')
    else:
        print('Not trained.')

    print(f'Exiting perform_actions_at_point at {start_point}, {intermediate_point}, {final_point}')

def perform_post_training_actions():
    steps = [
        (555, 82, 2),
        (597, 310, 2),
        (925, 195, 3),
        (774, 892, 2),
        (1055, 892, 6),
        (1313, 162, 2)
    ]

    for x, y, sleep_time in steps:
        pyautogui.moveTo(x, y, duration=0)
        time.sleep(sleep_time)

        if (x, y) == (1313, 162):
            capture_and_compare(x=635, y=407, name='new_ability', width=500, height=250, static_image='new_ability_static')
            if compare_images(image1_name='new_ability_static', image2_name='new_ability', threshold_score=0.7):
                close_action((879, 658))
                pyautogui.moveTo(x, y, duration=0)
            capture_and_compare(x=1088, y=241, name='evolution_or_not', width=50, height=25, static_image='evolution_static')
            if compare_images(image1_name='evolution_or_not', image2_name='evolution_static', threshold_score=0.7):
                close_action((878, 813))
                close_action((878, 759))
                pyautogui.moveTo(x, y, duration=0)
        pyautogui.click()
def perform_actions_in_loop():
    points = [
        (point1, intermediate_point1, intermediate_point2),
        (point2, intermediate_point1, intermediate_point2)
    ]
    
    print('Starting the bot')
    while True:
        for start_point, intermediate_point, final_point in points:
            print(f'Entering loop with points: {start_point}, {intermediate_point}, {final_point}')
            if not perform_actions_at_point(start_point, intermediate_point, final_point):
                break
        else:
            continue  
        break  

if __name__ == "__main__":
    delete_file(battle_or_not_path)
    time.sleep(3)
    perform_actions_in_loop()
