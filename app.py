from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    direction = data['direction'] 
    
    if direction == 'en_to_hi':
        translated_text = translator.translate(text, src='en', dest='hi').text
    elif direction == 'hi_to_en':
        translated_text = translator.translate(text, src='hi', dest='en').text
    else:
        translated_text = "Invalid translation direction"
    
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
