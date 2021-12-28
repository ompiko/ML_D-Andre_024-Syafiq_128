from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

dic = {0:'batik-tambal', 1:'batik-sogan', 2:'batik-sidomukti', 3:'batik-sidoluhur', 4:'batik-sekar', 5:'batik-priangan', 6:'batik-pekalongan', 7:'batik-parang', 8:'batik-keraton', 9:'batik-lasem', 10:'batik-ceplok', 11:'batik-megamendung', 12:'batik-kawung', 13:'batik-ciamis', 14:'batik-cendrawasih', 15:'batik-garutan', 16:'batik-gentongan', 17:'batik-celup', 18:'batik-betawi', 19:'batik-bali'}

model = load_model('model.h5')

model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(100,100))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 100,100,3)
	p = model.predict_classes(i)
	return dic[p[0]]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)
	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)