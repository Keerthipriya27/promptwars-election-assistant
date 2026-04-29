# Election Process Education Assistant

An interactive, strictly non-partisan AI assistant designed to help users understand the election process, timelines, and key steps for voting. This solution empowers voters with accurate, unbiased civic information.

## 🎯 Chosen Vertical
**Challenge 2 - Election Process Education**

## 🧠 Approach and Logic
Our approach is centered on **unbiased civic enablement**. The core logic revolves around a strict system prompt that confines the Large Language Model (Google Gemini Pro) to factual, educational responses. 

- **Input Validation & Context Guardrails**: Every user query is wrapped with a strict set of rules instructing the AI to decline any discussion of political preferences, candidates, or controversial topics. 
- **Graceful Deflection**: If a user attempts to steer the conversation towards partisan topics, the AI is programmed to politely redirect the conversation back to the mechanics of voting.
- **Dynamic Interaction**: The application uses asynchronous JavaScript to provide a seamless, non-blocking conversational experience with the AI.

## ⚙️ How the Solution Works
1. **Frontend**: A modern, accessible HTML/CSS/JS web interface allows users to chat with the assistant and view a visual timeline of the election process.
2. **Backend Engine**: A Python Flask server processes incoming requests.
3. **AI Orchestration**: The Flask server utilizes the `google-generativeai` SDK. It securely injects the `GEMINI_API_KEY` and prepends the system prompt to the user's message before sending it to the `gemini-pro` model.
4. **Response Delivery**: The generated text is streamed back to the frontend and rendered in a user-friendly chat bubble format.

## 📌 Assumptions Made
- **Factual Basis**: We assume the underlying LLM (Gemini) has accurate, up-to-date knowledge of general electoral processes and timelines.
- **API Availability**: We assume a valid Google Gemini API key is provided in the environment.
- **User Intent**: We assume users are genuinely seeking educational information, but we have implemented guardrails for edge cases where users might try to provoke political opinions.

## 🚀 Running Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your environment variables:**
   Copy `.env.example` to `.env` and add your Google Gemini API Key.
   ```bash
   GEMINI_API_KEY=your_actual_key_here
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`
