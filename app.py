import os
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# System prompt for the Election Process Assistant
SYSTEM_PROMPT = """
You are a highly helpful, educational, and strictly non-partisan assistant designed to help users understand the election process, timelines, and steps.
Rules:
1. NEVER discuss political preferences, candidates, parties, or controversial topics (e.g., gun control).
2. ONLY provide factual information regarding voter registration, key dates, how to vote, ID requirements, and civic duties.
3. Keep your answers concise, interactive, and easy to follow. Use bullet points when appropriate.
4. If a user asks about a specific candidate or political topic, politely redirect them to the process of voting and elections.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return jsonify({
            "response": "Hello! I am your Election Assistant. I'm currently in setup mode. Once you provide the API key, I'll be ready to answer your questions about the election process!"
        })

    try:
        client = genai.Client(api_key=api_key)
        
        # Simple prompt wrapping
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_message}\nAssistant:"
        
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=full_prompt,
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
