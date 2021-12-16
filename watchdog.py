"""import cv2
import datetime as dt

def imagemozaic(image):
	cascade_file= "haarcascade_frontalface_default.xml"
	clas = cv2.CascadeClassifier(cascade_file)
	img = cv2.imread(image)

	face_list = clas.detectMultiScale(img, scaleFactor = 1.1, minSize=(30,30))

	for x, y, w, h in face_list:
		face= img[y:y+h, x:x+w]
		small_pic = cv2.resize(face, (8,8))
		mosaic = cv2.resize(small_pic,(w,h))
		img[y:y+h, x:x+w]=mosaic

	now = dt.datetime.now()
	time = now.strftime('%Y%m%d-%H%M')
	cv2.imwrite('/{}.jpg'.format(image),img)
	return;"""