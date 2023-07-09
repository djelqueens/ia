from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__,template_folder='template')

openai.api_key = os.getenv('API_KEY_OPENAI')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_response():
    message = request.form['msg']
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50
    )
    reply = response.choices[0].text.strip()

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
