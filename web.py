from flask import Flask, request, redirect ,render_template, jsonify, send_from_directory
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する
import os
import glob


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False 


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


#uploadsの画像を取得してupload.htmlと一緒に返す
@app.route("/uploads_get/")
def uploads_get():
    files = glob.glob("./uploads/*")
    fileURLlist = []
    for file in files:
        fileURLlist.append("/uploaded/" + os.path.basename(file))
    print(fileURLlist)

    return render_template("upload.html", file_list = fileURLlist)


#gray_fileの画像を取得してupload.htmlと一緒に返す
@app.route("/gray_file_get/")
def uploads_get():
    files = glob.glob("./gray_file/*")
    fileURLlist = []
    for file in files:
        fileURLlist.append("/grayscaling/" + os.path.basename(file))
    print(fileURLlist)

    return render_template("upload.html", file_list = fileURLlist)


#Canny_fileの画像を取得してupload.htmlと一緒に返す
@app.route("/Canny_file_get/")
def uploads_get():
    files = glob.glob("./Canny_file/*")
    fileURLlist = []
    for file in files:
        fileURLlist.append("/Canny_filter/" + os.path.basename(file))
    print(fileURLlist)

    return render_template("upload.html", file_list = fileURLlist)



#cssを返す
@app.route('/uploads_get/<path:filename>')
def send_css(filename):
    return send_from_directory('./templates', filename)


#uploadsの画像を返す
@app.route('/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('./uploads', filename)


#gray_fileの画像を返す
@app.route('/grayscaling/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('./gray_file', filename)


#gray_fileの画像を返す
@app.route('/Canny_filter/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('./Canny_file', filename)



if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)