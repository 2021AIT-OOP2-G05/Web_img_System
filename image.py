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
    img_origin = cv2.imread(image)
    img_gray = cv2.imread(image,0)

    img_rect = img_origin.copy()
    img_mosaic = img_origin.copy()

    cascade_file= "haarcascade_frontalface_default.xml"
    clas = cv2.CascadeClassifier(cascade_file)
    face_list = clas.detectMultiScale(img_gray)

    if len(face_list) > 0:
        for face in face_list:
            x, y, w, h = face

            # 検出した顔の範囲を四角で囲む
            img_rect = cv2.rectangle(img_rect, (x, y), (x+w, y+h), color=(255, 255, 255), thickness=2)

            # 検出した顔の範囲をモザイクする
            mosaic = img_mosaic[y:y+h, x:x+w]
            mosaic = cv2.resize(mosaic, (w//50, h//50))
            mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)
            img_mosaic[y:y+h, x:x+w] = mosaic 
    cv2.imwrite(f'mosaic_file/{os.path.basename(image)}', img_mosaic)


# 動作確認用
if __name__=="__main__":
    files = glob.glob("./uploads/*")
    for file in files:
        gray_scale(file)
        canny_filta(file)
        mozaic_filta(file)

