import time
import sys
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#import 実行したい画像処理プログラム

target_dir = "監視したいフォルダのパス"

#LoggingEvenHandlerを上書きして動作を変更
class LoggingEventHandler2(FileSystemEventHandler):
    def on_created(self, event):    
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
    except KeyboardInterrupt:
        observer.stop()
        observer.join()