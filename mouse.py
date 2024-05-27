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
        print('Miscrit is trained')
        return False
    else:
        print('Not trained')
    
    pyautogui.moveTo(final_point[0], final_point[1], duration=0)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)
    return True

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

time.sleep(3)

perform_actions_in_loop()

