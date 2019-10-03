from flask import *
import gtts
#from pygame import mixer


app = Flask(__name__)

@app.route('/texttospeech/' , methods = ['PUT'])
def texttospeech():
	if request.method == 'PUT':
		filename = images.save(request.file['img1'])
		return filename