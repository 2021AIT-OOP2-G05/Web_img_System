from flask import Flask, request, redirect ,render_template, jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する
import os


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# TOPページ(本当は別のWebサーバーを構築するのが良い)
# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")




@app.route("/uploads/",methods=["POST"])
def upload():
    if ("file" in request.files): #存在確認
        upload_folder = "./uploads/"
        file = request.files["file"]
        file.save(os.path.join(upload_folder ,file.filename)) #file.filenameでファイル名取得
        return redirect("/")
    else: return redirect("/")
  
@app.route("/img_get/",methods=["GET"])
def img_get():
    #
    
    return render_template("upload.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)