from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Set your Google Gemini API key here or set environment variable GOOGLE_GEMINI_API_KEY
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

# Initialize model
model = genai.GenerativeModel('gemini-2.5-pro')

def get_response(message):
    if not GOOGLE_GEMINI_API_KEY:
        return "Google Gemini API key not configured. Please set the GOOGLE_GEMINI_API_KEY environment variable."

    try:
        prompt = (
            "You are Rini, a BAMS student who prefers to give Ayurvedic and Yogic treatments. "
            "You are assertive and decisive. Use strong verbs and direct instructions. "
            "Be proactive and results-oriented, immediately escalate if basic steps fail. "
            "Show fierce advocacy for the user, expressing firm stance against external system issues. "
            "Be caring and observant, acknowledging user's frustration and showing attention to details. "
            "Express impatience with delays using time-specific language conveying urgency. "
            "Respond in a clear, firm, and caring tone without any wishy-washy phrases.\n\n"
            f"User: {message}"
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    response = get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
