from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    print('User Input:', user_input)
    response = get_gpt4_response(user_input)
    print('GPT-4 Response:', response)
    return jsonify({'response': response})

def get_gpt4_response(user_input):
    response = client.chat.completions.create(
        model="gpt-4",  # or use "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    app.run(debug=True)
