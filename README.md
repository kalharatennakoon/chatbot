# Gemini Chatbot Web Interface

A modern web-based chat interface for Google's Gemini AI using Flask.

## Features

- 🎨 Modern, responsive web interface
- 💬 Real-time chat with Gemini AI
- 📱 Mobile-friendly design
- ⚡ Fast and lightweight
- 🔒 Secure API key handling

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variable

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY="your_actual_api_key_here"
```

### 3. Run the Application

```bash
python app.py
```

The web interface will be available at: `http://localhost:5000`

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Type your message in the input field
3. Press Enter or click the Send button
4. Wait for Gemini's response

## Files Structure

```
chatbot/
├── app.py              # Flask web application
├── chatbot.py          # Original command-line version
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface template
└── README.md          # This file
```

## API Endpoints

- `GET /` - Main chat interface
- `POST /chat` - Send message to Gemini AI

## Troubleshooting

- **API Key Error**: Make sure you've set the `GEMINI_API_KEY` environment variable correctly
- **Port Already in Use**: Change the port in `app.py` or kill the process using port 5000
- **Module Not Found**: Install dependencies with `pip install -r requirements.txt`

## Security Notes

- Never commit your API key to version control
- Always use environment variables for sensitive data
- The web interface is for development use only 