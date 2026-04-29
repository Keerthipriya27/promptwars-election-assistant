# Election Process Education Assistant

An interactive, non-partisan AI assistant designed to help users understand the election process, timelines, and key steps for voting.

## Challenge 2 - Election Process Education

This project was built for Challenge 2 to help educate users on the election process in an easy-to-follow, interactive way.

## Features
- **Interactive Chatbot**: Ask questions about voter registration, important dates, and voting methods.
- **Visual Timeline**: A quick reference guide to the key steps in the voting process.
- **Strictly Non-Partisan**: The assistant is programmed to focus *only* on the factual civic process and never discuss political preferences or candidates.

## Demo Video
Watch the deployment demo here: [YouTube Demo](https://www.youtube.com/watch?v=FMqCzBu_KIc)

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment variables:
   Copy `.env.example` to `.env` and add your Google Gemini API Key.
   ```bash
   GEMINI_API_KEY=your_actual_key_here
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`
