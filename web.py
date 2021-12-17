from flask import Flask, request, redirect ,render_template, jsonify, send_from_directory
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する
import os
import glob


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False 


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload_list/')
def upload_list_link():
    
    return render_template("upload.html")


@app.route("/uploads/",methods=["POST"])
def upload():
    if ("file" in request.files): #存在確認
        upload_folder = "./uploads/"
        file = request.files["file"]

        if '' == file.filename:
            return render_template("index.html", error="ファイルを指定してください。")

            file.save(os.path.join(upload_folder ,file.filename)) #file.filenameでファイル名取得
            return render_template("index.html", message="ファイルのアップロードしました。")

        else: return render_template("index.html", message="ファイルのアップロードできませんでした。")


#uploadsの画像を取得してupload.htmlと一緒に返す
@app.route("/uploads_get/")
def uploads_get():
    files = glob.glob("./uploads/*")
    fileURLlist = []
    for file in files:
        fileURLlist.append("/uploaded/" + os.path.basename(file))

    return render_template("upload.html", title = 'uploads', file_list = fileURLlist)


#gray_fileの画像を取得してupload.htmlと一緒に返す
@app.route("/gray_file_get/")
def gray_file_get():
    files = glob.glob("./gray_file/*")
    fileURLlist = []
    for file in files:
        fileURLlist.append("/grayscaling/" + os.path.basename(file))

    return render_template("upload.html", title = 'gray_file', file_list = fileURLlist)


#Canny_fileの画像を取得してupload.htmlと一緒に返す
@app.route("/Canny_file_get/")
def Canny_file_get():
    files = glob.glob("./Canny_file/*")
    fileURLlist = []
    for file in files:
        fileURLlist.append("/Canny_filter/" + os.path.basename(file))

    return render_template("upload.html", title = 'Canny_file', file_list = fileURLlist)


#cssを返す
@app.route('/uploads_get/<path:filename>')
def send_css(filename):
    return send_from_directory('./templates', filename)


#uploadsの画像を返す
@app.route('/uploaded/<path:filename>')
def uploaded_uploads(filename):
    return send_from_directory('./uploads', filename)


#gray_fileの画像を返す
@app.route('/grayscaling/<path:filename>')
def uploaded_gray_file(filename):
    return send_from_directory('./gray_file', filename)


#gray_fileの画像を返す
@app.route('/Canny_filter/<path:filename>')
def uploaded_Canny_file(filename):
    return send_from_directory('./Canny_file', filename)




if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)