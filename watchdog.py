
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


#wathdogを使用する際はターミナル等で pip install watchdog　を実行しインストールしないと使えないかも?しれません。

import time
import sys
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


from image import image #画像処理用のプログラム

#import 実行したい画像処理プログラム


target_dir = "監視したいフォルダのパス"

#LoggingEvenHandlerを上書きして動作を変更
class LoggingEventHandler2(FileSystemEventHandler):
    def on_created(self, event):    

        print(event.src_path+"が生成されました。")#debug用おk
        #ファイルに画像が入ってきた時に画像処理をするプログラムを起動

if __name__ == "__main__":
    path = target_dir #監視ファイルのパス

    print("生成されました。" + event.src_path)

if __name__ == "__main__":
    path = target_dir

    event_handler = LoggingEventHandler2()
    observer = Observer()       #監視オブジェクト生成
    observer.schedule(          #監視設定
        event_handler,
        path,
        recursive=True
        )
    observer.start()            #監視開始
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:#　^+Cで終了
        observer.stop()
        observer.join()

