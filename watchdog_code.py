#wathdogを使用する際はターミナル等で pip install watchdog　を実行しインストールしないと使えないかも?しれません。

import time
import sys
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


from image import gray_scale, canny_filta #画像処理用のプログラム

#import 実行したい画像処理プログラム


target_dir = "uploads" #uploadsフォルダを監視フォルダに指定

#LoggingEvenHandlerを上書きして動作を変更
class LoggingEventHandler2(FileSystemEventHandler):
    #ファイルやフォルダが更新された場合
    def on_modified(self, event):    #on_created -> on_modifiedに変更
        print("------------------------------------------")
        filepath = event.src_path
        filename = os.path.basename(filepath)
        if filename in target_dir:
            return

        print("filepath: ", filepath)
        print("filename: ", filename)

        try:
            gray_scale(filepath)    #関数を実行
            canny_filta(filepath)   #関数を実行

        except:
            print("画像処理できませんでした。")



        print(filename+"が追加されました。")#debug用おk
        #ファイルに画像が入ってきた時に画像処理をするプログラムを起動
        



if __name__ == "__main__":
    path = target_dir #監視フォルダのパス
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

