import os
import cv2
from skimage.metrics import structural_similarity as compare_ssim
from dotenv import load_dotenv

load_dotenv()

def compare_images(image1_name, image2_name,threshold_score):
    
    image_path = os.getenv('IMAGE_PATH')
    
    image1_path = os.path.join(image_path, image1_name+'.png')
    image2_path = os.path.join(image_path, image2_name+'.png')
    
    print('From compare_images method:  IMAGES PATH',image1_path,' ',image2_path)
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    (score, _) = compare_ssim(gray_image1, gray_image2, full=True)

    formatted_score = float(format(score, 'f'))
    print(formatted_score)
    if formatted_score >= threshold_score:
        print('score greater')
        return True
    else:
        print('score lesser')
        return False

# print(compare_images(image1_name='battle_static',image2_name='battle_or_not',threshold_score=0.7))
# compare_images(image1_name='evolution_or_not',image2_name='evolution_static',threshold_score=0.7)