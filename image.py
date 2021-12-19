import cv2
import numpy as np
import os
import glob

#画像のグレースケール化（二値化していない）

def gray_scale(image):    
    color_img = cv2.imread(image)
    im_gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(f'gray_file/{os.path.basename(image)}', im_gray)
    

#Cannyによる画像検出

def canny_filta(image):
    img = cv2.imread(image)
    img_canny = cv2.Canny(img, 100, 200)
    cv2.imwrite(f'Canny_file/{os.path.basename(image)}', img_canny)

#モザイク処理

def mozaic_filta(image):
	cascade_file= "haarcascade_frontalface_default.xml"
	clas = cv2.CascadeClassifier(cascade_file)
	img_mozaic = cv2.imread(image)

	face_list = clas.detectMultiScale(img_mozaic, scaleFactor = 1.1, minSize=(30,30))

	for x, y, w, h in face_list:
		face= img_mozaic[y:y+h, x:x+w]
		small_pic = cv2.resize(face, (8,8))
		mosaic = cv2.resize(small_pic,(w,h))
		img_mozaic[y:y+h, x:x+w]=mosaic

	cv2.imwrite(f'Mozaic_file/{os.path.basename(image)}', img_mozaic)


# 動作確認用
if __name__=="__main__":
    files = glob.glob("./uploads/*")
    for file in files:
        gray_scale(file)
        canny_filta(file)
        mozaic_filta(file)

