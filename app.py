from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from datetime import datetime

app = Flask(__name__)

# Configure the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create a generative model instance
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        if not user_message.strip():
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get current date and time
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%A, %B %d, %Y")
        current_time = current_datetime.strftime("%I:%M %p")
        
        # Add current date/time context to the message
        enhanced_message = f"""Current date and time: {current_date} at {current_time}

User question: {user_message}

Please provide accurate information based on the current date and time provided above."""
        
        # Generate response from Gemini
        response = model.generate_content(enhanced_message)
        
        return jsonify({
            'response': response.text,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080) 