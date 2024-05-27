import os
import pyautogui
import time
from snippet_capture import capture_snippet
from compare import compare_images
from dotenv import load_dotenv

load_dotenv()
image1_path = os.getenv('IMAGE1_PATH')
image2_path = os.getenv('IMAGE2_PATH')

x_enem = int(os.getenv('X_ENEM'))
y_enem = int(os.getenv('Y_ENEM'))

x_train = int(os.getenv('X_TRAIN'))
y_train = int(os.getenv('Y_TRAIN'))

point2 = (584, 606)
point1 = (1296, 269)
intermediate_point1 = (660, 934)
intermediate_point2 = (873, 813)

def perform_actions_at_point(start_point, intermediate_point, final_point):
    pyautogui.moveTo(start_point[0], start_point[1], duration=0)
    pyautogui.click()
    time.sleep(4)
    capture_snippet('battle_or_not',851,344,225,225)
     
    if not (compare_images(image1_name='battle_static',image2_name='battle_or_not',threshold_score=0.6)):
        print('Comparing battle static and battle or not png')
        return True
    else:
        time.sleep(5)
        image1_name = 'enemy_health1'
        image2_name = 'enemy_health2'
        
        capture_snippet(x =x_enem ,y =y_enem ,name = image1_name,width=200,height=100)

        pyautogui.moveTo(intermediate_point[0], intermediate_point[1], duration=0)
        
        time.sleep(7)
        c = 5
        for _ in range(c):
            pyautogui.click()
            time.sleep(7)
            capture_snippet(x =x_enem ,y =y_enem ,name = image2_name,width=200,height=100)
            time.sleep(2)
            comp = compare_images(image1_name=image1_name,image2_name=image2_name,threshold_score=0.6)
            print('COMPARING IMAGES',comp)
            if  not comp:
                print('Enemy Miscrit is dead')
                break  
        
        capture_snippet(x= x_train,y = y_train,name = 'is_training_complete',width=190,height=25)
        time.sleep(1)
        print('Compare trained ',compare_images(image1_name='is_training_complete',image2_name='training',threshold_score=0.6))
        
        if compare_images(image1_name='is_training_complete',image2_name='training',threshold_score=0.7):
            close(final_point=final_point)
            print('Miscrit is trained')
            perform_post_training_actions()
            time.sleep(3)
        else:
            print('Not trained')
            close(final_point=final_point)
        return True
    

def close(final_point):
    pyautogui.moveTo(final_point[0], final_point[1], duration=0.2)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)

def perform_actions_in_loop():
    points = [(point1, intermediate_point1, intermediate_point2),
              (point2, intermediate_point1, intermediate_point2)]
    print('Starting the bot')
    while True:
        for start_point, intermediate_point, final_point in points:
            print('AT THIS POINT',start_point,' ',intermediate_point,' ',final_point)
            if not perform_actions_at_point(start_point, intermediate_point, final_point):
                break
        else:
            continue  
        break  

def perform_post_training_actions():
    steps = [
        (555, 82, 2),
        (597, 310, 2),
        (925, 195, 3),
        (1055, 892, 6),
        (1313, 162, 2)
    ]
    
    for x, y, sleep_time in steps:
        pyautogui.moveTo(x, y, duration=0)
        time.sleep(sleep_time)
        capture_snippet('new_ability',635,407,500,250)
        if compare_images(image1_name='new_ability_static',image2_name='new_ability',threshold_score=0.7):
            time.sleep(1)
            close(final_point=(879,658))
            print('New Ability')
            time.sleep(2)
            pyautogui.moveTo(x, y, duration=0)
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)
        pyautogui.click()
        
time.sleep(3)

perform_actions_in_loop()

