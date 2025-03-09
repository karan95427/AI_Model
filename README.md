# AI Voice Assistant

An AI-powered virtual assistant built with Python that supports speech recognition, text-to-speech, Google Search automation, AI-generated responses using Google Gemini (Gemini-1.5 Pro), weather updates, and online music playback.

## Features
- **Voice Command Recognition**: Uses `speech_recognition` to process user voice input.
- **Text-to-Speech (TTS)**: Converts AI responses to speech using `win32com.client`.
- **AI-Powered Responses**: Integrates Google Gemini (Gemini-1.5 Pro) for generating AI responses.
- **Google Search Automation**: Opens web searches based on user queries.
- **Time Query Functionality**: Retrieves and announces the current time.
- **Music Playback (Online)**: Searches for and plays music directly from YouTube.
- **Weather Updates**: Retrieves real-time weather information for any city.
- **Chat History Management**: Resets or stores conversation history.
- **Error Handling**: Manages speech recognition and API response errors.

## Installation
### Prerequisites
Ensure you have Python 3.x installed along with the following dependencies:

```sh
pip install speechrecognition pywin32 google-generativeai pywhatkit requests
```

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/ai-assistant.git
   cd ai-assistant
   ```
2. Set up the **Google Gemini API Key** and **OpenWeatherMap API Key**:
   - Obtain an API key from [Google AI](https://ai.google.com/)
   - Obtain a weather API key from [OpenWeatherMap](https://openweathermap.org/)
   - Create a `config.py` file and add:
     ```python
     API_KEY = "your_google_gemini_api_key"
     WEATHER_API_KEY = "your_openweather_api_key"
     ```
3. Run the AI assistant:
   ```sh
   python main.py
   ```

## Usage
- Speak commands when prompted with **"Listening..."**
- Supported commands:
  - **"Search for [query]"**: Opens a Google search for the query.
  - **"The time"**: Announces the current time.
  - **"Play [song name] music"**: Searches and plays music from YouTube.
  - **"Weather in [city]"**: Retrieves the current weather for the specified city.
  - **"Using AI"**: Prompts AI to answer a query.
  - **"Reset chat"**: Clears chat history.
  - **"Ok"**: Exits the program.

## Future Improvements
- Add GUI support using Tkinter or PyQt.
- Extend capabilities to control smart home devices.
- Integrate Spotify API for more music options.
- Improve AI contextual memory.

## License
This project is licensed under the MIT License.

---
### **Contributions & Issues**
Feel free to submit pull requests or report issues. Let's build a better assistant together! 🚀

