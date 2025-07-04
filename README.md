#Meme AI Generator

This tool generates funny meme captions using OpenAI and lets users create memes by uploading an image or selecting a template. It's useful for content creators, marketers, and meme enthusiasts.

Features:
- Upload your own image or use a preloaded meme template
- Enter a text prompt to generate a meme caption using AI
- Automatically adds the caption to the image
- Option to download the final meme

Tech Stack:
- Python
- Streamlit for the UI
- OpenAI API for caption generation
- Pillow (PIL) for image manipulation

How to Use:
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Set your OpenAI API key in a .env file:
   OPENAI_API_KEY=your_api_key_here
4. Run the app:
   streamlit run memeai.py

Notes:
- Works best with clear and simple meme ideas
- Requires a valid OpenAI API key
- Tested with GPT-4 and GPT-3.5
