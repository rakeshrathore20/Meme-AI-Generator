import os
import random
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


load_dotenv()
api_key = os.getenv("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")
client = OpenAI(api_key=api_key)


default_prompts = [
    "When you realize it's Monday again",
    "That face you make when the code works on first try",
    "Trying to act normal when you're sleep deprived",
    "When someone says 'just add AI to it'",
    "When the client asks for one more change",
    "Me explaining memes to my grandparents",
    "When you're debugging and it suddenly works",
    "Trying to look productive in Zoom meetings",
    "When the pizza guy arrives during a meeting",
    "When you accidentally reply all to the company email"
]

# Streamlit 
st.set_page_config(page_title="Meme AI Generator", page_icon="😂", layout="centered")
st.title("Meme AI Generator - RAKESH KUMAR")
st.markdown("Upload an image and let AI write a meme caption for you!")

# --- Functions ---
def generate_caption(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a funny meme caption generator."},
                {"role": "user", "content": f"Write a hilarious meme caption about: {prompt}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating caption: {e}"

def add_caption_to_image(image, caption):
    draw = ImageDraw.Draw(image)
    font_path = "arial.ttf"
    font_size = 32
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()

    width, height = image.size
    bbox = draw.textbbox((0, 0), caption, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = height - text_height - 20

    # Text 
    outline_range = 2
    for dx in range(-outline_range, outline_range + 1):
        for dy in range(-outline_range, outline_range + 1):
            draw.text((x + dx, y + dy), caption, font=font, fill="black")

    draw.text((x, y), caption, font=font, fill="white")
    return image

#  UI 
uploaded_file = st.file_uploader("Upload your image (jpg/png)", type=["jpg", "jpeg", "png"])
prompt = st.text_input("Want to give your own meme idea? ")

if st.button("Generate Meme"):
    if not uploaded_file:
        st.error("Please upload an image first!")
    else:
        with st.spinner("Generating your meme..."):
            if not prompt:
                prompt = random.choice(default_prompts)
            caption = generate_caption(prompt)
            image = Image.open(uploaded_file).convert("RGB")
            meme = add_caption_to_image(image, caption)

            buf = BytesIO()
            meme.save(buf, format="JPEG")
            byte_im = buf.getvalue()

            st.image(meme, caption=caption)
            st.download_button("📥 Download Meme", data=byte_im, file_name="meme.jpg", mime="image/jpeg")
            st.success("Meme created successfully!")
