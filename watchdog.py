#wathdogを使用する際はターミナル等で pip install watchdog　を実行しインストールしないと使えないかも?しれません。
import time
import sys
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from image import image #画像処理用のプログラム


target_dir = "監視したいフォルダのパス"

#LoggingEvenHandlerを上書きして動作を変更
class LoggingEventHandler2(FileSystemEventHandler):
    def on_created(self, event):    
        print(event.src_path+"が生成されました。")#debug用
        #ファイルに画像が入ってきた時に画像処理をするプログラムを起動

if __name__ == "__main__":
    path = target_dir #監視ファイルのパス
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