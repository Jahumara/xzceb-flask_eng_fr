from flask import Flask, request

# Import the MyMemoryTranslator from the deep_translator package
from deep_translator import MyMemoryTranslator

# Create an instance of the MyMemoryTranslator service
translator = MyMemoryTranslator(api_key='your_api_key')

# Create a Flask application
app = Flask(__name__)

# Endpoint to translate English to French
@app.route('/englishToFrench', methods=['GET'])
def translate_english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    translation = translator.translate(text_to_translate, to_language='fr', from_language='en')
    return translation

# Endpoint to translate French to English
@app.route('/frenchToEnglish', methods=['GET'])
def translate_french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    translation = translator.translate(text_to_translate, to_language='en', from_language='fr')
    return translation

# Root endpoint to render the index.html file
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Run the Flask application
if __name__ == '__main__':
    app.run()
