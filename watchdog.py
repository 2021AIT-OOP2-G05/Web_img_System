'''林
import cv2
import numpy as np
import os

画像のグレースケール化（二値化していない）

def gray_scale(image):
    
    #im = cv2.imread(color_img)
    #color_img = cv2.imread(image)
    #im_gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    #cv2.imwrite('output1.jpeg', im_gray)

    #フォルダ作成(使うかは未定)
    #os.makedir.s('gray_directory', exist_ok = True)

Cannyによる画像検出

def canny_filta(image):
    img = cv2.imread(image)
    img_canny = cv2.Canny(img, 100, 200)
    cv2.imwrite('output2.jpeg', img_canny)

    #ファイル作成(使うかは未定)
    #os.makedirs('canny_directory', exist_ok = True)



if __name__ == "__main__":
    gray_scale()
    canny_filta()
    '''